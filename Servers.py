import config
import finnhub
import requests
from requests.auth import HTTPBasicAuth

class Servers:
    def __init__(self) -> None:
        self.Finn_Client = finnhub.Client(api_key=config.finnhub_key)
        self.Market_Client = HTTPBasicAuth('Authorization', config.Market_key)
        print("Success connection to servers.")

    def getStock(self,stock: str) -> None:
        quote = self.Finn_Client.quote(stock)
        return quote["c"]
    