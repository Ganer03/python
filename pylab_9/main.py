import csv
import locale
from datetime import datetime


def parse_datetime(datetime_str):
    if datetime_str == '-' or datetime_str == '':
        return None
    locale.setlocale(locale.LC_TIME, 'ru_RU.UTF-8')
    month_names = {
        'Январь': '01',
        'Февраль': '02',
        'Март': '03',
        'Апрель': '04',
        'Май': '05',
        'Июнь': '06',
        'Июль': '07',
        'Август': '08',
        'Сентябрь': '09',
        'Октябрь': '10',
        'Ноябрь': '11',
        'Декабрь': '12'
    }
    for month_name, month_num in month_names.items():
        datetime_str = datetime_str.replace(month_name, month_num)
    return datetime.strptime(datetime_str, "%d %m %Y %H:%M")


def parse_duration(duration_str):
    parts = duration_str.split()
    if len(parts) == 0 or parts[0] == '-':
        return None
    else:
        minutes = int(parts[0])
        seconds = int(parts[2])
        return minutes * 60 + seconds


def load_data(file_path):
    data = []
    with open(file_path, 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader) 
        for row in reader:
            rating = row[9].replace(',', '.')
            rating = None if rating == '-' else float(rating)
            v1 = None if row[10] == '-' else float(row[10].replace(',', '.'))
            v2 = None if row[11] == '-' else float(row[11].replace(',', '.'))
            v3 = None if row[12] == '-' else float(row[12].replace(',', '.'))
            v4 = None if row[13] == '-' else float(row[13].replace(',', '.'))
            v5 = None if row[14] == '-' else float(row[14].replace(',', '.'))
            v6 = None if row[15] == '-' else float(row[15].replace(',', '.'))
            v7 = None if row[16] == '-' else float(row[16].replace(',', '.'))
            v8 = None if row[17] == '-' else float(row[17].replace(',', '.'))
            v9 = None if row[18] == '-' else float(row[18].replace(',', '.'))
            v10 = None if row[19] == '-' else float(row[19].replace(',', '.'))
            data.append({
                'Фамилия': row[0],
                'Имя': row[1],
                'Учреждение': row[2],
                'Отдел': row[3],
                'Адрес электронной почты': row[4],
                'Состояние': row[5],
                'Тест начат': parse_datetime(row[6]),
                'Завершено': parse_datetime(row[7]),
                'Затраченное время': parse_duration(row[8]),
                'Оценка': rating,
                'В.1': v1,
                'В.2': v2,
                'В.3': v3,
                'В.4': v4,
                'В.5': v5,
                'В.6': v6,
                'В.7': v7,
                'В.8': v8,
                'В.9': v9,
                'В.10': v10,
            })
    return data


def successful_attempts(data):
    attempts = {}
    for entry in data:
        if entry['Состояние'] == 'Завершено' and entry['Оценка'] >= 6:
            email = entry['Адрес электронной почты']
            attempt_time = entry['Завершено']
            # print(entry['Состояние'], entry['Оценка'], entry['Завершено'], attempts[email]['Завершено'])
            if email not in attempts or attempts[email]['Завершено'] > attempt_time:
                attempts[email] = entry
    return sorted(attempts.values(), key=lambda x: x['Завершено'])


if __name__ == "__main__":
    file_path = "9-1.csv"
    data = load_data(file_path)
    successful_attempts_list = successful_attempts(data)
    print('Для файла 1:')
    for attempt in successful_attempts_list:
        print(f"{attempt['Фамилия']} {attempt['Имя']}, {attempt['Адрес электронной почты']}, {attempt['Завершено']}")
    print('\n')

    file_path = "9-2.csv"
    data = load_data(file_path)
    successful_attempts_list = successful_attempts(data)
    print('Для файла 2:')
    for attempt in successful_attempts_list:
        print(f"{attempt['Фамилия']} {attempt['Имя']}, {attempt['Адрес электронной почты']}, {attempt['Завершено']}")



