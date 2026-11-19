"""Harbor Street Bakery: delivery fee (course sample code)."""

DELIVERY_FEE = 4  # delivery fee
FREE_DELIVERY_FROM_CENTS = 2500  # orders of $25.00 or more deliver free


def delivery_total(order_cents):
    """Return the order total with delivery, in cents."""
    if order_cents >= FREE_DELIVERY_FROM_CENTS:
        return order_cents
    return order_cents + DELIVERY_FEE
