from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()

sec = pdr.get_data_yahoo('005930.KS', start = '2018-05-04') #kospi = XXXXXX.KS
msft = pdr.get_data_yahoo('MSFT', start='2018-05-04') #kosdaq = symbol

tmp_msft = msft.drop(columns='Volume')
tmp_msft.tail()

import matplotlib.pyplot as plt

#plot(x, y, 마커 형태,[,label='Label'])
plt.plot(sec.index, sec.Close, 'b', label='Sansung Electronics') # x = dateindex, y = Close,
plt.plot(msft.index, msft.Close, 'r--', label='Microsoft')
plt.legend(loc='best')
plt.show() #둘의 단위가 달라서 마이크로 소프트가 상대적으로 너무 작아 제대로 나오지 않음

# sec_dpc = (sec['Close']/sec['Close'].shift(1)-1)*100 #일간 변동률
#
# plt.hist(sec_dpc, bins=18) #일간 변동률 18개 구간으로 빈도수
# plt.grid(True)
#
# # sec_dpc_cs = sec_dpc.cumsum()
# #
# # # msft_dpc = (msft['Close']/msft['Close'].shift(1) -1) * 100
# # # msft_dpc.iloc[0]=0
# # # msft_dpc_cs = msft_dpc.cumsum()
# # #
# # # plt.plot(sec.index, sec_dpc_cs, 'b', label='Samsung Electronics')
# # # plt.plot(msft.index, msft_dpc_cs, 'r--', label='Microsoft')
# # # plt.ylabel('Change %')
# # # plt.grid(True)
# # # plt.legend(loc='best')
# # # plt.show()