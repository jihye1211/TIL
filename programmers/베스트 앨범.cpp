#include <string>
#include <vector> // �迭�� ����
#include <algorithm>
#include <unordered_map>
// key�� value ����
// Hash Table�� ����� Ű�� ������ �̿����� ����.(map�� Ű�� ������ ������)
// ���ĵǾ� ���� �ʿ䰡 �����Ƿ� ����, ���� ���� �����Ƿ� unorderde_map�� ����Ѵ�.

using namespace std;


bool compare(pair<int,int> a,pair<int,int> b){
    return a.first > b.first;
}
bool compare_map_value(pair<string,int> a,pair<string,int> b){
    return a.second > b.second;
}
vector<int> solution(vector<string> genres, vector<int> plays) {
    vector<int> answer;
    unordered_map<string,vector<pair<int,int>>> genre_playlist;  // �帣,vector(���ȸ��, �뷡 ������ȣ(�ε���) ��)
    unordered_map<string,int> genre_play_cnt;                   // �帣, �� ���ȸ��
    vector<pair<string,int>> genre_play_cnt_v;                  //genre_play_cnt�� value�� �����ϱ� ���� vector
    
    /*hash map�� ������ ����*/
    for(int i=0; i < genres.size(); i++){
        genre_playlist[genres[i]].push_back(make_pair(plays[i],i));
        genre_play_cnt[genres[i]]+=plays[i];
    }

    /*�帣�� ������ǵ� �󵵼��� ������������ ����*/
    for(auto &k : genre_playlist){
        sort(k.second.begin(),k.second.end(),compare);
    }

    /*�帣�� �� ���Ƚ�� ������������ ����*/
    genre_play_cnt_v.assign(genre_play_cnt.begin(),genre_play_cnt.end());
    sort(genre_play_cnt_v.begin(),genre_play_cnt_v.end(),compare_map_value);
    
    for(int i=0; i < genre_play_cnt_v.size(); i++){
        string genre_name = genre_play_cnt_v[i].first;
        /*�뷡�� �� ���� ��� ����Ʈ �ٹ��� ����ϹǷ�(�ּ� 1��)*/
        /*������ 1���� 1����, 2���̻��̸� 2�������� answer�� ����*/
        for(int j=0; (j < genre_playlist[genre_name].size() ) && (j < 2) ; j++){
            answer.push_back(genre_playlist[genre_name][j].second);      //�뷡 ������ȣ answer�� ����
        }
    }
    return answer;
}