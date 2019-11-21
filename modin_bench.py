# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 19:21:48 2019
https://ktr89.hateblo.jp/entry/2019/03/21/220741
@author: hfuji
"""

from benchmarker import Benchmarker
import numpy as np

from modin import pandas as mpd
import pandas as ppd
import dask.dataframe as ddf
import dask.multiprocessing

def run(row, col, loop=3):

    df_random = ppd.DataFrame(np.random.randn(row, col))
    df_random.to_csv("random.csv")

    with Benchmarker(loop) as bench:

        @bench(f'original pandas row:{row} col:{col}')
        def original_pandas_read(bm):
            ppd.read_csv('random.csv')


        @bench(f'modin pandas row:{row} col:{col}')
        def modin_read(bm):
            mpd.read_csv('random.csv')

        @bench(f'dask pandas row:{row} col:{col}')
        def dask_read(bm):
            df = ddf.read_csv('random.csv')
            df = df.compute()

if __name__ == "__main__":

    for r in [1, 10, 100,
        1_000, 10_000, 100_000,
        1_000_000, 10_000_000, 100_000_000]:
        run(row=r, col=273)
        