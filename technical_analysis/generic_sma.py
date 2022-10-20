from exchanges import mt5_interaction as mt5
import pandas

# Function to calculate the average of n number of entries
def calculate_sma(symbol, sma_size, timeframe, exchange):
    # Retrieve the raw data
    if exchange == "mt5":
        raw_data = mt5.query_historic_data(symbol=symbol, timeframe=timeframe, number_of_candles=sma_size)
    # Add other exchanges as they become available

    # Convert raw_data into a dataframe
    dataframe = pandas.DataFrame(raw_data)
    # Get the average of the close price
    sma = dataframe['close'].mean()
    return sma


# Function to calculate the 50-day SMA
def calculate_50_day_sma(symbol, exchange):
    return calculate_sma(symbol=symbol, sma_size=50, timeframe="D1", exchange=exchange)


# Function to calculate the 200-day SMA
def calculate_200_day_sma(symbol, exchange):
    return calculate_sma(symbol=symbol, sma_size=200, timeframe="D1", exchange=exchange)
