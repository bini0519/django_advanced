class1
===
json이란?
---
- 데이터 송수신을 할 때 사용함
- 자바스크립트의 객체 
- 문자열 데이터 표현식
- 송신할 때, 파이썬 형식의 문자열로 보낸다 (직렬화한다)

json.dumps(딕셔너리) -> String 형태가 된다.
json.loads(json형식) -> 딕셔너리형이 된다.

class2
===
request method 종류
---
1. GET
- 요청받은 url 정보를 검색하여 응답한다.
예) 글 목록을 갖다줘
2. POST
- 요청된 자원을 생성한다.
예) 새 글을 작성할래
3. PUT(PATCH)
예) 글을 이렇게 수정해줘
4. DELETE
예) 글을 삭제해줘

Httpie
===
설치하기
---
pip install --upgrade httpie

사용법
---
```python
http [flags] [method] URL [ITEM[ITEM]]
```
예) http --json POST 대상주소 GET인자==값 POST인자=값

class3- CBV
===

CBV 목적
---
(함수 : 상속 불가, 클래스 : 상속 가능)
->상속 가능하게 하기 위해 views.py를 클래스로 작성함.

파일별 기능
---
- models.py : 모델 만들기
- admin.py : 모델 등록
- 앱 안에 있는 urls.py
    클래스 이름.as_view()
- views.py
    django.view.generic.list 등 import해서 사용한다.