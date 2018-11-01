from rest_framework.viewsets import ModelViewSet

from test_app.models import Data
from .serializers import DataSerializer


class DataViewSet(ModelViewSet):
    queryset = Data.objects.order_by("-id")
    serializer_class = DataSerializer
