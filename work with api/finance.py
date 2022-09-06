# pip install yfinance
import yfinance as yf
# def wirteinfile(file_name, string):
#     with open(file_name,'w',encoding='utf-8') as file:
#         file.write(string)
#         file.close()
btc = yf.Ticker("BTC")
print(btc.actions)
# wirteinfile("data.txt", type(btc.history()))
