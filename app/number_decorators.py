def format_usd(my_price):
    """
    Formats a number as USD with a dollar sign and two decimals (and also thousands separator)

    Params my_price is a number (integer or float) that we want to format

    Examples: format_usd(10)
    """
    return f"${my_price:,.2f}"