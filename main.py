import pandas as pd
import numpy as np

cwl_data = pd.read_csv (r'C:\Users\samya\PyCharmProject\COVID-Global-Data-Analysis\covid_dataset\country_wise_latest.csv') #country_wise_latest.csv
c19c_data= pd.read_csv(r'C:\Users\samya\PyCharmProject\COVID-Global-Data-Analysis\covid_dataset\covid_19_clean_complete.csv') #covid_19_clean_complete.csv
day_data= pd.read_csv(r'C:\Users\samya\PyCharmProject\COVID-Global-Data-Analysis\covid_dataset\day_wise.csv') #day_wise
world_data= pd.read_csv(r'C:\Users\samya\PyCharmProject\COVID-Global-Data-Analysis\covid_dataset\worldometer_data.csv')#worldometer_data
us_data= pd.read_csv(r'C:\Users\samya\PyCharmProject\COVID-Global-Data-Analysis\covid_dataset\usa_county_wise.csv') #usa_county_wise


cwl_data.head()

def df_cleaning(df):
    # function to check and clean the 
    print('Dataframe Info',df.info())
    print("Check the null value and print the summary report",df.isnull().sum())
    print("\nShape of the dataframe", df.shape)
    print("\nData Types of each columns", df.dtypes)
    print("\nColumn info\n", df.columns)
    print('\nCheck Duplicate values in Dataframe\n', df.duplicated().sum())
    print('\nCheck the unique values of dataframe\n', df.nunique())
    #print('\n Check the unique values of dataframe', df.unique)
    

df_cleaning(cwl_data) 