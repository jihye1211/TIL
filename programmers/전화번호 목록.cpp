#include <string>
#include <vector>
#include <algorithm>

using namespace std;

bool solution(vector<string> phone_book) {
    bool answer = true;
    sort(phone_book.begin(), phone_book.end());
    // ���� sort�� ������ ��
    for (int i = 0; i < phone_book.size() - 1; i++) {
        if (phone_book[i] == phone_book[i + 1].substr(0, phone_book[i].size())) 
            // substr�� ����Ͽ� ���ξ �ִ��� Ȯ��
            // ���ΰ� ������ "ª�� ��ȣ"�� ���̸�ŭ�� �񱳴���� "�� ��ȣ"�� ���ۺ����� ��ȣ�� ��
            // substr
            // : ���ڿ��� �Ϻθ� ������.
            //   ���ڿ��� pos ��° ���ں��� count ���� ��ŭ�� ���ڿ��� ����. ���࿡, ���ڷ� ���޵� �κ� ���ڿ��� ���̰� ���ڿ� ���� ��ٸ�, �� �̻��� ��ȯ���� �ʰ� ���ڿ��� �� ������ �����Ѵ�.
            //   ����, count �� npos�� �����Ѵٸ�, �ڵ����� pos���� ���� ���ڿ��� ������ ����
            //   pos: ù��° ������ ��ġ
            //   count: �κ� ���ڿ��� ����
            //   ���ϰ�: ���� ���ڿ����� [pos, pos + count) ������ ���ڿ��� ��ȯ
            return false;
    }
    return answer;
}
