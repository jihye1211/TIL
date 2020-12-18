/* 문제 설명
 스파이가 가진 의상들이 담긴 2차원 배열 clothes가 주어질 때, 서로 다른 옷의 조합의 수를 return
 의상 이름의 중복X, 스파이는 최소 1개의 의상은 입음, 같은 종류의 의상을 2개 입을 수는 없음
*/
// 해시 이용하기
// 각 의상의 종류당 의상수 +1(안입는 경우)
// 모두 다 안입는 경우는 없으므로, 전체 카테고리를 곱한 뒤 -1
// 얼굴, 상의, 하의를 구별하여 저장하기 위해 map을 이용
// map의 value를 뽑아서 계산하면 됨.



#include <string>
#include <vector>
#include <map>
// 1. map이란
// Key, Value 쌍인 데이터를 균형 binary tree로 관리하는 자료구조입니다.
// * 2진 트리 종류는 Red-Black Tree을 사용
// 2. map을 사용하는 경우
// 1) 입력하는 자료를 정렬해야 할 때
//  2) 많은 자료를 저장하고, 검색이 빨라야 할 때
//  3) 빈번하게 삽입, 삭제하지 않을 때
//    - 삽입, 삭제 시 자동 정렬이 발생하여 속도가 느려짐
// 3. map의 핵심기능
// 3. map의 핵심 기능
/*  1) find
    (1) map은 key가 있다면 vector처럼 Random access가 가능
    (2) iterator를 사용하여 순차적으로 검색이 가능
  2) Insert
    (1) map은 자료를 삽입 시 내부에서 자동으로 Key 기준으로 오름차순 정렬(기본 정렬)을 하고 삽입이 됨
    (2) std::map의 원소는 std::pair 객체로 저장됨
    (3) key 중복은 허용하지 않음
    (4) 실행 중에 동적으로 크기가 확장됨
  3) erase
    (1) Random access 하여 삭제가 가능 */



#include <iostream>

using namespace std;
// 방법 1
void mix(int value, int& answer, vector<int> temp, int n);
int solution(vector<vector<string>> clothes) {
    int answer = 0;
    int value = 0;
    vector<int> temp;
    map<string, int> hash;
    for (int i = 0; i < clothes.size(); i++)
    {
        hash[clothes[i][1]]++;
    }
    map<string, int>::iterator ihash = hash.begin();
    answer = hash.begin()->second;
    for (ihash++; ihash != hash.end(); ++ihash) {
        answer = answer + (answer + 1) * ihash->second;
    }

    return answer;
}
//방법2 경우의 수를 생각하여 모두 곱하고, 안입는 경우 -1하기.
/*
int solution(vector<vector<string>> clothes) {
    map<string, int> M;
    int multiply = 1;

    for (int i = 0; i<clothes.size(); i++)
        M[clothes[i][1]]++;

    for (auto i : M)
        multiply *= (i.second + 1);

    return multiply - 1;
} */