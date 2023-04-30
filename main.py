import backtrader as bt
import pandas as pd
from yahooquery import Ticker

from custom_pandas_data import CustomPandasData
from sma_strategy import SimpleMovingAverageCrossoverStrategy


def obter_dados_historicos(ticker: str, periodo: str, intervalo: str, inicio: str, fim: str) -> pd.DataFrame:
    df = Ticker(symbols=ticker).history(period=periodo, interval=intervalo, start=inicio, end=fim)
    df.reset_index(inplace=True)
    df = df.drop("symbol", axis=1)
    df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d', utc=True)
    return df


if __name__ == '__main__':
    df = obter_dados_historicos('BOVA11.SA', 'ytd', '1d', '2022-01-01', '2023-04-30')
    data = CustomPandasData(dataname=df)

    cerebro = bt.Cerebro()
    cerebro.addstrategy(SimpleMovingAverageCrossoverStrategy)
    cerebro.adddata(data)
    cerebro.broker.setcash(10000.0)
    results = cerebro.run()

    print(f'Valor final do portfólio: {results[0].broker.getvalue()}')
    cerebro.plot()
