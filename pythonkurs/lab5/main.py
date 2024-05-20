import re


def is_html_image_code(input_str):
    pattern = r'<img\s+.*\s+src=".*\.(img|png|jpg|jpeg|gif)".*?>'
    return bool(re.match(pattern, input_str))


def get_html_image_code(input_str):
    if not isinstance(input_str, str):
        raise ValueError("Некорректный аргумент. Пожалуйста, введите строку.")

    if is_html_image_code(input_str):
        return input_str
    else:
        raise ValueError("Введенная строка не является кодом изображения HTML.")


input_string = '<img src="image.jpg" alt="Image">'
try:
    result = get_html_image_code(input_string)
    print("Введенная строка является кодом изображения HTML:")
    print(result)
except ValueError as e:
    print("Ошибка:", e)

