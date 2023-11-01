from collections import Counter
import re
from pprint import pprint

# 샘플 텍스트
text = """KT, SKT, 왕,,출근하기 존나 싫다. 행복할 리가 있겠니? 아... 출근하기 존나 싫다... 근데 진짜로? 9시간 뒤 출근이라는데 이게 실화인지 내일은 칼퇴할 수 있을런지, 운동은 갈 수 있을지!!!!! 지..."""

# 특수문자 제거 (물음표와 느낌표 제외)
cleaned_text = re.sub(r'[^A-Za-z가-힣!? ]', '', text)

# 텍스트를 단어별로 분리
words = cleaned_text.split()

# 각 단어의 빈도수 카운트
word_counts = Counter(words)

# 감성 사전 정의
sentiment_dict = {
    '존나': -1,
    '싫다': -1,
    '좋다': 1,
    '행복하다': 1,
    # 추가적인 단어들...
}

# 주어진 텍스트에서 단어별 감성 점수 계산
word_sentiments = {}
for word, count in word_counts.items():
    sentiment = sentiment_dict.get(word, 0)  # 사전에 없는 단어는 0(중립)으로 간주
    word_sentiments[word] = sentiment

# 결과 출력
print("\nSentiment Analysis:")
max_word_length = max(len(word) for word in word_counts.keys())

for word, count in word_counts.items():
    sentiment = word_sentiments[word]
    if sentiment > 0:
        sentiment_str = "긍정"
    elif sentiment < 0:
        sentiment_str = "부정"
    else:
        sentiment_str = "중립"
    print(f"keyword: '{word:<{max_word_length}}' | cnt: {count:3} | type: {sentiment_str:<5} | sc: {sentiment}")
