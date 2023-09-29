from django.db.models import Count
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, FileResponse, HttpResponse
import json

from robots.models import Robot
from services import create_manufactured_robots_report
from utils import get_last_week_dates
from validators.robot_validators import validate_robot_JSON_data


@csrf_exempt
def add_robot(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
        except ValueError:
            return JsonResponse(
                data={
                    'error': 'Не JSON-формат',
                },
                json_dumps_params={
                    'ensure_ascii': False
                },
                status=404,
            )
        else:
            if not validate_robot_JSON_data(data):
                return JsonResponse(
                    data={
                        'error': 'Невалидный формат данных',
                    },
                    json_dumps_params={
                        'ensure_ascii': False
                    },
                    status=404,
                )
            else:
                try:
                    new_robot = Robot.objects.create(
                        serial=f'{data["model"]}-{data["version"]}',
                        model=data['model'],
                        version=data['version'],
                        created=data['created'],
                    )
                except Exception as err:
                    print(err)
                    return JsonResponse(
                        data={
                            'error': 'Ошибка доступа к БД',
                        },
                        json_dumps_params={
                            'ensure_ascii': False
                        },
                        status=404,
                    )
                else:
                    return JsonResponse(
                        data={
                            'status': 'Запись добавлена',
                        },
                        json_dumps_params={
                            'ensure_ascii': False
                        },
                    )


def get_factory_report(request):
    start_week, end_week = get_last_week_dates()
    manufactured_robots = Robot \
        .objects.filter(created__gte=start_week, created__lt=end_week) \
        .values('model', 'version') \
        .annotate(total=Count('id'))
    models = {row['model'] for row in manufactured_robots}
    report = create_manufactured_robots_report(manufactured_robots, models)
    if report:
        return FileResponse(open(report, 'rb'))
    else:
        return HttpResponse('Ошибка создания отчёта')
