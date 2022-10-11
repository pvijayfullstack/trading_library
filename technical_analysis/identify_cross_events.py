from exchanges import mt5_interaction as mt5
import pandas


# Function to identify if a Death Cross or Golden Cross has occurred
def calculate_a_cross(symbol, timeframe, exchange):
    pandas.set_option("display.max_columns", None)
    pandas.set_option("display.max_rows", None)
    # Retreive the raw data
    if exchange == "mt5":
        sma_50_raw = mt5.query_historic_data(symbol=symbol, timeframe=timeframe, number_of_candles=51)
        sma_200_raw = mt5.query_historic_data(symbol=symbol, timeframe=timeframe, number_of_candles=201)

    # Convert into Dataframe
    sma_50_dataframe = pandas.DataFrame(sma_50_raw)
    sma_200_dataframe = pandas.DataFrame(sma_200_raw)

    # Extract the four averages
    # Current 50 SMA
    sma_50_current = sma_50_dataframe['close'].tail(50).mean()
    # Previous 50 SMA
    sma_50_previous = sma_50_dataframe['close'].head(50).mean()
    # Current 200 SMA
    sma_200_current = sma_200_dataframe['close'].tail(200).mean()
    # Previous 200 SMA
    sma_200_previous = sma_200_dataframe['close'].head(200).mean()

    # Compare the results
    if sma_50_previous > sma_200_previous and sma_50_current < sma_200_current:
        return "DeathCross"
    elif sma_50_previous < sma_200_previous and sma_50_current > sma_200_current:
        return "GoldenCross"
    else:
        return "NoCross"


# Function to calculate Death Cross and Golden Cross for daily trading
def calculate_day_cross(symbol, exchange):
    return calculate_a_cross(symbol=symbol, timeframe="D1", exchange=exchange)
