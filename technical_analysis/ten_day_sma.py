import generic_sma


# Function to calculate a 10-day SMA
def calc_10_day_sma(symbol, exchange):
    return generic_sma.calculate_sma(symbol=symbol, timeframe="D1", sma_size=10, exchange=exchange)