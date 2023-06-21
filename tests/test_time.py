import datetime as dt

import pytest

from bsc_utils.time import latest_td, prev_td, session_time
from bsc_utils.exceptions import SymbolNotFoundError


def test_latest_td():
    assert isinstance(latest_td('HOSE'), dt.datetime)
    assert isinstance(latest_td('BID'), dt.datetime)
    assert latest_td('HOSE') == latest_td('BID')
    with pytest.raises(SymbolNotFoundError, match='XXX not exists.'):
        latest_td('XXX')


def test_prev_td():
    assert isinstance(prev_td('HOSE'), dt.datetime)
    assert isinstance(prev_td('BID'), dt.datetime)
    assert prev_td('HOSE') == prev_td('BID')
    with pytest.raises(SymbolNotFoundError, match='XXX not exists.'):
        prev_td('XXX')


def test_session_time():
    ts_w_sessions = {
        dt.datetime(2023, 1, 1, 8, 44, 0): 'Market Close',
        dt.datetime(2023, 1, 1, 8, 45, 0): 'Future ATO Start',
        dt.datetime(2023, 1, 1, 8, 50, 0): 'Future ATO',
        dt.datetime(2023, 1, 1, 8, 59, 59): 'Future ATO End',
        dt.datetime(2023, 1, 1, 9, 0, 0): 'HOSE ATO Start',
        dt.datetime(2023, 1, 1, 9, 15, 0): 'Morning Session Start',
        dt.datetime(2023, 1, 1, 9, 15, 1): 'Morning Session',
        dt.datetime(2023, 1, 1, 11, 30, 1): 'Lunch Break',
        dt.datetime(2023, 1, 1, 13, 0, 0): 'Afternoon Session Start',
        dt.datetime(2023, 1, 1, 13, 0, 1): 'Afternoon Session',
        dt.datetime(2023, 1, 1, 14, 30, 1): 'Future/HOSE ATC',
        dt.datetime(2023, 1, 1, 14, 45, 1): 'Put-Through',
    }

    for ts, session in ts_w_sessions.items():
        assert session_time(ts) == session


def test_session_time_us():
    ts_w_sessions = {
        dt.datetime(2023, 6, 20, 20, 30, 1): 'NY Open',
        dt.datetime(2023, 6, 20, 20, 32, 0): 'NY Trading',
        dt.datetime(2023, 6, 20, 2, 59, 30): 'NY Close',
        dt.datetime(2023, 6, 20, 14, 15, 30): 'CBOE Open',
        dt.datetime(2023, 6, 20, 3, 14, 30): 'CBOE Close',
        dt.datetime(2023, 6, 20, 15, 1, 0): 'Pre-Market',
        dt.datetime(2023, 6, 20, 5, 0, 0): 'Post-Market',
        dt.datetime(2023, 6, 20, 9, 0, 0): 'Market Close',
    }

    for ts, session in ts_w_sessions.items():
        assert session_time(ts, region='US') == session
