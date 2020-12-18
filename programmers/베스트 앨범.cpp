#include <string>
#include <vector> // 배열과 유사
#include <algorithm>
#include <unordered_map>
// key로 value 접근
// Hash Table을 사용해 키의 순서를 이용하지 않음.(map은 키의 순서를 유지함)
// 정렬되어 있을 필요가 없으므로 적합, 성능 또한 빠르므로 unorderde_map을 사용한다.

using namespace std;


bool compare(pair<int,int> a,pair<int,int> b){
    return a.first > b.first;
}
bool compare_map_value(pair<string,int> a,pair<string,int> b){
    return a.second > b.second;
}
vector<int> solution(vector<string> genres, vector<int> plays) {
    vector<int> answer;
    unordered_map<string,vector<pair<int,int>>> genre_playlist;  // 장르,vector(재생회수, 노래 고유번호(인덱스) 값)
    unordered_map<string,int> genre_play_cnt;                   // 장르, 총 재생회수
    vector<pair<string,int>> genre_play_cnt_v;                  //genre_play_cnt를 value로 정렬하기 위한 vector
    
    /*hash map에 데이터 삽입*/
    for(int i=0; i < genres.size(); i++){
        genre_playlist[genres[i]].push_back(make_pair(plays[i],i));
        genre_play_cnt[genres[i]]+=plays[i];
    }

    /*장르별 재생음악들 빈도수를 내림차순으로 정렬*/
    for(auto &k : genre_playlist){
        sort(k.second.begin(),k.second.end(),compare);
    }

    /*장르별 총 재생횟수 내림차순으로 정렬*/
    genre_play_cnt_v.assign(genre_play_cnt.begin(),genre_play_cnt.end());
    sort(genre_play_cnt_v.begin(),genre_play_cnt_v.end(),compare_map_value);
    
    for(int i=0; i < genre_play_cnt_v.size(); i++){
        string genre_name = genre_play_cnt_v[i].first;
        /*노래를 두 개씩 모아 베스트 앨범을 출시하므로(최소 1개)*/
        /*음악이 1개면 1개만, 2개이상이면 2개까지만 answer에 저장*/
        for(int j=0; (j < genre_playlist[genre_name].size() ) && (j < 2) ; j++){
            answer.push_back(genre_playlist[genre_name][j].second);      //노래 고유번호 answer에 삽입
        }
    }
    return answer;
}