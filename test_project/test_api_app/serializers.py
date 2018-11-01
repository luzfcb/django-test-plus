from rest_framework import serializers

from test_app.models import Data


class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = (
            "id",
            "name",
        )
        read_only_fields = ("id",)
