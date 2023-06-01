import pandas as pd

from bsc_utils.database import Database, connect, query


def test_connect():
    connect(database=Database.MSSQL)
    connect(database=Database.ORACLE)
    connect(database=Database.SQLITE)


def test_query_mssql():
    r = query(Database.MSSQL, 'SELECT TOP 1 SYMBOL FROM STOCK_SYMBOLS')
    assert isinstance(r, pd.DataFrame)
    assert r.shape == (1, 1)


def test_query_oracle():
    r = query(
        Database.ORACLE,
        'SELECT SECURITY_CODE FROM SECURITIES FETCH FIRST 1 ROWS ONLY'
    )
    assert isinstance(r, pd.DataFrame)
    assert r.shape == (1, 1)


def test_query_sqlite():
    r = query(
        Database.SQLITE,
        'SELECT SYMBOL FROM SYMBOL_TYPES WHERE SYMBOL_TYPE = "CKCS" LIMIT 1'
    )
    assert isinstance(r, pd.DataFrame)
    assert r.shape == (1, 1)
    

def test_query_index():
    r = query(
        Database.ORACLE,
        '''
        SELECT
            TRADE_DATE, 
            EXCHANGE_CODE,
            CLOSE_INDEX 
        FROM EXCHANGE_DAILY 
        WHERE EXCHANGE_CODE = 'HOSE'
        FETCH FIRST 10 ROWS ONLY
        ''',
        index_col='TRADE_DATE'
    )
    assert isinstance(r, pd.DataFrame)
    assert r.index.names == ['TRADE_DATE']
    assert r.shape == (10, 2)