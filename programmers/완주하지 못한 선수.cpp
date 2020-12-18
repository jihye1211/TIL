#include <string>
// std:string은 문자열을 담는데 유용한 클래스이다.
// 직관적으로 사용할 수 있도록 돕는다.
// strlen : a.size() 또는 a.length()
// strcpy : a = b
// strcmp : a == b
#include <vector> 
// vector 헤더파일 추가
// 동적으로 원소를 추가할 수 있으며 크기가 자동으로 늘어남.
#include <iostream>
// #include <string> 내장되어 있음.
#include <algorithm>
// 원소들에 대해 작업할 수 있는 여러 가지 함수(검색, 정렬, 원소들 수정학, 개수 세기 등등)을 정의함.

using namespace std;

string solution(vector<string> participant, vector<string> completion) {
    // 비어있는 벡터 생성
    std::sort(participant.begin(), participant.end());
    std::sort(completion.begin(), completion.end());

    int num = 0;

    for (int i = 0; i < participant.size(); i++) {
        // size() : container에 있는 원소의 수
        if (participant[i] != completion[i]) {
            return participant[i];
        }
    }

    return participant[participant.size()];
}