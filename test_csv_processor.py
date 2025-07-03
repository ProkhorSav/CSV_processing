import pytest
from csv_processor import filter_rows, aggregate_column

SAMPLE_ROWS = [
    {'name': 'iphone 15 pro', 'brand': 'apple', 'price': '999', 'rating': '4.9'},
    {'name': 'galaxy s23 ultra', 'brand': 'samsung', 'price': '1199', 'rating': '4.8'},
    {'name': 'redmi note 12', 'brand': 'xiaomi', 'price': '199', 'rating': '4.6'},
    {'name': 'poco x5 pro', 'brand': 'xiaomi', 'price': '299', 'rating': '4.4'},
]


def test_filter_numeric_gt():
    filtered = filter_rows(SAMPLE_ROWS, "price", ">", "500")
    assert len(filtered) == 2


def test_filter_text_eq():
    filtered = filter_rows(SAMPLE_ROWS, "brand", "=", "xiaomi")
    assert len(filtered) == 2


def test_aggregate_avg():
    avg_price = aggregate_column(SAMPLE_ROWS, "price", "avg")
    assert round(avg_price) == 674  # (999+1199+199+299)/4 ≈ 674


def test_aggregate_min():
    min_rating = aggregate_column(SAMPLE_ROWS, "rating", "min")
    assert min_rating == 4.4


def test_aggregate_max():
    max_rating = aggregate_column(SAMPLE_ROWS, "rating", "max")
    assert max_rating == 4.9


@pytest.mark.parametrize("col", ["nonexistent"])
def test_invalid_column(col):
    with pytest.raises(Exception):
        filter_rows(SAMPLE_ROWS, col, "=", "test")