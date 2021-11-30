import pandas as pd
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense, LSTM, Dropout
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Flatten
from keras.layers import Dropout
from keras.layers import LSTM
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Flatten
from keras.layers import Dropout
from keras.layers.convolutional import Conv1D
from keras.layers.convolutional import MaxPooling1D
from keras import callbacks

def RNN(code, company, init=False):
    """RNN"""

    raw_df = pd.read_csv(f'./data/{code} {company}.csv')
    if init:
        raw_df = raw_df[0:-2]


    def MinMaxScaler(data):
        """최솟값, 최댓값 이용해 0~1 값으로 변환"""
        numerator = data - np.min(data, 0)
        denominator = np.max(data, 0) - np.min(data, 0)
        return numerator / (denominator + 1e-7)

    dfx = raw_df[['open', 'high', 'low', 'volume', 'close']]
    dfx = MinMaxScaler(dfx)
    dfy = dfx[['close']]
    x = dfx.values.tolist()
    y = dfy.values.tolist()

    data_x = []
    data_y = []
    window_size = 10
    for i in range(len(y) - window_size):
        _x = x[i: i + window_size]
        _y = y[i + window_size]
        data_x.append(_x)
        data_y.append(_y)

    # 훈련용 데이터셋
    train_size = int(len(data_y) * 0.7)
    train_x = np.array(data_x[0:train_size])
    train_y = np.array(data_y[0:train_size])

    # 테스트용 데이터셋
    test_size = len(data_y) - train_size
    test_x = np.array(data_x[train_size:len(data_x)])
    test_y = np.array(data_y[train_size:len(data_y)])

    model = Sequential()
    model.add(LSTM(units=10, activation='relu', return_sequences=True, input_shape=(window_size, 5)))
    model.add(Dropout(0.1))
    model.add(LSTM(units=10, activation='relu'))
    model.add(Dropout(0.1))
    model.add(Dense(units=1))
    model.summary()

    model.compile(optimizer='adam', loss='mean_squared_error')  # 최적화도구: adam
    model.fit(train_x, train_y, epochs=100, batch_size=30)  # epochs : 학습횟수, batch_size: 훈련데이터 갯수
    pred_y = model.predict(test_x)

    predict_price_tommorow = (raw_df.close.iloc[-1] * pred_y[-1] / dfy.close.iloc[-1])[0]
    predict_price_today = (raw_df.close.iloc[-2] * pred_y[-2] / dfy.close.iloc[-2])[0]

    percentage = round(((predict_price_tommorow/predict_price_today-1) * 100), 3)
    percentage = str(percentage)+'%'
    date = raw_df.date.iloc[-1]

    return (date, code, company, percentage)


def CNN(code, company, init = False):
    """CNN"""
    raw_df = pd.read_csv(f'./data/{code} {company}.csv')
    if init:
        raw_df = raw_df[0:-2]
    df = raw_df.drop(['volume'],1).drop(['adjc'],1)
    df = df.set_index("date")

    def normalize_data(dataset):
        cols = dataset.columns.tolist()
        col_name = [0] * len(cols)
        for i in range(len(cols)):
            col_name[i] = i
        dataset.columns = col_name
        dtypes = dataset.dtypes.tolist()
        minmax = list()
        for column in dataset:
            dataset = dataset.astype({column: 'float32'})
        for i in range(len(cols)):
            col_values = dataset[col_name[i]]
            value_min = min(col_values)
            value_max = max(col_values)
            minmax.append([value_min, value_max])
        for column in dataset:
            values = dataset[column].values
            for i in range(len(values)):
                values[i] = (values[i] - minmax[column][0]) / (minmax[column][1] - minmax[column][0])
            dataset[column] = values
        dataset[column] = values
        return dataset, minmax, cols

    dataset, minmax, col = normalize_data(df)
    print(df.values)
    values = dataset.values

    def split_sequences(sequence, n_steps):
        X, y = list(), list()
        for i in range(len(sequence)):
            end_ix = i + n_steps
            if end_ix > len(sequence) - 1:
                break
            seq_x, seq_y = sequence[i:end_ix], sequence[end_ix]
            X.append(seq_x)
            y.append(seq_y)
        return np.array(X), np.array(y)

    def data_setup(n_steps, n_seq, sequence):
        X, y = split_sequences(sequence, n_steps)
        n_features = X.shape[2]
        X = X.reshape((len(X), n_steps, n_features))
        new_y = []
        for term in y:
            new_term = term[-1]
            new_y.append(new_term)
        return X, np.array(new_y), n_features

    n_steps = 10
    n_seq = 10000
    rel_test_len = 0.1
    X, y, n_features = data_setup(n_steps, n_seq, values)
    X = X[:-1]
    y = y[1:]
    X_test, y_test = X[:int(len(X) * rel_test_len)], y[:int(len(X) * rel_test_len)]
    X_train, y_train = X[int(len(X) * rel_test_len):], y[int(len(X) * rel_test_len):]
    X.shape

    model = Sequential()
    model.add(LSTM(64, activation=None, input_shape=(10, 4), return_sequences=True))
    model.add(LSTM(32, activation=None, return_sequences=True))
    model.add(Flatten())
    model.add(Dense(100, activation=None))
    model.add(Dense(1, activation='sigmoid'))
    model.compile(loss='mse', optimizer='adam')
    model = Sequential()
    model.add(Conv1D(filters=128, kernel_size=3, activation='relu', input_shape=(10, 4)))
    model.add(Conv1D(filters=64, kernel_size=3, activation='relu'))
    model.add(MaxPooling1D(pool_size=2))
    model.add(Flatten())
    model.add(Dense(100, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))
    model.compile(loss='mse', optimizer='adam')

    epochs = 1000
    verbosity = 2
    h5 = 'network.h5'
    checkpoint = callbacks.ModelCheckpoint(h5,
                                           monitor='val_loss',
                                           verbose=0,
                                           save_best_only=True,
                                           save_weights_only=True,
                                           mode='auto',
                                           period=1)
    callback = [checkpoint]
    history = model.fit(X_train,
                        y_train,
                        epochs=epochs,
                        batch_size=len(X_train) // 4,
                        validation_data=(X_test, y_test),
                        verbose=verbosity,
                        callbacks=callback)
    pred_test = model.predict(X_test)


    predict_price_tommorow = (df[3][-1] * pred_test[-1] / y_test[-1])[0]
    predict_price_today = (df[3][-2]*pred_test[-2]/y_test[-2])[0]

    percentage = round(((predict_price_tommorow / predict_price_today - 1) * 100), 3)
    percentage = str(percentage) + '%'
    date = raw_df.date.iloc[-1]

    return (date, code, company, percentage)