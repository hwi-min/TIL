class ParentA:
    # 단어를 드래그하거나 포커싱을 한다음
    # ctrl + D를 하면 (주의. 대소문자 구분)
    # alt + 방향키로 줄 바꿈
    # alt shif + 위아래로 복제
    # ctrl + 좌우: 단어 단위로 커서 이동
    # ctrl + shif + 좌우: 단어 단위로 드래그
    # ctrl + shift + home/end: 왼쪽 끝으로 드래그 / 오른쪽으로 드래그
    # ctrl + k  // ctrl + s : VSCode shortcut 설정
    def __init__(self):
        self.value_a = 'ParentA'
    def show_value(self):
        print(f'Value from ParentA: {self.value_a}')

class ParentB:
    def __init__(self):
        self.value_b = 'ParentB'
    def show_value(self):
        print(f'Value from ParentB: {self.value_b}')

class Child(ParentA, ParentB):
    def __init__(self):
        # super().init() # ParentA 클래스의 init 메서드 호출
        self.value_c = 'Child'
    def show_value(self):
        super().show_value() # ParentA 클래스의 show_value 메서드 호출
        print(f'Value from Child: {self.value_c}')

child = Child()
child.show_value()  # 오류 발생 이유 child에서 생성자를 다시 생성했으니까 value_c만 남아있음