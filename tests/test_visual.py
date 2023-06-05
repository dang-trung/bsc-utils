import pandas as pd

from bsc_utils.database import Database, query
from bsc_utils.visual import plotly


def test_plotly():
    quotes = query(
        Database.ORACLE,
        '''
        SELECT 
            TRADE_DATE, 
            CLOSE_INDEX,
            AVG(CLOSE_INDEX) OVER (ORDER BY TRADE_DATE ASC RANGE BETWEEN 29 PRECEDING AND CURRENT ROW) AS MA30D,
            ROUND(TOTAL_VALUE / 1000000000) AS TOTAL_VALUE,
            ADVANCES / DECLINES AS AD
        FROM EXCHANGE_DAILY 
        WHERE 
            EXCHANGE_CODE = 'HOSE'
            AND DECLINES > 0
        ORDER BY TRADE_DATE ASC
        ''',
        index_col='TRADE_DATE'
    )
    trading_days = [d.to_pydatetime() for d in quotes.index]
    all_days = [
        d.to_pydatetime() for d in
        pd.date_range(start=trading_days[0], end=trading_days[-1], freq='D')
    ]
    non_trading_days = [d for d in all_days if d not in trading_days]
    subplots = {
        'VN-Index':
            [
                {
                    'type':
                        'scatter',
                    'x':
                        quotes.index,
                    'y':
                        quotes['CLOSE_INDEX'],
                    'showlegend':
                        False,
                    'name':
                        'VN-Index',
                    'range':
                        [
                            quotes['CLOSE_INDEX'].min() * .5,
                            quotes['CLOSE_INDEX'].max() * 1.1
                        ],
                },
                {
                    'type': 'scatter',
                    'x': quotes.index,
                    'y': quotes['MA30D'],
                    'showlegend': False,
                    'name': 'MA20D',
                },
                {
                    'type': 'bar',
                    'x': quotes.index,
                    'y': quotes['TOTAL_VALUE'],
                    'showlegend': False,
                    'name': 'Volume (B VND)',
                    'secondary_y': True,
                    'range': [0, quotes['TOTAL_VALUE'].max() * 3],
                    'showticklabels': False
                }
            ],
        'Advances/Declines':
            [
                {
                    'type': 'scatter',
                    'x': quotes.index,
                    'y': quotes['AD'],
                    'showlegend': False,
                    'name': 'AD',
                    'hovertemplate': '%{y:,.2f}',
                },
            ]
    }

    fig = plotly(subplots)
    fig.update_xaxes(rangebreaks=[dict(values=non_trading_days)])
    fig.show()