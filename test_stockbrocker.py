import pytest
from pytest_mock import MockerFixture

from nemo_api import NemoAPI
from stock_brocker import StockBrocker


def test_login_nemo_api(mocker: MockerFixture):
    driver = mocker.Mock(spec=NemoAPI)
    stock_brocker = StockBrocker(driver)
    id = "abc"
    passward = "1111"
    driver.login(id, passward)
    assert stock_brocker.login("nemo", id, passward) == f"{id} login success"
