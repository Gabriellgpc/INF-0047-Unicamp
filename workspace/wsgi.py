# -*- coding: utf-8 -*-
# Contact: condadoslgpc@gmail.com
# @Author: Luis Condados
# @Date:   2022-02-07 20:38:12
# @Last Modified by:   Luis Condados
# @Last Modified time: 2022-02-07 22:20:58

import predictor as myapp

# This is just a simple wrapper for gunicorn to find your app.
# If you want to change the algorithm file, simply change "predictor" above to the
# new file.

app = myapp.app