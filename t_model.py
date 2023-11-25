import tensorflow as tf
import tensorflow_hub as hub
import tensorflow_text as text


def get_model(
    tfhub_handle_encoder = "https://www.kaggle.com/models/jeongukjae/distilbert/frameworks/TensorFlow2/variations/multi-cased-l-6-h-768-a-12/versions/1",
    tfhub_handle_preprocess = "https://www.kaggle.com/models/jeongukjae/distilbert/frameworks/TensorFlow2/variations/multi-cased-preprocess/versions/2"
):
    text_input = tf.keras.layers.Input(shape=(), dtype=tf.string, name='text')
    preprocessing_layer = hub.KerasLayer(tfhub_handle_preprocess, name='preprocessing')
    encoder_inputs = preprocessing_layer(text_input)
    encoder = hub.KerasLayer(tfhub_handle_encoder, trainable=True, name='BERT_encoder')
    outputs = encoder(encoder_inputs)
    net = outputs['pooled_output']
    net = tf.keras.layers.Dropout(0.1)(net)
    net = tf.keras.layers.Dense(256, activation=None)(net)
    net = tf.keras.layers.Dense(195, activation=None, name='classifier')(net)
    model = tf.keras.Model(text_input, net)

    model.compile(
        optimizer=tf.keras.optimizers.SGD(),
        loss=tf.keras.losses.CategoricalCrossentropy(from_logits=True),
        metrics=["accuracy"]#tf.keras.metrics.CategoricalCrossentropy(from_logits=True)
    )
    return model, preprocessing_layer