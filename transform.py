from util import adjust_date
import pandas as pd



def transform_data(weather_df):
    '''
    This function transforms the extracted weather data to convert time,
    from unix to utc and also drop some columns.

    parameters: a dataframe df
    Return value: A dataFrame
    Return Type: A pandas dataframe object
    '''
    #convert unix to  utc
    weather_df['reading date'] = weather_df.apply(adjust_date,axis=1)

    # drop columns
    clean_df =weather_df.drop(['latitude', 'longitude', 'unix_date', 'unix_timezone'], axis = 1)
    return clean_df