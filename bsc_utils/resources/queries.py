class ORACLE:
    trading_days_ago = {
        'EXCHANGE':
            '''
            SELECT MAX(TRADE_DATE) AS TRADE_DATE
            FROM (
            SELECT TRADE_DATE
            FROM EXCHANGE_DAILY
            WHERE EXCHANGE_CODE = :ec
            ORDER BY TRADE_DATE DESC
            )
            WHERE ROWNUM = :rn
            ''',
        'SECURITY':
            '''
            SELECT MAX(TRADE_DATE) AS TRADE_DATE
            FROM (
            SELECT TRADE_DATE
            FROM SECURITY_DAILY
            WHERE SECURITY_CODE = :ec
            ORDER BY TRADE_DATE DESC
            )
            WHERE ROWNUM = :rn
            '''
    }
