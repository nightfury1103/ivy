# global
from typing import Union

import tensorflow as tf

# local
from ivy.functional.backends.tensorflow import ivy_dtype_dict


def is_native_dtype(dtype_in: Union[tf.DType, str], /) -> bool:
    return dtype_in in ivy_dtype_dict
