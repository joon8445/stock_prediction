from admin_data_updater import data_updater
import os
import pandas as pd

if __name__ == '__main__':
    stock_list = {'005930': '삼성전자', '000660': 'SK하이닉스', '035420': 'NAVER', '035720': '카카오'}
    updater = data_updater()
    for code, company in stock_list.items():
        print(code, company)
        updater.update_stock_price(code, company)
        pred_file = f'./data/{code}_{company}_pred.csv'
        stock_file = f'./data/{code} {company}.csv'
        if os.path.exists(pred_file):
            predict = pd.read_csv(pred_file)
            stock = pd.read_csv(stock_file)
            if predict.date.iloc[-1] == stock.date.iloc[-1]:
                print('already predicted')
            else:
                updater.update_prediction(code, company)
        else:
            updater.init_prediction(code, company)
            updater.update_prediction(code, company)
