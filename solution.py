import pandas as pd
import numpy as np
from scipy.stats import ks_2samp

chat_id = 263008738 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    is_homogeneous = True
    alpha = 0.08
    statistic, p_value = ks_2samp(x, y)
    if p_value < alpha:
        is_homogeneous = False
    return is_homogeneous
