import json
from datetime import datetime

from models.operation import Operation


def get_all_operations(path) -> list[dict]:
    """
    функция получения операций из файла
    :param path: путь к файлу
    :return: список словарей с операциями
    """
    with open(path, encoding='utf=8') as f:
        return json.load(f)


def get_operation_instances(operations: list[dict]) -> list[Operation]:
    """
    Функция получет операции в нужном формате
    :param operations: список словарей с операциями
    :return: список классов с операциями
    """
    operation_instances = []
    for operation in operations:
        if operation:
            if operation['state'] == 'EXECUTED':
                operation_instance: Operation = Operation(
                    num_id=operation['id'],
                    date=convert_datetime(operation['date']),
                    state=operation['state'],
                    operation_amount=operation['operationAmount'],
                    description=operation['description'],
                    from_=get_mask_paymon(operation.get('from', '')),
                    to=operation['to'],
                )
        operation_instances.append(operation_instance)
    return operation_instances


def convert_datetime(date: str) -> datetime:
    """
    Функция изменяет строку времени в вид dd.mm.YYYY
    :param date: Дата
    :return: Дата в формате datetime
    """
    return datetime.strptime(date, format('%Y-%m-%dT%H:%M:%S.%f'))


def get_mask_paymon(payment_method: str) -> str:
    if payment_method != '':
        list_info = payment_method.split()
        name = ' '.join(list_info[:-1])
        number = list_info[-1]
        if 'Счет' == name.lower():
            mask_paymon = name+' **'+number[-4:]
            print(mask_paymon)
        else:
            mask_paymon = name+' '+number[:4]+' '+number[4:6]+'** **** '+number[-4:]
    else:
        mask_paymon = ''
    return mask_paymon


def sort_operation_by_date(operations: list[Operation]):
    return sorted(operations, key=lambda operation: operation.date, reverse=True)
