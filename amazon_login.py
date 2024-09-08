from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

# 環境変数から認証情報を取得
email = os.getenv('AMAZON_EMAIL')
password = os.getenv('AMAZON_PASSWORD')

if not email or not password:
    raise Exception("Please set the EMAIL and PASSWORD enviroment variables")

# ChromeDriverの設定
options = Options()
options.add_argument("--start-maximized") # ブラウザを最大化して開始
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:
    # Amazonのログインページを開く
    driver.get('https://www.amazon.co.jp/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.co.jp%2F%3F%26tag%3Dhydraamazonav-22%26ref%3Dnav_signin%26adgrpid%3D157529192761%26hvpone%3D%26hvptwo%3D%26hvadid%3D675114138684%26hvpos%3D%26hvnetw%3Dg%26hvrand%3D13443556532871517128%26hvqmt%3De%26hvdev%3Dc%26hvdvcmdl%3D%26hvlocint%3D%26hvlocphy%3D9198555%26hvtargid%3Dkwd-333588672930%26hydadcr%3D15460_13679902%26gad_source%3D1&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=jpflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0')

    # メールアドレスを入力
    email_field = driver.find_element(By.ID, 'ap_email')
    email_field.send_keys(email)
    email_field.send_keys(Keys.RETURN)

    # 次のページが読み込まれるのを待つ
    time.sleep(2)

    # パスワードを入力
    password_field = driver.find_element(By.ID, 'ap_password')
    password_field.send_keys(password)
    password_field.send_keys(Keys.RETURN)

    # 必要に応じて追加の手順(2段階認証など)を処理
    # ここでは例として2秒待機する
    time.sleep(5)

finally:
    # ブラウザを閉じる
    driver.quit()