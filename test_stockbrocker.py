import pytest
from pytest_mock import MockerFixture
from auto_trading_system import AutoTradingSystem


class User:
    def __init__(self, user_id, password):
        self.user_id = user_id
        self.password = password


@pytest.fixture
def user_info():
    user = User("abc", "1111")
    return user


def test_login_mock(mocker: MockerFixture, user_info):
    driver = mocker.Mock(spec=AutoTradingSystem)
    api = "mock"
    driver.select_stock_brocker(api)
    driver.login.return_value = "[mock] abc login success"
    assert driver.login(user_info.user_id, user_info.password) == f"[{api}] {user_info.user_id} login success"


def test_login_nemo_mock(mocker: MockerFixture, user_info):
    driver = mocker.Mock(spec=AutoTradingSystem)
    api = "nemo"
    driver.select_stock_brocker(api)
    driver.login.return_value = "[nemo] abc login suceess"
    assert driver.login(user_info.user_id, user_info.password) == f"[{api}] {user_info.user_id} login success"


def test_login_kiwer_mock(mocker: MockerFixture, user_info):
    driver = mocker.Mock(spec=AutoTradingSystem)
    api = "kiwer"
    driver.select_stock_brocker(api)
    driver.login.return_value = "[kiwer] abc login suceess"
    assert driver.login(user_info.user_id, user_info.password) == f"[{api}] {user_info.user_id} login success"


class Stock:
    def __init__(self, code, price, counts):
        self.code = code
        self.price = price
        self.counts = counts


@pytest.fixture
def stock_info(mocker):
    stock = Stock("AAA", 30000, 30)
    return stock


def test_buy_mock(mocker: MockerFixture, stock_info):
    driver = mocker.Mock(spec=AutoTradingSystem)
    api = "mock"
    driver.select_stock_brocker(api)
    assert driver.buy(stock_info.code, stock_info.price,
                      stock_info.counts) == f"[{api}] {stock_info.code}, {stock_info.price}, {stock_info.counts} buy success"


def test_sell_mock(mocker: MockerFixture, stock_info):
    driver = mocker.Mock(spec=AutoTradingSystem)
    api = "mock"
    driver.select_stock_brocker(api)
    driver.sell.return_value = "[mock] abc sell success"
    assert driver.sell(stock_info.code, stock_info.price,
                       stock_info.counts) == f"[{api}] {stock_info.code}, {stock_info.price}, {stock_info.counts} sell success"


def test_get_price_mock(mocker: MockerFixture, stock_info):
    driver = mocker.Mock(spec=AutoTradingSystem)
    api = "mock"
    driver.select_stock_brocker(api)
    driver.get_price.return_value = 30000
    assert driver.get_price(stock_info.code) == f"[{api}] {stock_info.code} get_price success"
