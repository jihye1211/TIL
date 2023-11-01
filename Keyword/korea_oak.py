from konlpy.tag import Okt
import jpype1

# JVM 경로 직접 지정
jpype.startJVM("/Library/Java/JavaVirtualMachines/adoptopenjdk-16.jdk/Contents/Home")

# Okt 형태소 분석기 인스턴스 생성
okt = Okt()

text = """그곳에는 예쁜 나비가 많다. 하늘을 날아다니는 모습이 아름답다."""

# 형태소 분석
morphs = okt.pos(text)

# 부사를 제외한 명사와 동사, 형용사 추출
keywords = [word for word, pos in morphs if pos in ["Noun", "Verb", "Adjective"]]

# 결과 출력
print("Extracted Keywords:", keywords)
