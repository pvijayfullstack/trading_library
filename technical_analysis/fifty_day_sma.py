import generic_sma


# Function to calculate a 50-day SMA
def calc_50_day_sma(symbol, exchange):
    return generic_sma.calculate_sma(symbol=symbol, timeframe="D1", sma_size=50, exchange=exchange)