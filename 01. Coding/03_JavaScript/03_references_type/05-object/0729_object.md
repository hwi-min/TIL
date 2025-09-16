# 객체 (Object)
- 키로 구분된 데이터 집합을 저장하는 자료형
- 중괄호 ('{}')를 이용해 작성
- 중괄호 안에는 key:value 쌍으로 구성된 속성(property)를 여러개 작성 가능
- key는 문자형만 허용
- value는 모든 자료형 허용
- 단, 내가 key 값으로 공백을 가진 것이 있다면 ''을 붙여서 사용함
  ```javascript
  const user = {
    name: 'Alice',
    'key with space': true,
    greeting: function() {
      return 'hello'
    } // 함수도 객체다
  }
  ```

## method (특정한 객체가 가지고 있는 함수)
- 객체 속성에 정의된 함수
- object.method() 방식으로 호출
- 메서드는 객체를 '행동'할 수 있게 함
- 'this' 키워드를 사용해 객체에 대한 특정한 작업을 수행 할 수 있음
  - 함수나 메서드를 호출한 객체를 가리키는 키워드 (python의 self와 다름)
  - 함수 내에서 객체의 속성 및 메서드에 접근하기 위해 사용 
  ```javascript
  const obj = {
    greeting: function() {
      console.log(this)
    }
  }

  const gr = obj.greeting
  gr() // window

  obj.greting() // greeting
  ```

  - 메서드? 재사용성 때문에 만드는 거다. 이 메서드의 기능이 그와 유사한 obj2도 사용하고 싶을 수 있음. 그럼, 거의 유사하지만 살짝 다른 obj2에 함수를 정의하는게 아니라 가져와서 사용. 단점이 실수했을때 밖에 없음


## 추가 객체 문법
- 단축 속성
  - 키 이름과 값으로 쓰이는 변수의 이름이 같은 경우 단축 구문을 사용할 수 있음 