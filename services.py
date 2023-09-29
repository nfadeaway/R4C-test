import pandas as pd


def create_manufactured_robots_report(manufactured_robots, models, path='./reports/week-report.xlsx'):
    try:
        model_sheets = {model: {'Модель': [], 'Версия': [], 'Кол-во за неделю': []} for model in models}
        for robot in manufactured_robots:
            model_sheets[robot['model']]['Модель'].append(robot['model'])
            model_sheets[robot['model']]['Версия'].append(robot['version'])
            model_sheets[robot['model']]['Кол-во за неделю'].append(robot['total'])
        with pd.ExcelWriter(path, engine="xlsxwriter", mode='w') as excel_writer:
            for model_sheet in model_sheets.keys():
                pd.DataFrame(model_sheets[model_sheet]).to_excel(excel_writer, sheet_name=model_sheet, index=False)
                excel_writer.sheets[model_sheet].set_column(2, 2, 18)
    except Exception as err:
        print(err)
        return False
    else:
        return path
