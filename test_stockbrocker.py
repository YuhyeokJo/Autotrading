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


def test_login_mock(mocker: MockerFixture, user_info):
    driver = mocker.Mock(spec=StockBrocker)
    api = "mock"
    driver.login.return_value = "[mock] abc login suceess"
    assert driver.login(user_info.user_id, user_info.password) == f"[{api}] {user_info.user_id} login success"


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
