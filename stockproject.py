import requests
import time
keywords = ["stocks", "crypto", "bitcoin", "NYSE", "NASDAQ", 
            "Federal Reserve", "inflation", "interest rates",
            "earnings", "IPO", "merger", "hedge fund"]
parameters = {
    "apikey":"da67e67ed766f4f00568798553059138",
    "category":"business",
    "lang":"en",

}
#vars=
seen = set()
Not_Found = False


while True:
        reponse = requests.get("https://gnews.io/api/v4/search?q=Google&lang=en&max=5",params=parameters)
        print(reponse.status_code)
        res_json = reponse.json()['articles']
        for article in res_json:
            print(article['title'])
            time.sleep(5)