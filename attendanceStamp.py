from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# WebDriverのセットアップ
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    # 指定したURLを開く
    driver.get("https://geechs.lightning.force.com/lightning/page/home")

    # ページが完全に読み込まれるまで待機
    time.sleep(5)  # 必要に応じて調整

    # ボタンを探してクリックする（ボタンのXPathを指定）
    try:
        # ボタンが表示されるのを待つ
        button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[contains(@onclick, "IdpOptions.useIdp") and contains(text(), "次を使用してログイン")]'))
        )
        button.click()
        print("ボタンをクリックしました。")
    except (NoSuchElementException, TimeoutException):
        print("指定されたボタンが見つかりません。次の動作に移行します。")

    # 次の動作に移行
    # ここに次の動作を記述
    # 例: 次のページが表示されるまで待機するなど
    time.sleep(5)  # 必要に応じて調整

finally:
    # ブラウザを閉じない
    print("スクリプトが終了しましたが、ブラウザは開いたままにします。")