import pytest
from pytest_mock import MockerFixture
from driver import Driver
from stock_brocker import StockBrocker


def test_login_mock(mocker: MockerFixture):
    driver = mocker.Mock(spec=Driver)
    api = "mock"
    id = "abc"
    passward = "1111"
    stock_brocker = StockBrocker("mock", driver)
    driver.login(id, passward)
    assert stock_brocker.login(id, passward) == f"[{api}] {id} login success"


def test_login_nemo_mock(mocker: MockerFixture):
    driver = mocker.Mock(spec=Driver)
    api = "nemo"
    id = "abc"
    passward = "1111"
    stock_brocker = StockBrocker("nemo", driver)
    driver.login(id, passward)
    assert stock_brocker.login(id, passward) == f"[{api}] {id} login success"


def test_login_kiwer_mock(mocker: MockerFixture):
    driver = mocker.Mock(spec=Driver)
    api = "kiwer"
    id = "abc"
    passward = "1111"
    stock_brocker = StockBrocker("kiwer", driver)
    driver.login(id, passward)
    assert stock_brocker.login(id, passward) == f"[{api}] {id} login success"
