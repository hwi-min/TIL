capacity = 30  # 배낭의 최대 무게
items = [(5, 50), (10, 60), (20, 140)] # (무게, 가치)
result = fractional_knapsack_greedy(capacity, items)
print(f"최대 가치: {result}")