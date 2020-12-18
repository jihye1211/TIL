#include <string>
#include <vector>
#include <queue>
 
using namespace std;
 
int solution(vector<int> priorities, int location) {
    int answer = 0;
    priority_queue<int> pq;
    queue<pair<int,int>> q;
    
    int size = priorities.size();
    for(int i=0; i<size; i++) {
        q.push(make_pair(i, priorities[i]));
        pq.push(priorities[i]);
    }
    
    while(!q.empty()) {
        int i = q.front().first;
        int p = q.front().second;
        q.pop();
        
        //현재 문서의 중요도가 가장 높은 중요도라면 인쇄
        if(p == pq.top()) {
            pq.pop();
            answer += 1;
            
            //현재 문서가 내가 인쇄를 요청한 문서다
            if(i == location) {
                break;
            }
            
        } else {
            //다시 큐에 넣는다.
            q.push(make_pair(i,p));
        }
    }
    return answer;
}