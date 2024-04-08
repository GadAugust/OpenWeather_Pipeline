from util import get_engine, get_api_key
from extract import extract_data
from transform import transform_data
from load import load_data



def main():
    engine = get_engine()
    api_key = get_api_key()
    print(api_key)




    #extract the data
    weather_df = extract_data(file='gb.xlsx', api_key=api_key)
    print('Data Extracted Successfully')

    

    #transform the data
    df = transform_data(weather_df)
    print('Data Transformed Successfully')


    #load data to postgress
    load_data(df = df, engine=engine, table='weather')
    print('Data loaded Successfully')

if __name__== '__main__':
    main()
    print('Pipeline run successfully')




    