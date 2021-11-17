#DB에서 예측값 불러오기, 주식값 불러오기


class user_DB:
    def __init__(self):
        """생성자 : db연결 및 딕셔너리 생성"""

    def __del__(self):
        """소멸자 : db 연결해제"""
        self.conn.close()

    def load_prediction(self):
        """db에서 예측값 불러오기"""

    def load_stock_price(self):
        """db에서 주식값 불러오기"""
        #return(주식값df)
