from soynlp.word import WordExtractor
from soynlp.tokenizer import LTokenizer

# 텍스트 예시
texts = [
    "예쁜 나비가 날아간다.",
    "많은 사람들이 파크에 모였다.",
    "예쁜 꽃들이 피어있다.",
    "그는 많은 책을 읽는다."
]

# WordExtractor를 이용해 단어 점수 획득
word_extractor = WordExtractor()
word_extractor.train(texts)
word_score = word_extractor.extract()

# LTokenizer 초기화
cohesion_score = {word: score.cohesion_forward for word, score in word_score.items()}
tokenizer = LTokenizer(scores=cohesion_score)

# 토큰화
for text in texts:
    print(tokenizer.tokenize(text))
