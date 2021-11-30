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

        date, code, company, pred_cnn = prediction.CNN(code, company)
        date, code, company, pred_rnn = prediction.RNN(code, company)
        pred = {'date': [date], 'RNN': [pred_rnn], 'CNN':[pred_cnn]}
        pred_data = pd.DataFrame(pred)
        file = f'./data/{code}_{company}_pred.csv'
        if not os.path.exists(file):
            pred_data.to_csv(file, index=False, mode='w', encoding='utf-8-sig')
        else:
            pred_data.to_csv(file, index=False, mode='a', encoding='utf-8-sig', header=False)

    def init_prediction(self, code, company):
        date, code, company, pred_rnn = prediction.RNN(code, company, True)
        date, code, company, pred_cnn = prediction.CNN(code, company, True)
        pred = {'date': [date], 'RNN': [pred_rnn], 'CNN':[pred_cnn]}
        pred_data = pd.DataFrame(pred)
        file = f'./data/{code}_{company}_pred.csv'
        if not os.path.exists(file):
            pred_data.to_csv(file, index=False, mode='w', encoding='utf-8-sig')
        else:
            pred_data.to_csv(file, index=False, mode='a', encoding='utf-8-sig', header=False)
