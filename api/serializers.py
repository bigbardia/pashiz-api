from rest_framework import serializers
from .models import Koochooloo

class KoochoolooSerializer(serializers.ModelSerializer):

    class Meta:
        model = Koochooloo
        fields = "__all__"
        read_only_fields = ("name",)


