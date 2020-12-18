#include <string>
#include <vector>
#include <algorithm>

using namespace std;

bool solution(vector<string> phone_book) {
    bool answer = true;
    sort(phone_book.begin(), phone_book.end());
    // 먼저 sort를 실행한 후
    for (int i = 0; i < phone_book.size() - 1; i++) {
        if (phone_book[i] == phone_book[i + 1].substr(0, phone_book[i].size())) 
            // substr을 사용하여 접두어가 있는지 확인
            // 접두가 가능한 "짧은 번호"의 길이만큼만 비교대상인 "긴 번호"의 시작부터의 번호를 비교
            // substr
            // : 문자열의 일부를 리턴함.
            //   문자열의 pos 번째 문자부터 count 길이 만큼의 문자열을 리턴. 만약에, 인자로 전달된 부분 문자열의 길이가 문자열 보다 길다면, 그 이상을 반환하지 않고 문자열의 끝 까지만 리턴한다.
            //   또한, count 로 npos를 전달한다면, 자동으로 pos부터 원래 문자열의 끝까지 리턴
            //   pos: 첫번째 문자의 위치
            //   count: 부분 문자열의 길이
            //   리턴값: 원래 문자열에서 [pos, pos + count) 까지의 문자열을 반환
            return false;
    }
    return answer;
}
