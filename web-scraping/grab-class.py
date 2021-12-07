import requests
import bs4
result = requests.get("https://id.wikipedia.org/wiki/Mi_(makanan)")
# print(type(result))
# print(result.text)

soup = bs4.BeautifulSoup(result.text, "lxml") # lxml is the parser

# uncomment untuk menampilkan output
# print(soup)
# print(soup.select("title"))
# print(soup.select(".toclevel-1"))
# print(soup.select(".toclevel-1")[0])
# print(soup.select(".toclevel-1")[0].text)
# for item in soup.select(".toclevel-1"):
#     print(item.text)

