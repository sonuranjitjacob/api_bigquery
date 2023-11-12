import pandas as pd

def process_weatherapi_history_data(data):
    """
    Process and format weather data into a DataFrame.

    Parameters:
    - data (dict): Raw weather data containing forecast information.

    Returns:
    - pandas.DataFrame: A DataFrame containing processed weather data with columns for each hour's
      weather conditions.

    """
    #take data
    
    df = pd.DataFrame(data['forecast']['forecastday'][0]['hour'])
    df['condition'] = df['condition'].astype(str)
    return df
