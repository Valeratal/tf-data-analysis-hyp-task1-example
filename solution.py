import pandas as pd
import numpy as np


chat_id = 252926140 # Ваш chat ID, не меняйте название переменной

import scipy.stats as stats

import scipy.stats as st

def solution(x_success: int, x_cnt: int, y_success: int, y_cnt: int) -> bool:
  p_control = x_success / x_cnt
  p_test = y_success / y_cnt
  p_pool = (x_success + y_success) / (x_cnt + y_cnt)
  se = np.sqrt(p_pool * (1 - p_pool) * (1/x_cnt + 1/y_cnt))
  z_score = (p_test - p_control) / se
  p_value = st.norm.sf(abs(z_score))
  return p_value < 0.06
