import finnhub
import requests
from config import Finnhub_key,Market_key

class APIconnection:
    def __init__(self) -> None:
        try:
            self.finnhub_Conn = finnhub.Client(api_key=Finnhub_key)
            self.Market_Client = (Market_key)
        except Exception as err:
            print(f"Unexpected {err=}, {type(err)=}")

    def getStockPrice(self,stock: str) -> int:
        return self.finnhub_Conn.quote(stock)['c']
    
    def getStockGraph(self,stock: str):
        return self.finnhub_Conn.stock_candles('AAPL', 'D', 0, 10000)

conn = APIconnection()
print(conn.getStockGraph("RBLX"))