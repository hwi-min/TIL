# 클래스 정의
class Person:
    blood_color = 'red'
    def __init__(self, name): # 
        self.name = name
    def singing(self):
        return f'{self.name}가 노래합니다.'


# 인스턴스 생성
singer1 = Person('iu')
# 메서드 호출
print(singer1.singing())  
# 속성(변수) 접근
print(singer1.blood_color)

# Person 언급 동시에 instance 생성
# -> 넘겨 받은 'iu'라는 변수를 name(인스턴스 변수)에 할당하여 본인 만의 속성을 가짐
# + singing이라고 하는 method도 가진 상태로 생성이 됨
# 만들어 진 이 인스턴스를 singer1이라는 변수에 할당