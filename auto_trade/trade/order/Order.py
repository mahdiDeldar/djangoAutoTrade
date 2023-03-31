import MetaTrader5 as mt5
from MetaTrader5 import OrderSendResult, TradePosition, SymbolInfo
from time import sleep

# symbol_info: SymbolInfo = mt5.symbol_info('EURUSD')
mt5.initialize()


def send_buy_order(symbol, stop_loss, take_profit):
    request_buy = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "type": mt5.ORDER_TYPE_BUY,
        "price": mt5.symbol_info_tick(symbol).ask,
        "sl": stop_loss,
        "tp": take_profit,
        "volume": 0.1,
        "comment": 'Test_code',
        "type_filling": mt5.ORDER_FILLING_IOC
    }
    order_buy_send: OrderSendResult = mt5.order_send(request_buy)
    print(order_buy_send.order)
    return order_buy_send


def send_sell_order(symbol, stop_loss, take_profit):
    request_sell = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "type": mt5.ORDER_TYPE_SELL,
        "price": mt5.symbol_info_tick(symbol).bid,
        "sl": stop_loss,
        "tp": take_profit,
        "volume": 0.1,
        "comment": 'Test_code',
        "type_filling": mt5.ORDER_FILLING_IOC
    }
    order_sell_send: OrderSendResult = mt5.order_send(request_sell)
    print(order_sell_send.order)
    return order_sell_send

# sleep(5)
# selected_position: TradePosition = mt5.positions_get(ticket=orderSend.order)
# print(selected_position)
# mt5.Close(symbol='EURUSD', ticket=orderSend.order)


# --------------------------------------------------------------------
# close_action = mt5.ORDER_TYPE_BUY
# close_symbol = selected_position.symbol
# price = mt5.symbol_info(selected_position.symbol).ask
#
# if selected_position.type == 0:
#     close_action = mt5.ORDER_TYPE_SELL
#     price = mt5.symbol_info(selected_position.symbol).bid
# request_close = {
#     "action": mt5.TRADE_ACTION_DEAL,
#     "symbol": close_symbol,
#     "type": close_action,
#     "price": price,
#     "volume": selected_position.volume,
#     "comment": 'Test_code',
#     "type_filling": mt5.ORDER_FILLING_IOC
# }
# orderSend: OrderSendResult = mt5.order_send(request_close)
