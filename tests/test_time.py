import datetime as dt

from bsc_utils.time import latest_trading_day


def test_latest_trading_day():
    assert isinstance(latest_trading_day('HOSE'), dt.datetime)
    assert isinstance(latest_trading_day('BID'), dt.datetime)
    assert not latest_trading_day('XXX')
