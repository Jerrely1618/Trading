import finnhub
import pandas as pd
import datetime as dt
from time import time
from config import Finnhub_key,Market_key
from bokeh.io import curdoc
from bokeh.plotting import figure
from bokeh.themes import Theme
from bokeh.embed import components
from bokeh.models import NumeralTickFormatter
from math import pi

class APIconnection:
    def __init__(self) -> None:
        try:
            self.finnhub_Conn = finnhub.Client(api_key=Finnhub_key)
            self.Market_Client = (Market_key)
        except Exception as err:
            print(f"Unexpected {err=}, {type(err)=}")

    def getStockPrice(self,stock: str) -> int:
        return round(self.finnhub_Conn.quote(stock)['c'],2)
    
    def getStockGraph(self,stock: str, from_: str):
        graph_time={
            "Max":[round(time()),"M"],
            "5Y":[157680000,"M"],
            "1Y":[31536000,"D"],
            "6M":[14515200,"D"],
            "1M":[2419200,"60"],
            "5D": [604800,"30"],
            "1D": [86400,"15"],
        }
        data = self.finnhub_Conn.stock_candles(symbol=stock, resolution=graph_time[from_][1] , to=round(time()), _from=round(time())-graph_time[from_][0])
        df = self.DatatoPD(data)
        TOOLS = "wheel_zoom, box_zoom, save"
        curdoc().theme = Theme(filename="theme.yaml")
        p = figure(x_axis_type="datetime", tools=TOOLS, width=1000, height=480, title = stock)
        p.xaxis.major_label_orientation = pi / 4
        p.grid.grid_line_alpha = 0.3

        p.line(df.Time,df.Cost)
        p.yaxis[0].formatter = NumeralTickFormatter(format="$0.00")
        curdoc().add_root(p)
        return components(p)

    def DatatoPD(self,data: dict):
        for i,t in enumerate(data['t']):
            data['t'][i] = dt.datetime.fromtimestamp(t).strftime('%Y-%m-%d %H:%M:%S')
        
        for i,c in enumerate(data['c']):
            data['c'][i] = round(c,2)
        
        pandasData = list(zip(data['t'],data['c']))
        df = pd.DataFrame(pandasData,columns=['Time','Cost'])
        df['Time'] = pd.to_datetime(df['Time'])
        df = df.sort_values(by=['Time'])
        
        df.head()
        df.info()

        return df
    