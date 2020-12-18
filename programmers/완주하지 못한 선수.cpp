#include <string>
// std:string�� ���ڿ��� ��µ� ������ Ŭ�����̴�.
// ���������� ����� �� �ֵ��� ���´�.
// strlen : a.size() �Ǵ� a.length()
// strcpy : a = b
// strcmp : a == b
#include <vector> 
// vector ������� �߰�
// �������� ���Ҹ� �߰��� �� ������ ũ�Ⱑ �ڵ����� �þ.
#include <iostream>
// #include <string> ����Ǿ� ����.
#include <algorithm>
// ���ҵ鿡 ���� �۾��� �� �ִ� ���� ���� �Լ�(�˻�, ����, ���ҵ� ������, ���� ���� ���)�� ������.

using namespace std;

string solution(vector<string> participant, vector<string> completion) {
    // ����ִ� ���� ����
    std::sort(participant.begin(), participant.end());
    std::sort(completion.begin(), completion.end());

    int num = 0;

    for (int i = 0; i < participant.size(); i++) {
        // size() : container�� �ִ� ������ ��
        if (participant[i] != completion[i]) {
            return participant[i];
        }
    }

    return participant[participant.size()];
}