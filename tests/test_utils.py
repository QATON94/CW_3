from datetime import datetime
from pathlib import Path

import pytest

from models.operation import Operation
from src.utils import get_all_operations, get_operation_instances, get_mask_paymon


@pytest.fixture()
def path():
    path_ = Path(__file__).parent.parent
    test_operations_path = path_.joinpath('tests', 'test_operations.json')
    return test_operations_path


@pytest.fixture()
def json_data():
    return [{'date': '2019-08-26T10:50:58.294041',
             'description': 'Перевод организации',
             'from': 'Maestro 1596837868705199',
             'id': 441945886,
             'operationAmount': {'amount': '31957.58',
                                 'currency': {'code': 'RUB', 'name': 'руб.'}},
             'state': 'EXECUTED',
             'to': 'Счет 64686473678894779589'},
            {'date': '2019-07-03T18:35:29.512364',
             'description': 'Перевод организации',
             'from': 'MasterCard 7158300734726758',
             'id': 41428829,
             'operationAmount': {'amount': '8221.37',
                                 'currency': {'code': 'USD', 'name': 'USD'}},
             'state': 'EXECUTED',
             'to': 'Счет 35383033474447895560'},
            {'date': '2018-06-30T02:08:58.425572',
             'description': 'Перевод организации',
             'from': 'Счет 75106830613657916952',
             'id': 939719570,
             'operationAmount': {'amount': '9824.07',
                                 'currency': {'code': 'USD', 'name': 'USD'}},
             'state': 'EXECUTED',
             'to': 'Счет 11776614605963066702'},
            {'date': '2018-03-23T10:45:06.972075',
             'description': 'Открытие вклада',
             'id': 587085106,
             'operationAmount': {'amount': '48223.05',
                                 'currency': {'code': 'RUB', 'name': 'руб.'}},
             'state': 'EXECUTED',
             'to': 'Счет 41421565395219882431'},
            {'date': '2019-04-04T23:20:05.206878',
             'description': 'Перевод со счета на счет',
             'from': 'Счет 19708645243227258542',
             'id': 142264268,
             'operationAmount': {'amount': '79114.93',
                                 'currency': {'code': 'USD', 'name': 'USD'}},
             'state': 'EXECUTED',
             'to': 'Счет 75651667383060284188'},
            {'date': '2019-03-23T01:09:46.296404',
             'description': 'Перевод со счета на счет',
             'from': 'Счет 44812258784861134719',
             'id': 873106923,
             'operationAmount': {'amount': '43318.34',
                                 'currency': {'code': 'RUB', 'name': 'руб.'}},
             'state': 'EXECUTED',
             'to': 'Счет 74489636417521191160'},
            {'date': '2018-12-20T16:43:26.929246',
             'description': 'Перевод организации',
             'from': 'Счет 10848359769870775355',
             'id': 214024827,
             'operationAmount': {'amount': '70946.18',
                                 'currency': {'code': 'USD', 'name': 'USD'}},
             'state': 'EXECUTED',
             'to': 'Счет 21969751544412966366'},
            {'date': '2019-07-12T20:41:47.882230',
             'description': 'Перевод организации',
             'from': 'Счет 48894435694657014368',
             'id': 522357576,
             'operationAmount': {'amount': '51463.70',
                                 'currency': {'code': 'USD', 'name': 'USD'}},
             'state': 'EXECUTED',
             'to': 'Счет 38976430693692818358'},
            {'date': '2018-08-19T04:27:37.904916',
             'description': 'Перевод с карты на карту',
             'from': 'Visa Classic 6831982476737658',
             'id': 895315941,
             'operationAmount': {'amount': '56883.54',
                                 'currency': {'code': 'USD', 'name': 'USD'}},
             'state': 'CANCELED',
             'to': 'Visa Platinum 8990922113665229'},
            {'date': '2018-07-11T02:26:18.671407',
             'description': 'Открытие вклада',
             'id': 596171168,
             'operationAmount': {'amount': '79931.03',
                                 'currency': {'code': 'RUB', 'name': 'руб.'}},
             'state': 'EXECUTED',
             'to': 'Счет 72082042523231456215'}]


@pytest.fixture()
def operation_instances(json_data):
    operation_instances = []
    for operation in json_data:
        operation_instances.append(Operation(
            num_id=operation['id'],
            date=operation['date'],
            state=operation['state'],
            operation_amount=operation['operationAmount'],
            description=operation['description'],
            from_=operation.get('from', ''),
            to=(operation['to']),
        ))
    return operation_instances


def test_get_all_operations(path, json_expected):
    json_file = get_all_operations(path)
    assert json_file == json_expected


def test_get_operation_instances(json_data):
    operation_instances = get_operation_instances(json_data)
    assert operation_instances[0].num_id == 441945886
    assert operation_instances[0].date == datetime(2019, 8, 26, 10, 50, 58, 294041)
    assert operation_instances[0].state == "EXECUTED"
    assert operation_instances[0].operation_amount == {"amount": "31957.58", "currency":
        {
            "name": "руб.",
            "code": "RUB"}}
    assert operation_instances[0].description == "Перевод организации"
    assert operation_instances[0].from_ == "Maestro 1596 83** **** 5199"
    assert operation_instances[0].to == "Счет **9589"


@pytest.mark.parametrize('num_card, expected', [("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
                                                ("Счет 72082042523231456215", "Счет **6215"),
                                                ('', '')])
def test_get_mask_paymon(num_card, expected):
    assert get_mask_paymon(num_card) == expected
