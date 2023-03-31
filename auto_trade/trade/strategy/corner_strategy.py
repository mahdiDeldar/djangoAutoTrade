import datetime

from MetaTrader5 import SymbolInfo
import MetaTrader5 as mt5
from ..order.Order import send_buy_order, send_sell_order

mt5.initialize()


def split_last(close, n):
    m = n + 1
    if len(str(close)) > n and str(close)[-m] == '.':
        return float(str(close)[:-1])
    else:
        return close


def pip_calculate(close2, close1, symbol):
    symbol_info: SymbolInfo = mt5.symbol_info(symbol)
    currency_digits = symbol_info.digits
    close2_new = split_last(round(close2, currency_digits), currency_digits)
    close1_new = split_last(round(close1, currency_digits), currency_digits)
    print(close2, " ", close2_new, " ", close1, " ", close1_new, " ", symbol, "\n")
    short_f = close2_new - close1_new
    if currency_digits == 5:
        return round(short_f * 10000)
    if currency_digits == 4:
        return round(short_f * 1000)
    if currency_digits == 3:
        return round(short_f * 100)
    else:
        return round(short_f * 10)


trade_done_list = []


def check_corner(df, symbol):
    last_frame = df.shape[0] - 1
    if df['close'][last_frame - 1] < df['open'][last_frame - 1] and df['close'][last_frame - 2] > df['open'][
        last_frame - 2] and df['close'][last_frame - 3] < df['open'][last_frame - 3] and pip_calculate(
        df['close'][last_frame - 2], df['close'][last_frame - 1], symbol) > 2:
        j_loop = last_frame - 4
        for j in range(j_loop, 2, -1):
            if df['close'][j] > df['open'][j] and df['close'][j] > df['close'][last_frame - 2]:
                k_loop = j - 1
                for k in range(k_loop, 2, -1):
                    if df['close'][k] < df['open'][k]:
                        final_loop = k - 1
                        for f in range(final_loop, 2, -1):
                            if df['close'][f] > df['open'][f] and df['close'][f] < df['close'][last_frame - 2]:
                                diff = df['close'][last_frame - 1] - (
                                        (df['close'][last_frame - 2] - df['close'][last_frame - 1]) * 2)
                                # if (df['close'][f]) < diff:
                                trade_done_list.append(df['time'][last_frame])
                                send_sell_order(symbol, df['high'][last_frame - 2], diff)
                                print("sell", df['time'][last_frame], " ", df['time'][j], " ", df['time'][k], " ",
                                      df['time'][f], " ", pip_calculate(
                                        df['close'][last_frame - 2], df['close'][last_frame - 1], symbol))
                                break
                        break
                break
    elif df['close'][last_frame - 1] > df['open'][last_frame - 1] and df['close'][last_frame - 2] < df['open'][
        last_frame - 2] and df['close'][last_frame - 3] > \
            df['open'][last_frame - 3] and pip_calculate(df['close'][last_frame - 1], df['close'][last_frame - 2],
                                                         symbol) > 2:
        j_loop = last_frame - 4
        for j in range(j_loop, 2, -1):
            if df['close'][j] < df['open'][j] and df['close'][j] < df['close'][last_frame - 2]:
                k_loop = j - 1
                for k in range(k_loop, 2, -1):
                    if df['close'][k] > df['open'][k]:
                        final_loop = k - 1
                        for f in range(final_loop, 2, -1):
                            if df['close'][f] < df['open'][f] and df['close'][f] > df['close'][last_frame - 2]:
                                diff = df['close'][last_frame - 1] + (
                                        (df['close'][last_frame - 1] - df['close'][last_frame - 2]) * 2)
                                # if (df['close'][f]) > diff:
                                send_buy_order(symbol, df['low'][last_frame - 2], diff)
                                print("buy", df['time'][last_frame], " ", df['time'][j], " ", df['time'][k], " ",
                                      df['time'][f], " ",
                                      pip_calculate(df['close'][last_frame - 1], df['close'][last_frame - 2],
                                                    symbol))
                                break
                        break
                break
    else:
        print("candle is no ok", symbol, "\n")
