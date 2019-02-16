import numpy as np
import tensorflow as tf

coefficient = np.array([[1.],[-10.],[25.]])
# initializes w to 0
w = tf.Variable(0, dtype=tf.float32)
# control coefficient of quadratic func
#placeholder : value that you assign later
x = tf.placeholder(tf.float32, [3,1])
#cost = tf.add(tf.add(w**2, tf.multiply(-10.,w)),25)
#cost = w**2 - 10*w + 25
cost = x[0][0]*w**2 + x[1][0]*w + x[2][0]
#train as a learning algorithm uses GDO to minimize cost function
train = tf.train.GradientDescentOptimizer(0.01).minimize(cost)

init = tf.global_variables_initializer()
session = tf.Session()
session.run(init)
print(session.run(w))
#should see a 0.0
#session.run(train)
session.run(train, feed_dict={x:coefficient})
print(session.run(w))
#should see a 0.1

for i in range(1000):
    session.run(train, feed_dict={x:coefficient}))
print(session.run(w))
#should see a 4.99999
