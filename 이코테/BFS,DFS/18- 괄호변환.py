"""
1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다. 
2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다. 
3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다. 
  3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다. 
4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다. 
  4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다. 
  4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다. 
  4-3. ')'를 다시 붙입니다. 
  4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다. 
  4-5. 생성된 문자열을 반환합니다.
"""


def right_word(word):
    left_count, right_count = 0, 0
    for w in word:
        if left_count < right_count:
            return False
        if w == "(":
            left_count += 1
        if w == ")":
            right_count += 1
    return True


def reverse_string(word):
    reversed_string = ""
    for w in word:
        if w == "(":
            reversed_string += ")"
        if w == ")":
            reversed_string += "("
    return reversed_string


def solution(word):
    if word == "":
        return ""

    left_count, right_count = 0, 0
    for i in range(len(word)):
        if word[i] == "(":
            left_count += 1
        if word[i] == ")":
            right_count += 1
        if left_count == right_count and left_count != 0:
            u = word[: i + 1]
            v = word[i + 1 :]
            if right_word(u):
                return u + solution(v)
            else:
                temp = "("
                temp += solution(v)
                temp += ")"
                temp += reverse_string(u[1:-1])

                return temp


"""
- 균형잡힌 괄호 문자열인지 확인하는 함수는 따로 빼거나 flag로 처리하면(올바른 괄호 문자열처럼) 코드 이해하기 쉬울 것 같다. 
- reverse_string은 ''.join(['(' if w==')' else ')' for w in word]) 으로 간단히 처리 가능
"""
