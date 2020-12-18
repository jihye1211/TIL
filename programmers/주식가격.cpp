#include <string> 
#include <vector>
#include <stack>
// index를 가지고 스택에 입력
using namespace std; 
vector<int> solution(vector<int> prices) { 
    vector<int> answer(prices.size()); 
    stack<int> s; 
    int size = prices.size(); 
    for(int i=0;i<size;i++){ 
        while(!s.empty()&&prices[s.top()]>prices[i])
            // 감소하는 부분이 있는 index만 for문에서 answer 결정
        { answer[s.top()] = i-s.top(); s.pop(); } s.push(i); } 
    while(!s.empty()){ answer[s.top()] = size-s.top()-1; s.pop(); } 
    return answer;\
    // 감소하는 부분이 없는 경우 while문에서 answer 정해짐
    }