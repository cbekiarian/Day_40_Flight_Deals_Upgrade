import requests
import datetime as dt
from pprint import pprint
class FlightData:
    def __init__(self,stop_over = 0,via_city=""):
        self.stop_over = stop_over
        self.via_city = via_city
        self.date_now = dt.datetime.now().strftime("%d/%m/%Y")
        self.date_later = dt.datetime.now() + dt.timedelta(days = 6*30)
        self.date_later =self.date_later.strftime("%d/%m/%Y")
    def get_flights(self,name):
        URL ="https://api.tequila.kiwi.com/v2/search"
        KEY =
        headers = {
                'accept': 'application/json',
                'apikey': KEY
            }
        params = {
            "fly_from": "SKG",
            "fly_to": name,
            "date_from": self.date_now,
            "date_to": self.date_later,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "ret_from_diff_city": False,
            "ret_to_diff_city":False,
            "curr" : "EUR",
            "conn_on_diff_airport": 0,
            "max_stopovers": self.stop_over,
            "one_for_city" : 1,
        }
        response = requests.get(url= URL,params= params,headers=headers)
        response.raise_for_status()
        try:
            res = response.json()["data"][0]
        except IndexError:
            second = FlightData(stop_over=3)
            pop =second.get_flights(name)
            response.raise_for_status()

            return pop




        #     print(f"{index["cityTo"]}:{index["price"]} Euros")
        #     res.append ( {
        #         "city": index["cityTo"],
        #         "price":index["price"],
        #     })

        return res
