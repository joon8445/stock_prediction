import pandas as pd
from stoct_price import read_yahoo
import prediction
import os

class data_updater:
    def update_stock_price(self, code, company):
        """주식 값 저장"""
        read_yahoo(code, company).to_csv(f'./data/{code} {company}.csv', index=False)

    def update_prediction(self, code, company):
        """예측 값 저장"""
        date, code, company, percentage = prediction.RNN(code, company)
        pred = {'date': [date], 'percent': [percentage]}
        pred_data = pd.DataFrame(pred)
        file = f'./data/{code}_{company}_pred.csv'
        if not os.path.exists(file):
            pred_data.to_csv(file, index=False, mode='w', encoding='utf-8-sig')
        else:
            pred_data.to_csv(file, index=False, mode='a', encoding='utf-8-sig', header=False)
