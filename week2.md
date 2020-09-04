4강 REST Architecture
===
REST란?
---
REpresentational State Transfer의 약자
- 네트워크 통신 방법
- 자원을 이름으로 구분하여 상태를 전송하는 방법

API란?
---
Application Program Interface의 약자
- request, response로 오가는 구조화된 데이터

REST API란?
---
- REST 아키텍쳐 스타일을 따르는 API
- HTTP(GET/POST)로 CRUD를 구현할 수 있는 API
> 요즘 API는 json을 사용하기에 REST 조건을 잘 지키지 못한다. (예:django REST Framework)

5-1강 JSON 직렬화
===
![표](/폼모델폼.png)
![Form vs Serializer](/폼2.png)

5-2강 Serializer 실습
===
1. 가상환경 생성
2. djangorestframework, django 설치
3. 프로젝트, 앱 생성
4. rest_framework, 앱을 settings.py의 INSTALLED_APPS에 등록
5. 등등....

7강 APIView
===
views.py 
---
- 인자로 쓰이는 APIView 불러오기
- rest_framework에서 response, status 불러오기
- 내가 필요로 하는 http 메서드 만들기

1. SnippetList 클래스 이해하기
**get 메서드**
**post 메서드**

2. SnippetDetail 클래스 이해하기
**get_object 메서드** :404 페이지 구현하기 위함
**get 메서드**
**put 메서드**
**delete 메서드** 

urls.py
---
views.클래스.as_view()

