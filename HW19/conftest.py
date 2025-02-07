import pytest
from src.shop import Shop

@pytest.fixture()
def shop():
    return Shop()
