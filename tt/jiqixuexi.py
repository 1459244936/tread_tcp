# -*- coding:utf-8 -*-
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
#导入Mnist数据集
mnist=input_data.read_data_sets("MNIST_data",one_hot=True)
 
#数据集常数，输入层为28*28=784维的向量
INPUT_NODE=784
OUTPUT_NODE=10
 
#构建网络，x为网络输入，y_为训练数据的入口
x=tf.placeholder(tf.float32,shape=(None,INPUT_NODE))#batch_size不固定
y_=tf.placeholder(tf.float32,shape=(None,OUTPUT_NODE))#batch_size不固定
 
#输入层的权重w1和偏置b1
w1=tf.Variable(tf.random_normal([784,100],stddev=1))
b1=tf.Variable(tf.constant(0.1,shape=[100]))
 
#隐藏层的节点数量为100
#隐藏层的权重w2和偏置b2
w2=tf.Variable(tf.random_normal([100,10],stddev=1))
b2=tf.Variable(tf.constant(0.1,shape=[10]))
 
##线性模型，没有激活函数
#y1=tf.matmul(x,w1)+b1#输入层的输出
#y=tf.matmul(y1,w2)+b2#隐藏层的输出
 
#非线性模型
y1=tf.sigmoid(tf.matmul(x,w1)+b1)#输入层的输出
y=tf.sigmoid(tf.matmul(y1,w2)+b2)#隐藏层的输出
 
#设置正则化比重为0.0001
get_regularization= tf.contrib.layers.l2_regularizer(0.0001)
regularization=get_regularization(w1)+get_regularization(w2)
 
#使用交叉熵加softmax作为损失函数
loss=tf.nn.sparse_softmax_cross_entropy_with_logits(logits=y,labels=tf.argmax(y_,1))+regularization
 
#通过梯度下降算法优化器反向传播训练参数，参数学习率为0.001
train_step=tf.train.GradientDescentOptimizer(0.001).minimize(loss)
 
#correct_prediction为bool变量0或1表示是否预测正确
correct_prediction=tf.equal(tf.argmax(y,1),tf.argmax(y_,1))
#accuracy计算得出当前模型在验证数据集上的准确率
accuracy=tf.reduce_mean(tf.cast(correct_prediction,tf.float32))
 
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())#对所有的变量进行初始化
    #设置验证集
    validate_feed={x:mnist.validation.images,y_:mnist.validation.labels}
    test_feed={x:mnist.test.images,y_:mnist.test.labels}
 
    STEPS=200000 #总训练轮数
    BATCH_SIZE=100#每批训练数量batch_size
 
    #开始训练
    for i in range(STEPS):
        if(i%1000==0):
            vali_acc=sess.run(accuracy,feed_dict=validate_feed)#当前模型的准确率
            print('After %d steps accuracy is %g'%(i,vali_acc))
            #print(sess.run(w1))
        xs,ys=mnist.train.next_batch(BATCH_SIZE)#获取下一个batch的样本
        sess.run(train_step,feed_dict={x:xs,y_:ys})#训练优化
    test_acc=sess.run(accuracy,feed_dict=test_feed)#最终测试集上的准确率
    print("Finally accuracy is %g"%(test_acc))
 