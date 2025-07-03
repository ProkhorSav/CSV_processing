import argparse
from tabulate import tabulate
from csv_processor import read_csv, filter_rows, aggregate_column
from exceptions import CsvProcessorError


def parse_where(where_str):
    for op in ['>=', '<=', '>', '<', '=']:
        if op in where_str:
            parts = where_str.split(op, 1)
            if len(parts) == 2:
                col, val = parts
                return col.strip(), op, val.strip()
    raise ValueError("Invalid where format. Use column>value or column=value.")


def parse_aggregate(agg_str):
    # Пример agg_str: "avg=price"
    agg_type, col = agg_str.split('=')
    return col.strip(), agg_type.strip()


def main():
    parser = argparse.ArgumentParser(description="CSV Processor")
    parser.add_argument('file', help='Path to CSV file')

    parser.add_argument('--where', help='Filter condition (e.g., price>500)')
    parser.add_argument('--aggregate', help='Aggregation (e.g., avg=price)')

    args = parser.parse_args()

    try:
        rows = read_csv(args.file)

        if args.where:
            col, op, val = parse_where(args.where)
            rows = filter_rows(rows, col, op, val)

        if args.aggregate:
            col_agg, agg_type = parse_aggregate(args.aggregate)
            result = aggregate_column(rows, col_agg, agg_type)
            print(tabulate([[agg_type.upper(), col_agg.upper(), result]], headers=['AGG', 'COLUMN', 'VALUE']))
            return

        print(tabulate(rows, headers="keys"))

    except CsvProcessorError as e:
        print(f"Ошибка обработки CSV файла: {e}")


if __name__ == '__main__':
    main()