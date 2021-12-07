import requests
import bs4
result = requests.get("http://www.example.com")
# print(type(result))
# print(result.text)

soup = bs4.BeautifulSoup(result.text, "lxml") # lxml is the parser
# print(soup)
print(soup.select("title"))
print(soup.select("title")[0].getText())
print(soup.select("p"))
print(soup.select("p")[0].getText())
print(soup.select("h1"))
