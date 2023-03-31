from _datetime import datetime as dt
from time import sleep

import pandas as pd
import MetaTrader5 as mt5
from ..strategy.corner_strategy import check_corner

mt5.initialize(login=5765715, server="AMarkets-Demo", password="0BXzqSab")
symbol_list = {'EURUSD', 'XAUUSD', 'GBPUSD'}
timeframe = mt5.TIMEFRAME_M1
num_bars = 100


def check_all_symbole():
    for symbol in symbol_list:
        bars = mt5.copy_rates_from_pos(symbol, mt5.TIMEFRAME_M1, 0, num_bars)
        df = pd.DataFrame(bars)
        df['time'] = pd.to_datetime(df['time'], unit='s')
        check_corner(df, symbol)
        sleep(3)


def get_data_euro_m1():
    bars = mt5.copy_rates_from_pos('EURUSD', mt5.TIMEFRAME_M1, 0, num_bars)
    df = pd.DataFrame(bars)
    df['time'] = pd.to_datetime(df['time'], unit='s')
    check_corner(df, 'EURUSD')
    # print(df, "spaceEUR", dt.now())


def get_data_euro_m5():
    bars = mt5.copy_rates_from_pos('EURUSD', mt5.TIMEFRAME_M5, 0, num_bars)
    df = pd.DataFrame(bars)
    df['time'] = pd.to_datetime(df['time'], unit='s')
    check_corner(df, 'EURUSD')


def get_data_xau_m1():
    bars = mt5.copy_rates_from_pos('XAUUSD', mt5.TIMEFRAME_M1, 0, num_bars)
    df = pd.DataFrame(bars)
    df['time'] = pd.to_datetime(df['time'], unit='s')
    check_corner(df, 'XAUUSD')
    # print(df, "spaceXAU", dt.now())


def get_data_gbp_m1():
    bars = mt5.copy_rates_from_pos('GBPUSD', mt5.TIMEFRAME_M1, 0, num_bars)
    df = pd.DataFrame(bars)
    df['time'] = pd.to_datetime(df['time'], unit='s')
    check_corner(df, 'GBPUSD')


def get_data_gbp_m5():
    bars = mt5.copy_rates_from_pos('GBPUSD', mt5.TIMEFRAME_M5, 0, num_bars)
    df = pd.DataFrame(bars)
    df['time'] = pd.to_datetime(df['time'], unit='s')
    check_corner(df, 'GBPUSD')
