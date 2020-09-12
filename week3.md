>참고자료1:<https://github.com/encode/django-rest-framework>
>참고자료2:<https://www.django-rest-framework.org/tutorial/3-class-based-views/>

8강 mixins
===
어떻게 하면 코드 낭비를 줄일 수 있을까??  
상속을 하면 된다!!
이러한 관점에서 mixins를 알아보자.  

List View
---
```python
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
#주목!!!
from rest_framework import mixins
from rest_framework import generics

#상속하는 방법
class SnippetList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    #등록(generics.GenericAPIView 안에서 선언된 변수임)
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    #필요로 하는 메서드
    #가변인자 사용(인자의 개수에 상관없이 받음)
    def get(self, request, *args, **kwargs):
        #list는 ListModelMixin에서 이미 정의된 메서드
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        #create는 CreateModelMixin에서 이미 정의된 메서드
        return self.create(request, *args, **kwargs)
```
>Detail View도 비슷한 형식

9강 generic CBV
===
mixins 안에서도 불필요한 코드 제거함으로 더욱 간단한 코드 만들기
```python 
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework import generics

#상속을 통해 메서드 정의하는 불필요한 코드를 생략한다.
#위 코드의 .list .create를 묶어놓은 클래스
class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
```
>Detail도 동일

10강 ViewSet
===
정의된 클래스 4개 있음. 그 중 2개에 대해서만 알아보자.
```python 
#retrieve, list 메서드를 묶어주는 역할
#특정 레코드를 읽을 수 있게 도와준다.
class ReadOnlyModelViewSet(mixins.RetrieveModelMixin,
                           mixins.ListModelMixin,
                           GenericViewSet):
    pass

class ModelViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    pass
```
ViewSet을 쓰면 CRUD가 두 줄로 끝난다.   
그러면 다른 Logic들을 어떻게 사용하지?  
ModelViewSet을 상속해서
@action을 통해 view를 설계할 수 있다!  

```python 
from rest_framework.decorators import action
from rest_framework.response import Response

class SnippetViewSet(viewsets.ModelViewSet):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    #response를 어떤 형식으로 rendering 시킬 것인가
    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        #직접 Response()를 리턴한다.
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
```
디폴트값은 GET방식이다.

11강 Router
===
ViewSet을 하나의 path함수로 처리 가능할까?  
불가능하다.  
즉, 여러 path함수를 묶어야 한다. == path함수의 두번째인자로 묶는다. 
어떻게??  
as_view()를 사용한다.  

```python
mypath = PostViewSet.as_view({'http_method':'처리할 함수'})

urlpatterns = [
    path('', mypath)
]
```
하지만... 이런 매핑관계를 만드는게 귀찮다.  
그래서 간단하게 **routers**를 쓰는거다!  

12강 pagination
===
1. 왜 사용하는가?  
하나의 request만으로 처리하기 어려운 레코드들을 여러 request로 나누어 전송하려고.  

2. 구현방법
DRF 제공 클래스 4가지가 있는데,  
PageNumberPagination(default), CustomizedPagination 두가지가 많이 쓰인다. 

>참고자료: <https://www.django-rest-framework.org/api-guide/pagination/>

1) PageNumberPagination
---
rest_framework의 settings.py 내용
```python
'DEFAULT_PAGINATION_CLASS': None,
'PAGE_SIZE': None,
```
나의 프로젝트의 settings.py 맨 아래에 추가한다. 
```python 
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 4
}
```
!!반드시 레코드를 정렬한 후, 페이지네이션을 할 것!!  
```python
queryset = Post.objects.all().order_by('id')
```

2) CustomizedPagination
---
pagiantion.py 파일 새로 만들기

13강 filtering and search
===
filtering | search
--------- | ------
request 걸러보내기 | response 걸러받기

```python
#관리자 만들기
python manage.py createsuperuser
```