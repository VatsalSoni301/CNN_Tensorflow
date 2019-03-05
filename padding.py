import tensorflow as tf

t = tf.constant([[1, 2, 3], [4, 5, 6]])
paddings = tf.constant([[1, 1,], [2, 2]])

# each list in a padding corresponds to each dimension
# eg: [1,1] corresponds to row and it adds on top of data and 1 row on bottom of data.
# eg: [2,2] corresponds to column it adds 2 column before data and 2 columns  after data.
# hint change padding value and see output :)

with tf.Session() as sess:
	# sess.run(tf.global_variables_initializer())
	print(sess.run(t))
	print(sess.run(paddings))
	t=tf.pad(t, paddings, "CONSTANT")
	print(sess.run(t))