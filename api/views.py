from rest_framework import generics
from .serializers import  UserSerializer
from rest_framework.permissions import AllowAny


#新規ユーザ作成
class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)



#csvの登録
from rest_framework import viewsets
from .models import Csv
from .serializers import  CsvSerializer
class CsvViewSet(viewsets.ModelViewSet):
    queryset = Csv.objects.all()
    serializer_class = CsvSerializer