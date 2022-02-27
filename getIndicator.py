from tradingview_ta import TA_Handler, Interval, Exchange

ethereum = TA_Handler(
    symbol="ETHUSD",
    screener="crypto",
    exchange="BINANCE",
    interval=Interval.INTERVAL_4_HOURS,
)

