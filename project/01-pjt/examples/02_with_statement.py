import sys
print(sys.getdefaultencoding())

# open 함수를 사용하는 방법은 open(filename, mode, encoding)
data = open('./example.txt', 'r')
# print(data) # encoding 정보를 주지 않으면, 해당 파일의 인코딩 방식을 따라감
print(data.read()) # 정보를 들고와서 출력
data.close()

'''
with 표현식 as 변수: alias (별칭) 표현식의 결과값을 변수에 할당
    코드 블럭
with문 종료시, 리소서 해제
'''
with open('example.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    print(content)
print(file.read()) # with는 따로 close 해 줄 필요가 없다.
