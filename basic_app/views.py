from rest_framework import generics

from basic_app import serializers, inspectDB_models


# Create your views here.
class ListAnketa(generics.ListCreateAPIView):
    queryset = inspectDB_models.Anketa.objects.all()
    serializer_class = serializers.AnketaSerializers


class DetailAnketa(generics.RetrieveUpdateDestroyAPIView):
    queryset = inspectDB_models.Anketa.objects.all()
    serializer_class = serializers.AnketaSerializers


class ListUsers(generics.ListCreateAPIView):
    queryset = inspectDB_models.Anketa.objects.all()
    serializer_class = serializers.UsersSerializers


class DetailUsers(generics.RetrieveUpdateDestroyAPIView):
    queryset = inspectDB_models.Anketa.objects.all()
    serializer_class = serializers.UsersSerializers


class List_Elon_Shogird(generics.ListCreateAPIView):
    queryset = inspectDB_models.ElonShogird.objects.all()
    serializer_class = serializers.Elon_ShgirdSerializer


class Detail_Elon_Shogird(generics.RetrieveUpdateDestroyAPIView):
    queryset = inspectDB_models.ElonShogird.objects.all()
    serializer_class = serializers.Elon_ShgirdSerializer
