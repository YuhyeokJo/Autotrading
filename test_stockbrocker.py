import pytest
from pytest_mock import MockerFixture
from driver import Driver
from stock_brocker import StockBrocker


class User:
    def __init__(self, user_id, password):
        self.user_id = user_id
        self.password = password


@pytest.fixture
def user_info():
    user = User("abc", "1111")
    return user


def test_login_mock(mocker: MockerFixture, user_info):
    driver = mocker.Mock(spec=Driver)
    api = "mock"
    stock_brocker = StockBrocker("mock")
    driver.login.return_value = "[mock] abc login suceess"
    assert stock_brocker.login(user_info.user_id, user_info.password) == f"[{api}] {user_info.user_id} login success"


def test_login_nemo_mock(user_info):
    api = "nemo"
    stock_brocker = StockBrocker("nemo")
    assert stock_brocker.login(user_info.user_id, user_info.password) == f"[{api}] {user_info.user_id} login success"


def test_login_kiwer_mock(user_info):
    api = "kiwer"
    stock_brocker = StockBrocker("kiwer")
    assert stock_brocker.login(user_info.user_id, user_info.password) == f"[{api}] {user_info.user_id} login success"
