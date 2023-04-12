import numpy as np
from scipy.stats import cramervonmises_2samp



chat_id = 263008738 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    is_homogeneous = False
    alpha = 0.08
    result = cramervonmises_2samp(x, y)
    p_value = result.pvalue
    # p_value = result.significance_level
    if p_value < alpha:
        is_homogeneous = True
    return is_homogeneous
