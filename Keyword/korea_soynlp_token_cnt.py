from collections import Counter
from soynlp.word import WordExtractor
from soynlp.tokenizer import LTokenizer
from pprint import pprint

texts = [
    "예쁜 나비가 날아간다.",
    "많은 사람들이 파크에 모였다.",
    "예쁜 꽃들이 피어있다.",
    "그는 많은 책을 읽는다."
]

texts = ['''(서울=뉴스1) = 최준기 KT AI/빅데이터사업본부 본부장이 31일 서울 서초구 KT 연구개발센터에서 기자설명회에서 기존 모델보다 비용을 약 30% 절감할 수 있는 초거대 인공지능(AI) `믿음`(Mi:dm)에 대해 설명하고 있다. 출시하는 모델은 베이직, 스탠다드, 프리미엄, 엑스퍼트 등 총 4종이다. 경량 모델부터 초대형 모델까지 기업의 규모와 목적에 맞게 맞춤형으로 사용할 수 있도록 한다. (KT 제공) 2023.10.31/뉴스1 photo@news1.kr
''']

# WordExtractor를 이용해 단어 점수 획득
word_extractor = WordExtractor()
word_extractor.train(texts)
word_score = word_extractor.extract()

# LTokenizer 초기화
cohesion_score = {word: score.cohesion_forward for word, score in word_score.items()}
tokenizer = LTokenizer(scores=cohesion_score)

# 모든 문장에서 토큰화된 단어들을 모음
all_tokens = [token for text in texts for token in tokenizer.tokenize(text)]

# 단어별 빈도수 계산
word_count = Counter(all_tokens)
pprint(word_count)
