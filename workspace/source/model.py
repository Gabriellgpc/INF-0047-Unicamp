# -*- coding: utf-8 -*-
# @Author: Luis Condados
# @Date:   2022-02-07 20:39:25
# @Last Modified by:   Condados
# @Last Modified time: 2022-12-16 15:56:49

import os

import numpy as np
import tensorflow as tf
import tensorflow_text as text  # Registers the ops.

prefix = "/opt/program"
assets = os.path.join(prefix, "assets")

# A singleton for holding the model. This simply loads the model and holds it.
# It has a predict function that does a prediction based on the model and the input data.
class ScoringService():
    model = None # Where we keep the model when it's loaded
    processor = None

    @classmethod
    def get_model(cls):
        """Get the model object for this instance, loading it if it's not already loaded."""
        if cls.model is None or cls.processor is None:
            # Try to set up GPU
            # setup_gpu(0)

            saved_model_path = os.path.join(assets, 'saved_model')
            cls.model = tf.saved_model.load(saved_model_path)

            saved_preprocessor_path = os.path.join(assets, 'saved_preprocessor')
            cls.preprocessor = tf.saved_model.load(saved_preprocessor_path)
        return cls.model, cls.preprocessor

    @classmethod
    def predict(cls, address: str, location: str):
        # Get model
        model, preprocessor = cls.get_model()

        # Do the preprocessing
        text_preprocessed = preprocessor([np.array([address]), np.array([location])])
        model_output = model(text_preprocessed)

        # Run the inference
        score = tf.sigmoid(model_output).numpy().reshape(-1)[-1].astype(np.float64)

        return score