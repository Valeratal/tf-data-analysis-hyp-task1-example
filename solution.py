import pandas as pd
import numpy as np


chat_id = 252926140 # Ваш chat ID, не меняйте название переменной


import scipy.stats as stats

def solution(x_success: int, x_cnt: int, y_success: int, y_cnt: int) -> bool:
  p1 = x_success / x_cnt
  p2 = y_success / y_cnt
  p = (x_success + y_success) / (x_cnt + y_cnt)
  se = np.sqrt(p * (1 - p) * (1/x_cnt + 1/y_cnt))
  z = (p2 - p1) / se
  if z > stats.norm.ppf(1 - 0.06/2):
    return True
  else:
    return False
