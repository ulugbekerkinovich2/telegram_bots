from rest_framework import generics

from basic_app import serializers, nextSmodel


# Create your views here.
class ListAnketa(generics.ListCreateAPIView):
    queryset = nextSmodel.Anketa.objects.all()
    serializer_class = serializers.AnketaSerializers


class DetailAnketa(generics.RetrieveUpdateDestroyAPIView):
    queryset = nextSmodel.Anketa.objects.all()
    serializer_class = serializers.AnketaSerializers


class ListUsers(generics.ListCreateAPIView):
    queryset = nextSmodel.Anketa.objects.all()
    serializer_class = serializers.UsersSerializers


class DetailUsers(generics.RetrieveUpdateDestroyAPIView):
    queryset = nextSmodel.Anketa.objects.all()
    serializer_class = serializers.UsersSerializers


class List_Elon_Shogird(generics.ListCreateAPIView):
    queryset = nextSmodel.ElonShogird.objects.all()
    serializer_class = serializers.Elon_ShgirdSerializer


class Detail_Elon_Shogird(generics.RetrieveUpdateDestroyAPIView):
    queryset = nextSmodel.ElonShogird.objects.all()
    serializer_class = serializers.Elon_ShgirdSerializer


class List_Elon_Sheirk(generics.ListCreateAPIView):
    queryset = nextSmodel.ElonSherik.objects.all()
    serializer_class = serializers.Elon_SherikSerializer


class Detail_Elon_Sherik(generics.RetrieveUpdateDestroyAPIView):
    queryset = nextSmodel.ElonSherik.objects.all()
    serializer_class = serializers.Elon_SherikSerializer


class List_Elon_Ish_Joyi(generics.ListCreateAPIView):
    queryset = nextSmodel.ElonIshJoyiKerak.objects.all()
    serializer_class = serializers.Elon_Ish_joyi_Serializer


class Detail_Elon_ish_joyi(generics.RetrieveUpdateDestroyAPIView):
    queryset = nextSmodel.ElonIshJoyiKerak.objects.all()
    serializer_class = serializers.Elon_Ish_joyi_Serializer


class List_Elon_Hodim(generics.ListCreateAPIView):
    queryset = nextSmodel.ElonXodim.objects.all()
    serializer_class = serializers.Elon_HodimSerializer


class Detail_Elon_Hodim(generics.RetrieveUpdateDestroyAPIView):
    queryset = nextSmodel.ElonXodim.objects.all()
    serializer_class = serializers.Elon_HodimSerializer


class List_Elon_Ustoz(generics.ListCreateAPIView):
    queryset = nextSmodel.ElonUstozKerak.objects.all()
    serializer_class = serializers.Elon_UstozSerializer


class Detail_Elon_Ustoz(generics.RetrieveUpdateDestroyAPIView):
    queryset = nextSmodel.ElonUstozKerak.objects.all()
    serializer_class = serializers.Elon_UstozSerializer
