import bs4
import httpx

response = httpx.get("https://2ip.ru/")
response.raise_for_status()
text = response.text


d_clip_button_pos = text.find('id="d_clip_button"')
print(d_clip_button_pos)
span_pos = text.find("<span>", d_clip_button_pos)
span_pos_end = text.find("</span>", d_clip_button_pos)
print(span_pos)
print(text[span_pos + 6 : span_pos_end])

soup = bs4.BeautifulSoup(text, features="html.parser")
d_clip_button = soup.find(id="d_clip_button")
span = d_clip_button.find("span")
print(span.text)


HEADERS = {
    "Cookie": "_ym_uid=1639148487334283574; _ym_d=1639149414; \
_ga=GA1.2.528119004.1639149415; _gid=GA1.2.512914915.1639149415; \
habr_web_home=ARTICLES_LIST_ALL; hl=ru; fl=ru; _ym_isad=2; \
__gads=ID=87f529752d2e0de1-221b467103cd00b7:\
T=1639149409:S=ALNI_MYKvHcaV4SWfZmCb3_wXDx2olu6kw",
    "Accept-Language": "ru-RU,ru;q=0.9",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Cache-Control": "max-age=0",
    "If-None-Match": 'W/"37433-+qZyNZhUgblOQJvD5vdmtE4BN6w"',
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36",
    "sec-ch-ua-mobile": "?0",
}

MY_HUBS = {"Смартфоны", "Удалённая работа", "IT-компании"}


response = httpx.get("https://habr.com/ru/news/", headers=HEADERS)
response.raise_for_status()
text = response.text

r = httpx.get("https://habr.com/kek/v2/articles/most-reading?fl=ru&hl=ru")
most_reading = r.json()
print(most_reading)


soup = bs4.BeautifulSoup(text, features="html.parser")
articles = soup.find_all("article")
for article in articles:
    title = article.find("h2")
    hubs = article.find_all("a", class_="tm-article-snippet__hubs-item-link")
    article_hubs = set([hub.find("span").text for hub in hubs])
    if MY_HUBS & article_hubs:
        a_tag = title.find("a")
        href = a_tag.attrs["href"]
        url = "https://habr.com" + href
        print(title.text, url)
        print("----")
