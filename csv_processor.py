import csv
from typing import List, Dict, Any, Callable, Optional
from exceptions import ColumnNotFoundError, InvalidOperationError


class Aggregator:
    """Базовый класс для агрегаций."""

    def aggregate(self, values: List[float]) -> float:
        raise NotImplementedError


class AvgAggregator(Aggregator):
    def aggregate(self, values: List[float]) -> float:
        return sum(values) / len(values) if values else 0.0


class MinAggregator(Aggregator):
    def aggregate(self, values: List[float]) -> float:
        return min(values) if values else 0.0


class MaxAggregator(Aggregator):
    def aggregate(self, values: List[float]) -> float:
        return max(values) if values else 0.0


AGGREGATORS = {
    'avg': AvgAggregator(),
    'min': MinAggregator(),
    'max': MaxAggregator(),
}


def read_csv(file_path: str) -> List[Dict[str, Any]]:
    with open(file_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return list(reader)


def filter_rows(rows: List[Dict[str, Any]], column: str,
                operator: str, value: str) -> List[Dict[str, Any]]:
    if not rows or column not in rows[0]:
        raise ColumnNotFoundError(f"Column '{column}' not found in file.")

    op_map = {
        '>': lambda a, b: a > b,
        '<': lambda a, b: a < b,
        '=': lambda a, b: a == b,
    }
    if operator not in op_map:
        raise InvalidOperationError(f"Invalid operator '{operator}'.")

    # Определяем тип данных колонки (int/float или строка)
    sample_value = rows[0][column]
    try:
        value_cast = float(value)
        cast_func = float
    except ValueError:
        value_cast = value
        cast_func = str

    filtered = [
        row for row in rows
        if op_map[operator](cast_func(row[column]), value_cast)
    ]
    return filtered


def aggregate_column(rows: List[Dict[str, Any]], column: str,
                     agg_type: str) -> float:
    if not rows or column not in rows[0]:
        raise ColumnNotFoundError(f"Column '{column}' not found in file.")

    try:
        values = [float(row[column]) for row in rows]
    except ValueError:
        raise InvalidOperationError("Aggregation only supported for numeric columns.")

    aggregator = AGGREGATORS.get(agg_type)
    if aggregator is None:
        raise InvalidOperationError(f"Unknown aggregation type '{agg_type}'.")

    return aggregator.aggregate(values)