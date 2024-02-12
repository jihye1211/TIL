import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

# vivino 와인 정보 사이트 크롤링
# https://www.vivino.com/

driver = None

def create_driver():
    options = Options()
    driver = webdriver.Chrome(options=options)
    return driver

def slow_scroll(driver, scroll_step, delay):
    total_height = driver.execute_script("return document.body.scrollHeight")
    for i in range(0, total_height+3600, scroll_step):
        driver.execute_script(f"window.scrollTo(0, {i});")
        time.sleep(delay)



def crawl_vivino_data_selenium(driver, id, vintage):
    url = f"https://www.vivino.com/w/{id}" if pd.isna(vintage) else f"https://www.vivino.com/w/{id}?year={int(vintage)}"
    
    try:
        driver.get(url)
        WebDriverWait(driver, 10).until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
        slow_scroll(driver, 300, 0.5)

        # Grapes, Wine style, Alcohol content, Food Pairings 정보 추출
        grapes, wine_style, alcohol_content, food_pairings = [], [], [], []  # 빈 리스트로 초기화

        # Food Pairings 정보 추출
        food_pairings_elements = driver.find_elements(By.CLASS_NAME, "foodPairing__foodContainer--1bvxM")
        for element in food_pairings_elements:
            food_pairings.append(element.text.split('\n'))

        # Wine Facts 정보 추출
        wine_facts = driver.find_elements(By.CSS_SELECTOR, ".wineFacts__wineFacts--2Ih8B .wineFacts__fact--3BAsi")
        for fact in wine_facts:
            header = fact.find_element(By.XPATH, "./..").text
            if 'Grapes' in header:
                grapes = fact.text if fact.text else []
            elif 'Wine style' in header:
                wine_style = fact.text if fact.text else []
            elif 'Alcohol content' in header:
                alcohol_content = fact.text if fact.text else []

        return grapes, wine_style, alcohol_content, food_pairings, url
    except Exception as e:
        print(f"Error while fetching data for URL: {url} - {e}")
        return [], [], [], [], url  # 예외가 발생하면 모든 필드를 빈 리스트로 반환하되, URL은 반환

# Selenium 드라이버 설정
# 단일 WebDriver 인스턴스 사용하여 드라이버 설정
driver = create_driver()

# CSV 파일 로드
data = pd.read_csv('modified_red_image_1.csv')

# 새 정보를 저장할 리스트
grapes_data = []
wine_style_data = []
alcohol_content_data = []
food_pairings_data = []
urls = []

# 모든 레코드에 대해 크롤링
for index, row in data.iterrows():
    grapes, wine_style, alcohol_content, food_pairings, url = crawl_vivino_data_selenium(driver, row['ID'], row['Vintage'])
    grapes_data.append(grapes)
    wine_style_data.append(wine_style)
    alcohol_content_data.append(alcohol_content)
    food_pairings_data.append(food_pairings)
    urls.append(url)

# 모든 크롤링 작업 후 WebDriver 세션 종료
driver.quit()

# 데이터프레임에 새 열로 정보 추가
data['Grapes'] = grapes_data
data['Wine Style'] = wine_style_data
data['Alcohol Content'] = alcohol_content_data
data['Food Pairings'] = food_pairings_data
data['URL'] = urls

# 변경된 데이터프레임을 새로운 CSV 파일로 저장
data.to_csv('red_updated_vivino_data1.csv', index=False)


## rose, sparkling, fortified, dessert, red