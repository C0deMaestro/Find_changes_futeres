import requests,numpy
from datetime import datetime

def responce(start_timestamp,end_timestamp,symbol):
    base_url = "https://api.binance.com/"
    symbol = symbol
    url = f"{base_url}api/v3/klines?symbol={symbol}&interval=1d&startTime={start_timestamp}&endTime={end_timestamp}"
    param = {"limit":1000}
    response = requests.get(url,params=param)
    return response.json()

def get_time(year_s,month_s,day_s,year_e,month_e,day_e):
    start_date_1 = datetime(year=year_s, month=month_s, day=day_s)
    end_date_1 = datetime(year=year_e, month=month_e, day=day_e)
    start_timestamp = int(start_date_1.timestamp() * 1000)
    end_timestamp = int((end_date_1.timestamp() * 1000))
    return start_timestamp,end_timestamp

def write_data(data,symbol):
    with open(f"data_{symbol}.txt", "a") as prices_files:
        for day in data:
            prices_files.write(f"{day[4]}, ")

def main(year_s,month_s,day_s,year_e,month_e,day_e,symbol):
    start_timestamp,end_timestamp = get_time(year_s,month_s,day_s,year_e,month_e,day_e)
    answer = responce(start_timestamp,end_timestamp,symbol)
    write_data(answer,symbol)

def clear_file(symbol):
    f = open(f'data_{symbol}.txt', 'w')
    f.close()

clear_file("ETHUSDT")
clear_file("BTCUSDT")

main(2017,1,1,2020,12,31,"ETHUSDT")
main(2020,1,1,2023,12,31,"ETHUSDT")

main(2017,1,1,2020,12,31,"BTCUSDT")
main(2020,1,1,2023,12,31,"BTCUSDT")

with open("data_ETHUSDT.txt", "r") as prices_files:
    print(len(prices_files.read().split(", ")))

with open("data_BTCUSDT.txt", "r") as prices_files:
    print(len(prices_files.read().split(", ")))

