# -*- coding: utf-8 -*-
# Contact: condadoslgpc@gmail.com
# @Author: Luis Condados
# @Date:   2022-02-07 21:15:40
# @Last Modified by:   Luis Condados
# @Last Modified time: 2022-02-07 21:15:52

import tensorflow as tf

def setup_gpu(gpu_id=0, allow_memory_growth=True):

    gpus = tf.config.list_physical_devices('GPU')
    if gpus:
        try:
            gpu = gpus[gpu_id] if gpu_id <= len(gpus) else gpus[0]
            if len(gpus) > 1:
                tf.config.experimental.set_visible_devices(gpus[gpu_id], 'GPU')
            
            if allow_memory_growth:
                tf.config.experimental.set_memory_growth(gpu, allow_memory_growth)

        except RuntimeError as e:
            return