import pandas as pd

# DB에서 예측한 값 불러오기

def load_predict(code,company):
    try:
        stock = pd.read_csv(f'./../admin/data/{code} {company}.csv')
        predict = pd.read_csv(f'./../admin/data/{code}_{company}_pred.csv')
        real_price = stock.close.iloc[-1]
        predict_date = predict.date.iloc[-1]

        predict_price_RNN = predict.percent.iloc[-1]


        prediction_1 = str(predict_date) + ' 종가 : '+ str(real_price) + '\n다음 거래일 종가 증감률 예측 : '+str(predict_price_RNN)

        if len(predict) > 1:
            predict_price_RNN_1 = predict.percent.iloc[-2]
            real_price_1 = stock.close.iloc[-2]
            real_price_percent = round((real_price_1 / real_price - 1) * 100, 3)
            prediction_1 += '\n이전 거래일 종가 증감률 예측 : ' + str(predict_price_RNN_1)
            prediction_1 += '\n이전 거래일 실제 종가 증감률 : ' + str(real_price_percent)+'%'



        return prediction_1
    except:
        return 'prediction error'
