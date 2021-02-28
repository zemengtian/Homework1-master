# Contains helper functions for your apps!
import os
from os import listdir, remove


# If the io following files are in the current directory, remove them!
# 1. 'currency_pair.txt'
# 2. 'currency_pair_history.csv'
# 3. 'trade_order.p'


def check_for_and_del_io_files():
    # Your code goes here.

    if ('currency_pair.txt' in os.listdir()) == 1:
        os.remove("currency_pair.txt")
    if ('currency_pair_history.csv' in os.listdir()) == 1:
        os.remove("currency_pair_history.csv")
    if ('trade_order.p' in os.listdir()) == 1:
        os.remove("trade_order.p")
    pass  # nothing gets returned by this function, so end it with 'pass'.
