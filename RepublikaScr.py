from bs4 import BeautifulSoup
import requests
import time
import datetime
import json

html_text = requests.get('https://www.republika.co.id/').text
soup = BeautifulSoup(html_text, 'lxml')
def find_news():
    news = soup.find_all('li', class_ = 'list-group-item list-border conten1')
    data = []
    with open('data.json', 'w') as f:
        for new in news:
            title = new.h3.text.strip()
            categories = new.find('span', class_ = 'kanal-info').text
            waktu = new.find('div', class_ = 'date').text.split('-')
            wanci = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            info = {"Judul Berita    :" : title, "Waktu Publish   :" : waktu[1].strip(), "Kategori        :" : categories, "Waktu Akses     :" : wanci}
            data.append(info)
        jdumps = json.dumps(data)
        f.writelines(jdumps)

if __name__ == '__main__':
    while True:
        time_wait = 1
        find_news()
        print(f"Waiting for {time_wait} minutes.....")
        time.sleep(time_wait*20)