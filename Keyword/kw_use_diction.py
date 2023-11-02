from collections import Counter
import re
from pprint import pprint

# 샘플 텍스트
text = """나는 오늘 정말 행복했다. 아침부터 하늘이 맑고 바람이 부드럽게 불어와서 아름다웠다. 하늘에는 밝은 햇살이 가득했고, 나는 그 아래에서 사랑하는 사람과 함께 산책을 즐겼다. 그녀와의 대화는 항상 나를 기쁘게 해주었다. 중간에 어떤 사람이 우리를 무시하려 했지만, 그런 것은 중요하지 않았다. 사랑하는 사람과의 행복한 시간은 그 어떤 짜증나는 상황보다 더 값졌다.

그러나 저녁이 되면서 불안한 소식이 들려왔다. 내 친구가 어려운 상황에 처해 있다는 소식이었다. 그의 슬픈 목소리를 듣고 나는 울다가 결국 눈물을 흘렸다. 그렇게 힘들다는 그의 얘기에 짜증이 날 정도로 화가 났다. 누군가가 그를 해코지했다는 얘기를 듣고 나는 그를 위해 화를 내기도 했다. 그러나 그의 슬픔은 어두워서 나를 더욱 우울하게 만들었다. 그래도 내일은 다시 밝은 날이 올 것이라는 희망을 버리지 않았다. !@!#@!#@#$@#%#$^"""

# 특수문자 제거 (물음표와 느낌표 제외)
cleaned_text = re.sub(r'[^A-Za-z가-힣!? ]', '', text)
print(cleaned_text)

# 텍스트를 단어별로 분리
words = cleaned_text.split()

# 각 단어의 빈도수 카운트
word_counts = Counter(words)

# 감성 사전 정의
sentiment_dict = {
    # 명사
    '행복': 1,
    '사랑': 1,
    '기쁨': 1,
    '불안': -1,
    '슬픔': -1,
    '짜증': -1,

    # 동사
    '즐기다': 1,
    '웃다': 1,
    '기다리다': -1,
    '울다': -1,
    '운다': -1,
    '화내다': -1,
    '무시하다': -1,

    # 형용사
    '아름답다': 1,
    '밝다': 1,
    '슬프다': -1,
    '힘들다': -1,
    '어둡다': -1,
    '낡다': -1,
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
    print(f"{word:<{max_word_length}} - cnt: {count:3}, type: {sentiment_str:<5}, sc: {sentiment}")

