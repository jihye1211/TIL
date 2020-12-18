/* ���� ����
 �����̰� ���� �ǻ���� ��� 2���� �迭 clothes�� �־��� ��, ���� �ٸ� ���� ������ ���� return
 �ǻ� �̸��� �ߺ�X, �����̴� �ּ� 1���� �ǻ��� ����, ���� ������ �ǻ��� 2�� ���� ���� ����
*/
// �ؽ� �̿��ϱ�
// �� �ǻ��� ������ �ǻ�� +1(���Դ� ���)
// ��� �� ���Դ� ���� �����Ƿ�, ��ü ī�װ��� ���� �� -1
// ��, ����, ���Ǹ� �����Ͽ� �����ϱ� ���� map�� �̿�
// map�� value�� �̾Ƽ� ����ϸ� ��.



#include <string>
#include <vector>
#include <map>
// 1. map�̶�
// Key, Value ���� �����͸� ���� binary tree�� �����ϴ� �ڷᱸ���Դϴ�.
// * 2�� Ʈ�� ������ Red-Black Tree�� ���
// 2. map�� ����ϴ� ���
// 1) �Է��ϴ� �ڷḦ �����ؾ� �� ��
//  2) ���� �ڷḦ �����ϰ�, �˻��� ����� �� ��
//  3) ����ϰ� ����, �������� ���� ��
//    - ����, ���� �� �ڵ� ������ �߻��Ͽ� �ӵ��� ������
// 3. map�� �ٽɱ��
// 3. map�� �ٽ� ���
/*  1) find
    (1) map�� key�� �ִٸ� vectoró�� Random access�� ����
    (2) iterator�� ����Ͽ� ���������� �˻��� ����
  2) Insert
    (1) map�� �ڷḦ ���� �� ���ο��� �ڵ����� Key �������� �������� ����(�⺻ ����)�� �ϰ� ������ ��
    (2) std::map�� ���Ҵ� std::pair ��ü�� �����
    (3) key �ߺ��� ������� ����
    (4) ���� �߿� �������� ũ�Ⱑ Ȯ���
  3) erase
    (1) Random access �Ͽ� ������ ���� */



#include <iostream>

using namespace std;
// ��� 1
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
//���2 ����� ���� �����Ͽ� ��� ���ϰ�, ���Դ� ��� -1�ϱ�.
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