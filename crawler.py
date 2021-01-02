import requests
from bs4 import BeautifulSoup

def naver_news(keyword):
    news_url = "https://search.naver.com/search.naver?where=news&query="

    raw = requests.get(news_url+keyword, headers={'User-Agent':'Mozilla/5.0'})
    html = BeautifulSoup(raw.text, "html.parser")
    articles = html.select("ul.list_news > li")

    l = []

    for i in range(5):
        target_url = articles[i].select_one("a")["href"]
        title = articles[i].select_one("a.news_tit").text
        image = articles[i].select_one("img.thumb.api_get")
        if image is not None:
            image = image["src"]
        contents = articles[i].select_one("div.news_dsc").text
        if len(contents) >= 60:
            contents = contents[:57]+"..."

        news_dict = {'url' : target_url, 'title' : title, 'img' : image, 'contents' : contents}
        l.append(news_dict)

    return l

def main():
    keyword = input("keyword : ")

    l = naver_news(keyword)

    # test print
    for i in range(len(l)):
        print('[{}]'.format(i+1))
        print(l[i]['url'])
        print(l[i]['title'])
        print(l[i]['img'])
        print(l[i]['contents'])
    
if __name__ == "__main__":
    main()
