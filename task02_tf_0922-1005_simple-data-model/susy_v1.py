import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import pandas as pd
import time;

# add one more layer and return the output of this layer
def add_layer(inputs, in_size, out_size, activation_function=None):
    Weights = tf.Variable(tf.random_normal([in_size, out_size]))
    biases = tf.Variable(tf.zeros([1, out_size]) + 0.1)
    Wx_plus_b = tf.matmul(inputs, Weights) + biases
    if activation_function is None:
        outputs = Wx_plus_b
    else:
        outputs = activation_function(Wx_plus_b)
    return outputs

# define data
data = pd.read_csv("data/SUSY-100-0.csv")     #Read data
train_data = data.values.astype(np.float32)     #Transform into an array
x_data = train_data[:,1:]                       #Feature [1,8] column
y_data = train_data[:,0][:, np.newaxis]         #label

# Define placeholder for inputs to Neural Networks
xs = tf.placeholder(tf.float32, [None, 18], name="x_input")        #input：18
ys = tf.placeholder(tf.float32, [None, 1], name="y_input")        #output:1

# add hidden layer
l1 = add_layer(xs, 18, 128, activation_function=tf.sigmoid) 
l2 = add_layer(l1, 128, 8, activation_function=tf.nn.tanh) 
prediction = add_layer(l2, 8, 1, activation_function=None) 

# the error between prediction and real data
# 误差：对二者差的平方求和再取平均
loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys - prediction),reduction_indices=[1]))
train_step = tf.train.GradientDescentOptimizer(0.05).minimize(loss)

# Initialize variables
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)

#tf.train.SummaryWriter
writer = tf.summary.FileWriter('.')
writer.add_graph(tf.get_default_graph())

# training
train_loss = []
steps = []
since = time.time()
for t in range(4000):
    # training
    sess.run(train_step, feed_dict={xs: x_data, ys: y_data})

    if t % 50 == 0:
        # to see the step improvement
        loss_=sess.run(loss, feed_dict={xs: x_data, ys: y_data})
        train_loss.append(loss_)
        steps.append(t)
        # print('Step：{:03d} Loss：{:.3%}：'.format(t,loss_))
    
# visualize 
fig, axes = plt.subplots(figsize=(12, 8))
fig.suptitle('Training Metrics')
axes.set_ylabel("Loss", fontsize=14)
axes.set_xlabel("steps", fontsize=14)
axes.plot(train_loss)
plt.show()

#Spend time
time_elapsed = time.time() - since

# print('time cost:{:.0f}s'.format(time_elapsed))

#Save as training-summary.txt
with open("training-summary.txt","w") as f:
    f.write('Step：{:03d},time cost:{:.0f}s,Loss：{:.3%}：'.format(t,time_elapsed,loss_))