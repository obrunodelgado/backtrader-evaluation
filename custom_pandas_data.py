import backtrader as bt


class CustomPandasData(bt.feeds.PandasData):
    lines = ('close',)
    params = (
        ('open', 1),
        ('high', 2),
        ('low', 3),
        ('close', 4),
        ('volume', 5),
        ('datetime', 0),
    )
