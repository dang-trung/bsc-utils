import datetime as dt
from typing import Literal

from .database import Database, query
from .resources import queries


def latest_trading_day(symbol: str) -> dt.datetime:
    return trading_day_by_ord(symbol, ord=0)


def trading_day_by_ord(symbol: str, ord: int) -> dt.datetime:
    r = query(
        Database.ORACLE,
        queries.ORACLE.trading_days_ago(symbol_type(symbol)),
        params=(symbol, ord + 1),
        as_df=False
    )

    return r[0].get('TRADE_DATE')


def symbol_type(symbol: str) -> Literal['EXCHANGE', 'SECURITY']:
    exchange_codes = query(
        Database.ORACLE,
        'SELECT DISTINCT(EXCHANGE_CODE) FROM EXCHANGE_DAILY',
        as_df=False
    )
    exchange_codes = [c['EXCHANGE_CODE'] for c in exchange_codes]

    if symbol in exchange_codes:
        return 'EXCHANGE'
    else:
        return 'SECURITY'