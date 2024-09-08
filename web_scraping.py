# web_scraping.py

# requestsとBeautifulSoupのインポート
import requests
from bs4 import BeautifulSoup

# ウェブサイトをスクレイピング関数
def scrape_website(url):
    # 指定されたURLにHTTPリクエストを送信
    response = requests.get(url)
    # 取得したHTMLコンテンツをパース
    soup = BeautifulSoup(response.content, 'html.parser')
    # ページタイトルを取得
    title = soup.title.string
    return title

# メイン関数
def main():
    url = "https://www.amazon.co.jp/" # スクレイピング対象の実際のURL
    # ウェブサイトのタイトルを取得
    title = scrape_website(url)
    print(f"The title of the website is: {title}")

# このファイルが直接実行された場合、main関数を呼び出す
if __name__ == "__main__":
    main()