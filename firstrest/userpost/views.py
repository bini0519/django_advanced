from userpost.models import UserPost
from userpost.serializer import UserSerializer
from rest_framework import viewsets
from rest_framework.filters import SearchFilter

class UserPostViewSet(viewsets.ModelViewSet):
    queryset = UserPost.objects.all()
    serializer_class = UserSerializer

    filter_backends = [SearchFilter]
    search_fields = ('title',)
    #어떤 컬럼을 기반으로 검색을 할 건지 -> 튜플

    def get_queryset(self):
        qs = super().get_queryset()

        #인증된 관리자이면
        if self.request.user.is_authenticated:

            #지금 로그인한 관리자가 쓴 글만 확인
            qs = qs.filter(author = self.request.user)
            #filter 또는 exclude 사용가능
        
        #인증된 관리자가 아니면 빈 쿼리셋 리턴
        else: 
            qs = qs.none()

        return qs