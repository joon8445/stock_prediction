import pandas as pd
from datetime import datetime

class data_updater:
    def update_stock_price(self, code, company):
        """주식 값 저장"""
        self.read_yahoo(code, company).to_csv(f'./data/{code} {company}.csv', index=False)

    def read_yahoo(self, code, company):
        """Yahoo Finance에서 주식 시세를 읽어서 데이터프레임으로 반환"""
        try:
            url = f'https://query1.finance.yahoo.com/v7/finance/download/%s?period1=0&period2=1000000000000000000&interval=1d&events=history&includeAdjustedClose=true' % (
                        code + '.KS')
            df = pd.read_csv(url)
            tmnow = datetime.now().strftime('%Y-%m-%d %H:%M')
            print('[{}] {} ({}) : downloading...'.format(tmnow, company, code), end="\r")
            df = df.rename(columns={'Date': 'date', 'Open': 'open', 'High': 'high', 'Low': 'low',
                                    'Close': 'close', 'Adj Close': 'adjc', 'Volume': 'volume'})
            df = df.dropna()
            df[['open', 'high', 'low', 'close', 'adjc', 'volume']] = df[
                ['open', 'high', 'low', 'close', 'adjc', 'volume']].astype(int)
        except Exception as e:
            print('Exception occured', str(e))
            return None
        return df
    def update_prediction(self):
        """예측 값 저장"""

