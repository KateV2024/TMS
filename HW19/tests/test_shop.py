import pytest
from src.shop import Shop


@pytest.mark.parametrize("cart, item, quantity, expected", [
    ({}, "Apple", 2, {"Apple": 2}),
    ({"Apple": 2}, "Banana", 2, {"Apple": 2, "Banana": 2}),
    ({"Apple": 2, "Banana": 2}, "Pear", 0, ValueError)
]
)
def test_add_to_cart(shop, cart, item, quantity, expected):
    shop.cart = cart
    if quantity > 0:
        assert shop.add_to_cart(item, quantity) == expected
    else:
        with pytest.raises(ValueError):
            shop.add_to_cart(item, quantity)

