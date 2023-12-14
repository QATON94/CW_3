from datetime import datetime

from src.utils import get_mask_paymon


class Operation:
    def __init__(
            self,
            num_id: int,
            date: str | datetime,
            state: str,
            operation_amount: dict,
            description: str,
            from_: str,
            to: str
    ):
        self.num_id = num_id
        self.date = date
        self.state = state
        self.operation_amount = operation_amount
        self.description = description
        self.from_ = from_
        self.to = to


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
                    to=get_mask_paymon(operation['to']),
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


def sort_operation_by_date(operations: list[Operation]):
    """
    Функция сортирует данные по дате
    :param operations: Полученные данные
    :return: Отсортированные данные
    """
    return sorted(operations, key=lambda operation: operation.date, reverse=True)
