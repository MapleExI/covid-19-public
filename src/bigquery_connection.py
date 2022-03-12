import pandas as pd
import pybigquery
from sqlalchemy import create_engine
from google_auth_oauthlib import flow

#class to create bigquery connection and fetch data from googles open covid 19 dataset
class bigquery_connector():
    
    def __init__(self):
        
        self.db = create_engine('bigquery://',
                           credentials_path="creds.json")
        self.df = ""

    def read_table(self):
        query = """SELECT country_name, iso_3166_1_alpha_3 as Code, SUM(new_recovered) as Recovered, SUM(new_confirmed)
                as Confirmed, SUM(new_deceased) as Deceased FROM `bigquery-public-data.covid19_open_data.covid19_open_data`
                GROUP BY country_name, Code"""
        self.df = pd.read_sql(query, con=self.db)

    def get_data(self):
        return self.df
        








