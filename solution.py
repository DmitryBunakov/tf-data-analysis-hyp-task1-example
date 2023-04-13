import pandas as pd
import numpy as np
from scipy.stats import norm
from statsmodels.stats.proportion import proportions_ztest

chat_id = 378114682 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    
    alpha = 0.07
    
    count = np.array([x_success, y_success])
    nobs = np.array([x_cnt, y_cnt])
    zstat, p_value = proportions_ztest(count=count, nobs=nobs, alternative='smaller')
    return p_value < alpha
