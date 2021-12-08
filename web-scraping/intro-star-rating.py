# tampilkan semua item yang mempunya rating bintang 2
import requests
import bs4

base_url = 'http://books.toscrape.com/catalogue/page-{}.html'
res = requests.get(base_url.format(1))
soup = bs4.BeautifulSoup(res.text, 'lxml')
products = soup.select('.product_pod')
example = products[0]

#output kosong karena ada spacing(class = star-rating Three)
print(products[0].select(".star-rating Three"))

#gantikan spacing dengan "." maka output akan muncul (class = star-rating Three)
print(products[0].select(".star-rating.Three"))

print(example.select('a')[1]['title'])