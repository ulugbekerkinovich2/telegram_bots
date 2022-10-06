from rest_framework import serializers

from basic_app import inspectDB_models


class AnketaSerializers(serializers.ModelSerializer):
    class Meta:
        model = inspectDB_models.Anketa
        fields = "__all__"


class UsersSerializers(serializers.ModelSerializer):
    class Meta:
        model = inspectDB_models.Users
        fields = "__all__"


class Elon_ShgirdSerializer(serializers.ModelSerializer):
    class Meta:
        model = inspectDB_models.ElonShogird
        fields = "__all__"
