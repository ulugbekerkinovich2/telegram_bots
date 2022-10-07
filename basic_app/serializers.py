from rest_framework import serializers

from basic_app import nextSmodel


class AnketaSerializers(serializers.ModelSerializer):
    class Meta:
        model = nextSmodel.Anketa
        fields = "__all__"


class UsersSerializers(serializers.ModelSerializer):
    class Meta:
        model = nextSmodel.Users
        fields = "__all__"


class Elon_ShgirdSerializer(serializers.ModelSerializer):
    class Meta:
        model = nextSmodel.ElonShogird
        fields = "__all__"


class Elon_SherikSerializer(serializers.ModelSerializer):
    class Meta:
        model = nextSmodel.ElonSherik
        fields = "__all__"


class Elon_Ish_joyi_Serializer(serializers.ModelSerializer):
    class Meta:
        model = nextSmodel.ElonIshJoyiKerak
        fields = "__all__"


class Elon_UstozSerializer(serializers.ModelSerializer):
    class Meta:
        model = nextSmodel.ElonUstozKerak
        fields = "__all__"


class Elon_HodimSerializer(serializers.ModelSerializer):
    class Meta:
        model = nextSmodel.ElonXodim
        fields = "__all__"
