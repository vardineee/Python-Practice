from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
articles = soup.find_all(name="span", class_ = "titleline")
article_texts = []
article_links = []

for articles_tag in articles:
    article_text = articles_tag.getText()
    article_texts.append(article_text)

    article_link = articles_tag.select_one(selector="span a").get("href")

    article_links.append(article_link)



# article_text=article_tag.getText()
# print(article_text)
# article_link = article_tag.get("href")
# print(article_link)
article_votes = [int(score.getText().split()[0])  for score in soup.find_all(name="span", class_ = "score")]
print(article_texts)
print(article_links)
print(article_votes)

largest_number = max(article_votes)
largest_index = article_votes.index(largest_number)


print(article_texts[largest_index])
print(article_links[largest_index])
print(largest_number)
# print(article_vote)



# with open ("website.html") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# anch = soup.find_all(name="a")
# print(anch)
# for tag in anch:
#     print(tag.get("href"))