import backtrader as bt


class SimpleMovingAverageCrossoverStrategy(bt.Strategy):
    params = (('fast', 10), ('slow', 30))

    def __init__(self):
        self.fast_ma = bt.indicators.SimpleMovingAverage(self.data.close, period=self.params.fast)
        self.slow_ma = bt.indicators.SimpleMovingAverage(self.data.close, period=self.params.slow)

    def next(self):
        if self.fast_ma[0] > self.slow_ma[0] and not self.position:
            print(f'Compra: {self.data.datetime.datetime()}')
            self.buy()
        elif self.fast_ma[0] < self.slow_ma[0] and self.position:
            print(f'Venda: {self.data.datetime.datetime()}')
            self.sell()