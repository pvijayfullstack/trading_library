import json
import os
from exchanges import mt5_interaction as mt5_interface
from technical_analysis import identify_cross_events
from technical_analysis import generic_sma
import time


# Function to import settings from settings.json
def get_project_settings(importFilepath):
    # Test the filepath to sure it exists
    if os.path.exists(importFilepath):
        # Open the file
        f = open(importFilepath, "r")
        # Get the information from file
        project_settings = json.load(f)
        # Close the file
        f.close()
        # Return project settings to program
        return project_settings
    else:
        return ImportError


# Main function
if __name__ == '__main__':
    # Set up the import filepath
    import_filepath = "C:/Users/james/PycharmProjects/trading_library/settings.json"
    # Import project settings
    project_settings = get_project_settings(import_filepath)
    # Start MT5
    mt5_interface.start_mt5(project_settings["username"], project_settings["password"], project_settings["server"],
                            project_settings["mt5Pathway"])
    # Initialize symbols
    mt5_interface.initialize_symbols(project_settings["symbols"])
    # Calculate a cross event
    cross_event = identify_cross_events.calculate_day_cross(symbol=project_settings["symbols"][0], exchange="mt5")
    print(cross_event)


