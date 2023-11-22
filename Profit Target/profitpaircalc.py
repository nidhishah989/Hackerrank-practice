#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'stockPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY stocksProfit
#  2. LONG_INTEGER target
#

def stockPairs(stocksProfit, target):
    # Write your code here
    
    stocksProfit.sort()
    count =0
    visited=set()

    
    for i,val in enumerate(stocksProfit):
        if val <= target:
            remain = target-val
            j=i+1
            while(j<len(stocksProfit) and stocksProfit[j]<=remain):
                if stocksProfit[j]==remain:
                    if (val,remain) not in visited and (remain,val) not in visited:
                        count +=1
                        visited.add((val,remain))
                        visited.add((remain,val))
                    break
                j +=1    
                
    return count                
                    

if __name__ == '__main__':
     
    stocks_profit_1 = [1, 3, 46, 1, 3, 9]
    target_1 = 47
    result_1 = stockPairs(stocks_profit_1, target_1)
    print(result_1)
    assert result_1 == 1, f"Expected 1, got {result_1}"

    stocks_profit_2 = [5, 7, 9, 13, 11, 6, 6, 3, 3]
    target_2 = 12
    result_2 = stockPairs(stocks_profit_2, target_2)
    print(result_2)
    assert result_2 == 3, f"Expected 3, got {result_2}"
     
