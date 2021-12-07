import requests
import bs4
result = requests.get("https://id.wikipedia.org/wiki/Mi_(makanan)")

soup = bs4.BeautifulSoup(result.text, "lxml") # lxml is the parser

# images_text = soup.select("img")[0]
# images_url = images_text['src']
# images_class = soup.select(".image")
# print(images_text)
# print('\n')
# print(images_class)
# print('\n')
# print(images_url)
image_link = requests.get('https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Mi_%28Mi_makanan%29.jpg/220px-Mi_%28Mi_makanan%29.jpg')
# print(image_link.content) # print the content of the image(binary file)

# menyimpang gambar ke dalam folder
f = open('mi.jpg', 'wb')
f.write(image_link.content)
f.close()