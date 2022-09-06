import requests


def wirteinfile(file_name, string):
    with open(file_name,'w',encoding='utf-8') as file:
        file.write(string)
        file.close()


request = requests.get("https://nova.bitcambio.com.br/api/v3/public/getmarkethistory",
                       params={
                           'market': 'BTC_BRL',
                           'count': '40'},
                       headers={

                       })
ans = request.json()
# print(*ans['result'], sep='\n')
print(ans['result'][39])