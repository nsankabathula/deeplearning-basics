import tensorflow as tf;

# Model
weight = tf.Variable([.1], tf.float32);
bias = tf.Variable([-.1], tf.float32);

#Input
input = tf.placeholder(tf.float32);

#Predected Output
output_model = weight * input + bias;

#Actual Output
actual_output = tf.placeholder(tf.float32);

#Loss
squared_delta = tf.square(output_model - actual_output);
loss = tf.reduce_sum(squared_delta);

#Optimize

optimizer = tf.train.GradientDescentOptimizer(0.01);
train = optimizer.minimize(loss);

init = tf.global_variables_initializer();

with tf.Session() as sess:
    File_Writer = tf.summary.FileWriter('C:\\Users\\nsankabathula\\PycharmProjects\\Basics\\graph', sess.graph);
    sess.run(init);
    #print(sess.run(loss,{input:[1,2,3,4], actual_output:[0,-1,-2,-3]}));
    for i in range (500):
        sess.run(train, {input: [1, 2, 3, 4], actual_output: [0, -1, -2, -3]});
        print (i, sess.run([weight, bias]));

    #print(sess.run([Weight, bias]));


