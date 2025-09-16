def check_match(expression):
    # 여는 괄호들을 일단 담아둘 스택
    stack = []
    matching_dict = {
        ')': '(',
        '}':'{',
        ']':'['
    }

    # 괄호의 짝을 매칭시킬 수 있어야 할 것
    for char in expression:
        if char in matching_dict.values():
            stack.append(char)
        elif char in matching_dict.keys():
            if not stack or stack[-1] != matching_dict[char]:
                return False
            stack.pop()

# 예시
examples = ["(a(b)", "a(b)c)", "a{b(c[d]e}f)"]
for ex in examples:
    if check_match(ex): 
        print(f"{ex} 는 올바른 괄호") 
    else:
        print(f"{ex} 는 올바르지 않은 괄호")