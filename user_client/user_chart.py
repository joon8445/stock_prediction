import pandas as pd
import mpl_finance
import matplotlib.ticker as ticker

# DB에서 주가 정보 불러오고 차트그리기
def draw_chart(self, code, company):
    """주식 차트 그리기"""
    stock = pd.read_csv(f'./../admin/data/{code} {company}.csv')
    stock = stock.iloc[-60:-1]

    ax = self.fig.add_subplot(1,1,1)
    ax.xaxis.set_major_locator(ticker.MaxNLocator(3))
    ax.plot(stock.date, stock.close, 'g', linewidth=0.5)

    mpl_finance.candlestick2_ohlc(ax, stock['open'], stock['high'], stock['low'], stock['close'], width=0.5,
                                  colorup='r', colordown='b')

