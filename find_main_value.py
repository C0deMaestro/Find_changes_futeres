
import matplotlib.pyplot as plt



plt.figure(figsize=(14, 7))

plt.plot(times, prices, label='ETH Price')

plt.xlabel('Time')

plt.ylabel('Price')

plt.legend()



plt.twinx()



plt.plot(joined_df['time'], joined_df['price_btc'], color='r', label='BTC Price')

plt.xlabel('Time')

plt.ylabel('Price')

plt.legend()



plt.twinx()



plt.plot(joined_df['time'], joined_df['price_eth'], color='g', label='ETH Price')

plt.xlabel('Time')

plt.ylabel('Price')

plt.legend()



plt.twinx()



plt.plot(joined_df['time'], joined_df['price_eth'] - (joined_df['price_btc'].corr(joined_df['price_eth']) * joined_df['price_btc']), color='b', label='ETH Price - BTC Correlation')

plt.xlabel('Time')

plt.ylabel('Price')

plt.legend()