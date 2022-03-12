import plotly.express as px
import pandas as pd

class graph():

    def __init__(self, data, datatype):
        self.df = data
        self.dtype = datatype

    #create mapgraph with info of covid situation in the country
    def create_figure(self):
        fig = px.choropleth(self.df, locations="Code",
                    color=self.dtype, #chosen datatype to show
                    hover_name="country_name", # column to add to hover information
                    color_continuous_scale=px.colors.sequential.Plasma)
           
        return fig
        

        




