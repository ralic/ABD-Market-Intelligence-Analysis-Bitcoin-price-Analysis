import numpy as np

import tensorflow as tf

from data_analysis_s import data_pre
import sys
sys.path.insert(0,'/home/lpy/tflearn/')
import tflearn


train_data,train_label = data_pre('train')
test_data,test_label = data_pre('test')
print train_data.shape
print test_data.shape
days=35

net = tflearn.input_data(shape=[None, days, 22])
net = tflearn.lstm(net, 40, return_seq=False)#,dropout=0.8)
net = tflearn.dropout(net, 0.8)

#net = tflearn.lstm(net, 512)#,dropout=0.8)
#net = tflearn.dropout(net, 0.8)

net = tflearn.fully_connected(net, 1, activation='linear')
net = tflearn.regression(net, optimizer='rmsprop', loss='mean_square',metric='R2', name="target")

model = tflearn.DNN(net, tensorboard_verbose=0,tensorboard_dir='log_s/',checkpoint_path='model_s/')
model.load("model_s/-85963")
model.fit(train_data, train_label, n_epoch=10000,run_id='lstm',snapshot_epoch=True,validation_set=(test_data,test_label), show_metric=True, batch_size=20)
model.save("model/bitcoin_lstm_s.tfl")

   # print model.predict(train_data),train_label
   # print mean_squared_error(model.predict(train_data), train_label)
