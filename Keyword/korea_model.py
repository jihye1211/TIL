import spacy

# spacy 한국어 모델 로드
nlp = spacy.load('ko_core_news_sm')

text = """그곳에는 예쁜 나비가 많다. 하늘을 날아다니는 모습이 아름답다."""

# 텍스트 분석
doc = nlp(text)

# 부사를 제외한 명사와 동사 추출
keywords = [token.text for token in doc if token.pos_ in ["NOUN", "VERB", "ADJ"]]

# 결과 출력
print("Extracted Keywords:", keywords)
