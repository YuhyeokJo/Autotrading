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

def test_buy_nemo_api(mocker: MockerFixture):
    driver = mocker.Mock(spec=Driver)
    api = "nemo"
    code = "AAA"
    price = 30000
    counts = 30
    stock_brocker = StockBrocker("nemo", driver)
    driver.buy(code, price, counts)
    assert stock_brocker.buy(code, price, counts) == f"[{api}] {code} {price} {counts} 구매완료"

def test_buy_kiwi_api(mocker: MockerFixture):
    driver = mocker.Mock(spec=Driver)
    api = "nemo"
    #종목코드, 가격, 수량
    code = "AAA"
    price = 30000
    counts = 30
    stock_brocker = StockBrocker("kiwer", driver)
    driver.buy(code, price, counts)
    assert stock_brocker.buy(code, price, counts) == f"[{api}] {code} {price} {counts} 구매완료"


def test_login_kiwer_api(mocker: MockerFixture):
    driver = mocker.Mock(spec=Driver)
    api = "kiwer"
    id = "abc"
    passward = "1111"
    stock_brocker = StockBrocker("kiwer", driver)
    driver.login(id, passward)
    assert stock_brocker.login(id, passward) == f"[{api}] {id} login success"

