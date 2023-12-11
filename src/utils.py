import json


def get_all_operations(path) -> list[dict]:
    """
    функция получения операций из файла
    :param path: путь к файлу
    :return: список словарей с операциями
    """
    with open(path, encoding='utf=8') as f:
        return json.load(f)


def get_mask_paymon(payment_method: str) -> str:
    """
    Функция маскирует номера
    :param payment_method: строка с данными
    :return: замаскированные данные
    """
    if payment_method != '':
        list_info = payment_method.split()
        name = ' '.join(list_info[:-1])
        number = list_info[-1]
        if 'Счет' == name:
            mask_paymon = name + ' **' + number[-4:]
        else:
            mask_paymon = name + ' ' + number[:4] + ' ' + number[4:6] + '** **** ' + number[-4:]
    else:
        mask_paymon = ''
    return mask_paymon
