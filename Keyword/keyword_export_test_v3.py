import nltk
from collections import Counter
from textblob import TextBlob

# NLTK 데이터 다운로드
nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')

text = '''... (your text here) ...'''

text = '''(서울=뉴스1) = 최준기 KT AI/빅데이터사업본부 본부장이 31일 서울 서초구 KT 연구개발센터에서 기자설명회에서 기존 모델보다 비용을 약 30% 절감할 수 있는 초거대 인공지능(AI) `믿음`(Mi:dm)에 대해 설명하고 있다. 출시하는 모델은 베이직, 스탠다드, 프리미엄, 엑스퍼트 등 총 4종이다. 경량 모델부터 초대형 모델까지 기업의 규모와 목적에 맞게 맞춤형으로 사용할 수 있도록 한다. (KT 제공) 2023.10.31/뉴스1 photo@news1.kr
'''
# =>> 네츄럴

text = '''아 출근하기 존나 싫다'''

# TextBlob을 이용한 품사 태깅
blob = TextBlob(text)
tags = blob.tags  # 각 단어의 품사 정보를 포함하는 리스트

# 부사를 제외한 단어들
non_adverb_words = [word for word, pos in tags if not pos.startswith("RB")]

# 각 단어의 빈도수 카운트
word_counts = Counter(non_adverb_words)

# 각 단어별 감성 분석
word_sentiments = {}
for word in word_counts.keys():
    analysis = TextBlob(word)
    word_sentiments[word] = analysis.sentiment.polarity

# 결과 출력
print("Word Frequencies (Excluding Adverbs):")
for word, count in word_counts.items():
    print(f"{word}: {count}")

print("\nSentiment Analysis:")
for word, sentiment in word_sentiments.items():
    if sentiment > 0:
        sentiment_str = "positive"
    elif sentiment < 0:
        sentiment_str = "negative"
    else:
        sentiment_str = "neutral"
    print(f"{word}: {sentiment_str} ({sentiment:.2f})")
