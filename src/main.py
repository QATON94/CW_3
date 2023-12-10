from src.setings import OPERATION_PATH
from src.utils import get_all_operations, get_operation_instances, sort_operation_by_date


def main() -> None:
    all_operations = get_all_operations(OPERATION_PATH)
    operation_instances = get_operation_instances(all_operations)
    sort_operations = sort_operation_by_date(operation_instances)
    for i in range(5):
        print(f'{sort_operations[i].date.strftime("%d.%m.%Y")} {sort_operations[i].description}\n'
              f'{sort_operations[i].from_} -> {sort_operations[i].to}\n'
              f'{sort_operations[i].operation_amount["amount"]} {sort_operations[i].operation_amount["currency"]["name"]}')


if __name__ == '__main__':
    main()
