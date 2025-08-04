import pytest
from pytest_mock import MockerFixture
from stock_brocker import StockBrocker


class User:
    def __init__(self, user_id, password):
        self.user_id = user_id
        self.password = password


@pytest.fixture
def user_info():
    user = User("abc", "1111")
    return user


class Stock:
    def __init__(self, code, price, counts):
        self.code = code
        self.price = price
        self.counts = counts

@pytest.fixture
def stock_info():
    stock = Stock("AAA", 30000, 30)
    return stock


def test_login_mock(mocker: MockerFixture, user_info):
    driver = mocker.Mock(spec=StockBrocker)
    api = "mock"
    driver.login.return_value = "[mock] abc login success"
    assert driver.login(user_info.user_id, user_info.password) == f"[{api}] {user_info.user_id} login success"

def test_buy_mock(mocker: MockerFixture, stock_info):
    driver = mocker.Mock(spec=StockBrocker)
    api = "mock"
    driver.buy.return_value = "[mock] abc buy success"
    assert driver.buy(stock_info.code, stock_info.price, stock_info.counts) == f"[{api}] {stock_info.code} , {stock_info.price}, {stock_info.counts} buy success"

def test_sell_mock(mocker: MockerFixture, stock_info):
    driver = mocker.Mock(spec=StockBrocker)
    api = "mock"
    driver.sell.return_value = "[mock] abc sell success"
    assert driver.sell(stock_info.code, stock_info.price, stock_info.counts) == f"[{api}] {stock_info.code} , {stock_info.price}, {stock_info.counts} buy success"

def test_getPrice_mock(mocker: MockerFixture):
    driver = mocker.Mock(spec=StockBrocker)
    api = "mock"
    driver.getPrice.return_value = "[mock] abc getPrice success"
    assert driver.getPrice(stock_info.code) == f"[{api}] {stock_info.code} getPrice success"


def test_login_nemo_mock(mocker: MockerFixture, user_info):
    driver = mocker.Mock(spec=StockBrocker)
    api = "nemo"
    driver.login.return_value = "[nemo] abc login suceess"
    assert driver.login(user_info.user_id, user_info.password) == f"[{api}] {user_info.user_id} login success"


def test_login_kiwer_mock(mocker: MockerFixture, user_info):
    driver = mocker.Mock(spec=StockBrocker)
    api = "kiwer"
    driver.login.return_value = "[kiwer] abc login suceess"
    assert driver.login(user_info.user_id, user_info.password) == f"[{api}] {user_info.user_id} login success"
