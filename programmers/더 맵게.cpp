#include <vector>
#include <queue>

using namespace std;

int solution(vector<int> scoville, int K) {
	int answer = 0;

	int lowlow_scoville; //가장 맵지 않은 음식의 스코빌 지수
	int low_scoville;    //두 번째로 맵지 않은 음식의 스코빌 지수

	//우선순위 큐를 이용하여 자동으로 오름차순으로 정렬되게 한다.
	priority_queue<int, vector<int>, greater<int>> pq(scoville.begin(), scoville.end());


	//가장 맵지 않은 음식의 스코빌 지수가 
	//기준치인 K보다 낮다면 계속 반복한다.
	while (pq.top() < K) {
		//섞을 2개의 음식이 남아있지 않다면 -1을 반환
		if (pq.size() == 1) return answer = -1;

		//가장 맵지 않은 음식을 추출
		lowlow_scoville = pq.top();
		pq.pop();

		//두 번쨰로 맵지 않은 음식을 추출
		low_scoville = pq.top();
		pq.pop();
		
		//두 음식을 섞은 다음 우선순위 큐에 넣어준다.
		pq.push(lowlow_scoville + (low_scoville * 2));

		//횟수 추가
		answer++;
	}

	return answer;
}