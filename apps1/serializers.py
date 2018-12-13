from rest_framework import serializers
from .models import xu222

class xu222Serializer(serializers.ModelSerializer):
    class Meta:
        model = xu222
        fields = "__all__"

