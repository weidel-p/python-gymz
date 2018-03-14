# -*- coding: utf-8 -*-

import numpy as np


def to_message(low, high, value):
    assert(np.shape(low) == np.shape(high) == np.shape(value))
    try:
        return [{'min': float(low[i]), 'max': float(high[i]), 'value': float(value[i])} for i in range(len(low))]
    except TypeError:
        return [{'min': float(low), 'max': float(high), 'value': float(value)}]
