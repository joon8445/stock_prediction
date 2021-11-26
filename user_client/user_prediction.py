import pandas as pd

# DB에서 예측한 값 불러오기

def load_predict(code,company):
    stock = pd.read_csv(f'./../admin/data/{code} {company}.csv')
    predict = pd.read_csv(f'./../admin/data/{code}_{company}_pred.csv')
    real_price = stock.close.iloc[-1]
    real_price_date = stock.date.iloc[-1]

    predict_price_RNN = predict.percent.iloc[-1]


    prediction_1 = str(real_price_date) + ' 종가 : '+ str(real_price) + '\n다음 거래일 종가 증감률 예측 : '+str(predict_price_RNN)+'\n전일 거래 예측 종가 오차율 : '

    return prediction_1
