# -*- coding: utf-8 -*-
# @Author: Luis Condados
# @Date:   2022-02-07 20:38:24
# @Last Modified by:   Condados
# @Last Modified time: 2022-12-16 15:58:09

from pydantic import BaseModel
from typing import Optional
from typing import List

class RequestTemplate(BaseModel):
    sentence: str