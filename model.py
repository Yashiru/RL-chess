import tensorflow as tf

class RlModel(tf.keras.Model):
    def __init__(self):
        super(RlModel, self).__init__()
        
        self.model = tf.keras.models.Sequential()
        self.model.add(tf.keras.layers.Flatten(input_shape=[8]))

        self.model.add(tf.keras.layers.Dense(1024, activation="relu"))
        self.model.add(tf.keras.layers.Dense(2048, activation="relu"))
        self.model.add(tf.keras.layers.Dense(4096, activation="softmax"))
        # self.optimizer = tf.train.adam(0.01)


        
    def predict(self, env):
        model_output = self.model.predict(env)[0]
        return model_output

        