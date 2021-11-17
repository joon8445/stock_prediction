# DB에서 예측한 값 불러오기

def predict():


    fake_real_price = 110000
    fake_predict_price_1 = 113000


    real_price = fake_real_price
    predict_price_1 = fake_predict_price_1

    prediction_1 = '2021. 11. 03. Data 기준 11.4일 예측가 : ' + str(predict_price_1) + '\n전일 거래 예측 종가 오차율 : '
    prediction_1 += "{:.2f}".format((1 - real_price / predict_price_1) * 100)
    predict_price_2 = 114000
    prediction_2 = '2021. 11. 03. Data 기준 11.4일 예측가 : ' + str(predict_price_1) + '\n전일 거래 예측 종가 오차율 : '
    prediction_2 += "{:.2f}".format((1 - real_price / predict_price_2) * 100)

def load_predict(stock_name):
    #db에서 #db에서 예측값 불러오기
    predict_price = 0

    return predict_price