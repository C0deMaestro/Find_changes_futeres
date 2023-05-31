import numpy
from sklearn.linear_model import LinearRegression

def find_corr_coeff():#ищем коэффициент корреляции между ethusdt и btcusdt
    with open("data_ETHUSDT.txt", "r") as prices_files:
        lst_eth = list(map(float,prices_files.read().split(", ")[:-1]))

    with open("data_BTCUSDT.txt", "r") as prices_files:
        lst_btc = list(map(float,prices_files.read().split(", ")[:-1]))

    coef_corr = numpy.corrcoef(numpy.array(lst_eth),numpy.array(lst_btc))[0,1]
    print(coef_corr)

find_corr_coeff()