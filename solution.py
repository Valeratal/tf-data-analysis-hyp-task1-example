import pandas as pd
import numpy as np


chat_id = 252926140 # Ваш chat ID, не меняйте название переменной

import scipy.stats as stats

def solution(x_success: int, x_cnt: int, y_success: int, y_cnt: int) -> bool:
    # Calculate the expected number of successful calls in the test sample under the null hypothesis
    p = x_cnt / y_cnt
    expected_success = y_cnt * p

    # Calculate the p-value for the hypothesis test
    p_value = 1 - stats.binom.cdf(x_success - 1, y_cnt, p)

    # Compare the p-value to the significance level and return the decision
    return p_value < 0.06 and x_success > expected_success
