# browser_open.py

import webbrowser

def open_browser(url):
    # デフォルトのブラウザで指定されたURLを開く
    webbrowser.open(url)

def main():
    url = "https://www.wikipedia.org" # 開きたいURL
    open_browser(url)

if __name__ == "__main__":
    main()
