from config import EXECUTED_COUNT
from src.utils import read_json, get_executed_operations, sort_operations, get_last_operations, convert_date, \
    convert_payment_info


def main():
    """
    Запуск программы
    """
    operations = read_json()
    executed_operations = get_executed_operations(operations)
    sorted_operations = sort_operations(executed_operations)
    last_operations = get_last_operations(sorted_operations, EXECUTED_COUNT)
    for operation in last_operations:
        converted_date = convert_date(operation.get("date"))
        payment_from = operation.get("from")
        payment_to = operation.get("to")
        if "открытие" in operation["description"].lower():
            print(f"{converted_date} {operation["description"]}\n"
                  f"{convert_payment_info(payment_to) if payment_to else None}\n"
                  f"{operation["operationAmount"]["amount"]} {operation["operationAmount"]["currency"]["name"]}\n")
        else:
            print(f"{converted_date} {operation["description"]}\n"
                  f"{convert_payment_info(payment_from) if payment_from else None} -> {convert_payment_info(payment_to)
                  if payment_to else None}\n"
                  f"{operation["operationAmount"]["amount"]} {operation["operationAmount"]["currency"]["name"]}\n")

if __name__ == "__main__":
    main()
