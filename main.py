import requests
from bs4 import BeautifulSoup


urls = []
D = {}


def fetchPrice(arr):
  for url in arr:
    data = requests.get(url, headers={ "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"})
    raw = BeautifulSoup(data.content, features="html5lib")
    latestPrice = int("".join(raw.find(class_="a-price-whole").contents[0].split(",")))
    productName = raw.title.contents[0]
    if url in D:
      res = []
      D[url]["latestPrice"] = latestPrice
      D[url]["priceHistory"].append(latestPrice)
      D[url]["averagePrice"] = sum(D[url]["priceHistory"])/len(D[url]["priceHistory"])
      if latestPrice < D[url]["lowestPrice"]:
        D[url]["lowestPrice"] = latestPrice
      if latestPrice > D[url]["highestPrice"]:
        D[url]["highestPrice"] = latestPrice

      if D[url]["lowestPrice"] >= latestPrice:
        D[url]["response"].append("Today its price is lowest")

      elif D[url]["averagePrice"] >= latestPrice:
        D[url]["response"].append("Today its price is lower average")
      
    else:
      newProduct = {
        "name": " ".join(productName.split(" ")[0:4]),
        "latestPrice": latestPrice,
        "priceHistory": [latestPrice],
        "averagePrice": latestPrice,
        "lowestPrice": latestPrice,
        "highestPrice": latestPrice,
        "response": []
      }
      D[url] = newProduct


def addNewProduct(url):
  if url not in urls:
    fetchPrice([url])
    urls.append(url)





addNewProduct("https://www.amazon.in/Uberlyfe-Seater-Sofa-Cum-SCB-001734-BK_A/dp/B07SC7M71D/ref=lp_27060486031_1_1")

addNewProduct("https://www.amazon.in/Seiko-Sports-Day-Date-Analog-Color/dp/B096G1SVZM/ref=sr_1_1?keywords=seiko&pf_rd_i=2563504031&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_p=c0043bd7-04fa-4e5e-ab5b-3c68c27b9dd6&pf_rd_r=32YC0HW7SYH2RTV0RR5V&pf_rd_s=merchandised-search-12&pf_rd_t=30901&qid=1667420215&qu=eyJxc2MiOiI3LjU1IiwicXNhIjoiNy40NSIsInFzcCI6IjIuNTIifQ%3D%3D&s=watches&sr=1-1")

fetchPrice(urls)

print(D)

# def foo(D):
#   res = {}
  
    