from bsc_utils.database import Database, connect, query


def test_connect():
    connect(database=Database.MSSQL)
    connect(database=Database.ORACLE)
    connect(database=Database.SQLITE)


def test_query_mssql():
    r = query(Database.MSSQL, 'SELECT TOP 1 SYMBOL FROM STOCK_SYMBOLS')
    assert isinstance(r, list)
    assert isinstance(r[0], dict)


def test_query_oracle():
    r = query(
        Database.ORACLE,
        'SELECT SECURITY_CODE FROM SECURITIES FETCH FIRST 1 ROWS ONLY'
    )
    assert isinstance(r, list)
    assert isinstance(r[0], dict)


def test_query_sqlite():
    r = query(
        Database.SQLITE,
        'SELECT SYMBOL FROM SYMBOL_TYPES WHERE SYMBOL_TYPE = "CKCS" LIMIT 1'
    )
    assert isinstance(r, list)
    assert isinstance(r[0], dict)