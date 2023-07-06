import datetime as dt

import pandas as pd

from bsc_utils.crawl import yf, fred


def test_yf():
    quotes = yf(
        ticker='^SPX',
        interval='1D',
        start=dt.datetime(2023, 6, 10),
        end=dt.datetime(2023, 6, 20)
    )
    assert type(quotes) == pd.DataFrame
    assert len(quotes) == 5


def test_fred():
    series = fred('WALCL')
    assert type(series) == pd.DataFrame
    assert len(series) > 0