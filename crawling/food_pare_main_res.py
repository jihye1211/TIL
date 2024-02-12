import requests
import pandas as pd

def crawl_vivino_data_selenium(driver, id, vintage):
    url = f"https://www.vivino.com/w/{id}" if pd.isna(vintage) else f"https://www.vivino.com/w/{id}?year={int(vintage)}"
    
    try:
        res = requests.get(url)

        # Grapes, Wine style, Alcohol content, Food Pairings 정보 추출
        grapes, wine_style, alcohol_content, food_pairings = [], [], [], []  # 빈 리스트로 초기화

        # Food Pairings 정보 추출
        # food_pairings_elements = driver.find_elements(By.CLASS_NAME, "foodPairing__foodContainer--1bvxM")
        # for element in food_pairings_elements:
        #     food_pairings.append(element.text.split('\n'))

        # Wine Facts 정보 추출
        # wine_facts = driver.find_elements(By.CSS_SELECTOR, ".wineFacts__wineFacts--2Ih8B .wineFacts__fact--3BAsi")
        # for fact in wine_facts:
        #     header = fact.find_element(By.XPATH, "./..").text
        #     if 'Grapes' in header:
        #         grapes = fact.text if fact.text else []
        #     elif 'Wine style' in header:
        #         wine_style = fact.text if fact.text else []
        #     elif 'Alcohol content' in header:
        #         alcohol_content = fact.text if fact.text else []

        return grapes, wine_style, alcohol_content, food_pairings, url
    except Exception as e:
        print(f"Error while fetching data for URL: {url} - {e}")
        return [], [], [], [], url  # 예외가 발생하면 모든 필드를 빈 리스트로 반환하되, URL은 반환
