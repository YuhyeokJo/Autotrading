import pytest
from pytest_mock import MockerFixture
from driver import Driver
from kiwer_api import KiwerAPI
from nemo_api import NemoAPI
from stock_brocker import StockBrocker


def test_login_nemo_api(mocker: MockerFixture):
    driver = mocker.Mock(spec=Driver)
    api = "nemo"
    id = "abc"
    passward = "1111"
    stock_brocker = StockBrocker("nemo", driver)
    driver.login(id, passward)
    assert stock_brocker.login(id, passward) == f"[{api}] {id} login success"


def test_login_kiwer_api(mocker: MockerFixture):
    driver = mocker.Mock(spec=Driver)
    api = "kiwer"
    id = "abc"
    passward = "1111"
    stock_brocker = StockBrocker("kiwer", driver)
    driver.login(id, passward)
    assert stock_brocker.login(id, passward) == f"[{api}] {id} login success"

