from kafka import KafkaProducer

# KafkaProducer 생성
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',          # Kafka 브로커 주소 (기본 포트: 9092)
    value_serializer=lambda v: v.encode('utf-8') # 메시지를 UTF-8로 직렬화(바이트 변환)
)

# 5개의 메시지를 순차적으로 전송
for i in range(5):
    message = f"hello kafka {i}"                 # 전송할 메시지
    producer.send('test-topic1', message)         # 'test-topic' 토픽으로 메시지 전송
    print(f"Sent: {message}")                    # 전송 로그 출력

# 전송되지 않은 메시지를 모두 전송 후 리소스 정리
producer.flush()                                 # 버퍼에 남은 메시지를 즉시 전송
producer.close()                                 # Producer 종료


"""
tc 50개 -> 6초
"""
import sys
# sys.stdin = open('test_code.txt')

T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    nums = list(map(int, input().split()))
    max_sum = float('-inf')

    # 모든 K-sum 배열 만들기 >> O(N)
    k_sums = []

    current_sum = sum(nums[:K]) # 초기 값 세팅
    k_sums.append(current_sum)

    # (N-K)번 반복
    for i in range(1, N-K+1):
        current_sum = current_sum - nums[i-1] + nums[i+K-1]
        k_sums.append(current_sum)

    # 겹치지 않는 두 K-sum의 최대 합 찾기 >> O(N^2)
    for j in range(len(k_sums)- K): 
        for l in range(j+K, len(k_sums)): # 요소가 하나라도 안겹치려면 -> 인덱스가 k개 차이나야함
            paired_sum = k_sums[j] + k_sums[l]
            if max_sum < paired_sum: 
                max_sum = paired_sum

    print(f"#{t} {max_sum}")