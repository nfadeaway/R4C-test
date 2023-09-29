from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

from robots.models import Robot
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
