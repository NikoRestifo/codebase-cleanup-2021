
# import the code we want to test
from app.shopping import format_usd


def test_format_usd():
    assert format_usd(9.5) == "$9.50"

# once we have some tests ...