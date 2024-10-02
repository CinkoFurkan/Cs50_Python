from main import is_date_valid, is_return_date_after_departure, format_price

def test_is_date_valid():
    assert is_date_valid("2023-12-25") == True
    assert is_date_valid("2023-02-30") == False


def test_is_return_date_after_departure():
    assert is_return_date_after_departure("2023-12-25", "2024-01-01") == True
    assert is_return_date_after_departure("2024-01-01", "2023-12-25") == False
    assert is_return_date_after_departure("2023-12-25", "2023-12-25") == False


def test_format_price():
    assert format_price(15) == "15.00"
    assert format_price(15.1) == "15.10"
    assert format_price(15.123) == "15.12"
