class DB_updater:
    def __init__(self):
        """생성자: db연결및 딕셔너리생성"""

    def __del__(self):
        """소멸자 : db연결 해제"""
        self.conn.close()

    def update_stock_price(self):
        """주식 값 저장"""

    def update_prediction(self):
        """예측 값 저장"""
