# nohup python3 food_pair_main_v2.py &
import time
import logging
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

# 로깅 설정
logging.basicConfig(filename='vivino_crawling.log', level=logging.INFO, format='%(asctime)s %(levelname)s:%(message)s')

# vivino 와인 정보 사이트 크롤링
# https://www.vivino.com/

driver = None

def create_driver():
    options = Options()
    options.add_argument('--headless')  # 헤드리스 모드 활성화
    options.add_argument('--disable-gpu')  # GPU 사용 안함, 특히 리눅스/맥에서 헤드리스 모드에 권장됨
    options.add_argument('--no-sandbox')  # 샌드박스 비활성화, 특히 리눅스에서 권장됨
    options.add_argument('--disable-dev-shm-usage')  # /dev/shm 파티션 사용 안함, 도커나 CI 환경에서 유용
    driver = webdriver.Chrome(options=options)
    return driver

def slow_scroll(driver, scroll_step, delay):
    total_height = driver.execute_script("return document.body.scrollHeight")
    for i in range(0, total_height + 3600, scroll_step):
        driver.execute_script(f"window.scrollTo(0, {i});")
        time.sleep(delay)

def crawl_vivino_data_selenium(driver, id, vintage):
    url = f"https://www.vivino.com/w/{id}" if pd.isna(vintage) else f"https://www.vivino.com/w/{id}?year={int(vintage)}"
    
    try:
        driver.get(url)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "body")))

        slow_scroll(driver, 300, 0.5)

        # Initialize data containers
        grapes, wine_style, alcohol_content, food_pairings = None, None, None, []

        # Check and extract Food Pairings information
        food_pairings_elements = driver.find_elements(By.CLASS_NAME, "foodPairing__foodContainer--1bvxM")
        if food_pairings_elements:
            food_pairings = [element.text.split('\n') for element in food_pairings_elements]

        # Extract Wine Facts information
        wine_facts_elements = driver.find_elements(By.CSS_SELECTOR, ".wineFacts__wineFacts--2Ih8B .wineFacts__fact--3BAsi")
        for fact in wine_facts_elements:
            fact_header = fact.find_element(By.XPATH, "./..").text
            fact_text = fact.text
            if 'Grapes' in fact_header and fact_text:
                grapes = fact_text
            elif 'Wine style' in fact_header and fact_text:
                wine_style = fact_text
            elif 'Alcohol content' in fact_header and fact_text:
                alcohol_content = fact_text

        logging.info(f"Data fetched successfully for URL: {url}")
        return grapes, wine_style, alcohol_content, food_pairings, url
    except Exception as e:
        logging.error(f"Error while fetching data for URL: {url} - {e}")
        return None, None, None, [], url

# Selenium 드라이버 설정
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
data.to_csv('red_updated_vivino_data.csv', index=False)