"""
입력 조건 
- 스테이지 개수 N, (1<=N<=500)
- 게임을 이용하는 사용자가 현재 멈춰있는 스테이지의 번호가 담긴 배열 stages (길이는 1이상 200,000 이하)
- 단, N+1 은 마지막 스테이지(N번째 스테이지)까지 클리어한 사용자를 나타냄. 

출력 조건
- 실패율 = 스테이지에 도달했으나 아직 클리어하지 못한 플레이어 수/스테이지에 도달한 플레이어 수
- 스테이지에 도달한 플레이어 수가 없는 경우, 해당 스테이지의 실패율은 0으로 정의. 
- 실패율이 높은 스테이지 순으로 스테이지 번호 배열을 출력.
"""

def solution(N, stages):
    location = [0]*(N+2)
    for i in range(len(stages)):
        location[stages[i]] += 1

    players = [0]*(N+2) # stage 별 도달한 플레이어 수 리스트
    player = location[N+1] # stage 별 클리어한 플레이어 수 
    for i in range(N,0,-1):
        player += location[i]
        players[i] = player

    failures = []
    for i in range(1, N+1):
        if players[i] != 0:
            failure_rate = location[i]/players[i]
        else:
            failure_rate = 0
        failures.append((i, failure_rate))


    failures.sort(key=lambda x: -x[1])
    answer = [x[0] for x in failures]
    return answer
"""
- 0으로 나누는 경우 고려 안 해서 런타임 오류났었음. 
- 나는 계수 정렬 위해 리스트를 만든 다음, 스테이지에 도달한 총 플레이어 수를 스테이지마다 누적해서 계산했는데
- len([x for x in stages if x>=i]) 으로 i번째 스테이지에 도달한 총 플레이어 수를 계산할 수도 있다. (리스트 길이 이용)
- i번째 스테이지에 도달한 사람 수 세는 과정은 stages.count(i)으로 대체 가능
- 위처럼 N부터 0까지 player를 계산하지 않고 1번부터 N번까지 계산했다면 분모가 0이 되는 일도 없었을 것.
"""