from admin_data_updater import data_updater

if __name__ == '__main__':
    stock_list = {'005930': '삼성전자', '000660': 'SK하이닉스', '035420': 'NAVER', '035720': '카카오'}
    updater = data_updater()
    for code, company in stock_list.items():
        print(code, company)
        updater.update_stock_price(code, company)
        updater.update_prediction(code, company)

"""run"""
