# 문제 링크 : https://programmers.co.kr/learn/courses/30/lessons/60060?language=python3
# 풀이 기록 : https://velog.io/@hong_journey/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EA%B0%80%EC%82%AC-%EA%B2%80%EC%83%89
"""
# 효율성 오류난 코드
def left_start(query):
    # 접미사에 ? 가 있을 때, 시작하는 index
    start = 0
    end = len(query)-1
    while start <= end:
        mid = (start+end)//2
        if query[mid] == '?' and query[mid-1] != '?':
            return mid
        elif '?' in query[:mid]:
            end = mid - 1
        else: 
            start = mid + 1

def right_end(query):
    # 접두사에 ? 가 있을 때, 끝나는 index
    start = 0
    end = len(query)-1
    while start <= end:
        mid = (start+end) // 2
        if query[mid] == '?' and query[mid+1] != '?':
            return mid
        elif '?' in query[mid+1:]:
            start = mid + 1
        else:
            end = mid -1
    return mid

def solution(words, queries):
    answer = []
    for query in queries:
        query_len = len(query)
        if query.count('?') == query_len: # 전체 '?'인 경우
            match_count = 0
            for word in words:
                if len(word)==query_len:
                    match_count += 1
                    
        elif query[-1] == '?': # 접미사에 '?'인 경우
            match_count = 0
            for word in words:
                if len(word) != query_len:
                    continue
                start_index = left_start(query)    
                if word[:start_index] == query[:start_index]:
                    match_count += 1
                        
        else: # 접두사에 '?'인 경우
            match_count = 0
            for word in words:
                if len(word) != query_len:
                    continue
                end_index = right_end(query)
                if word[end_index+1:] == query[end_index+1:]:
                    match_count += 1
        answer.append(match_count)
    
    return answer
"""

from bisect import bisect_left, bisect_right


def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)

    return right_index - left_index


# 모든 단어를 길이마다 나누어서 저장하기 위한 리스트
array = [[] for _ in range(10001)]
# 모든 단어를 길이마다 나누어서 뒤집어 저장하기 위한 리스트
reversed_array = [[] for _ in range(10001)]


def solution(words, queries):
    answer = []
    for word in words:
        array[len(word)].append(word)
        reversed_array[len(word)].append(word[::-1])

    for i in range(10001):  # 이진 탐색을 수행하기 위해 각 단어 리스트 정렬 수행
        array[i].sort()
        reversed_array[i].sort()

    for q in queries:
        if q[0] != "?":  # 접미사에 ? 가 존재, 전체가 ? 인 경우도 제외
            res = count_by_range(
                array[len(q)], q.replace("?", "a"), q.replace("?", "z")
            )
        else:  # 접두사에 ? 가 존재 + 전체가 ? 인 경우
            res = count_by_range(
                reversed_array[len(q)],
                q[::-1].replace("?", "a"),
                q[::-1].replace("?", "z"),
            )
        answer.append(res)
    return answer
