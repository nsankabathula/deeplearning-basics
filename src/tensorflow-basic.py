
import tensorflow as tf;
node1 = tf.constant(4.0);
node2 = tf.constant(-10.0);
node = node1 * node2;
sess = tf.Session();
File_Writer = tf.summary.FileWriter('C:\\Users\\nsankabathula\\PycharmProjects\\Basics\\graph', sess.graph);
#with tf.Session() as sess:
output = sess.run(node);
print (output);
sess.close();

