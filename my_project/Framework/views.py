from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import FrameworkModel
from .serializers import FrameworkSerializer


class FrameworkListView(ListAPIView):
    queryset = FrameworkModel.objects.all()
    serializer_class = FrameworkSerializer


class FrameworkLookupView(ListAPIView):
    queryset = FrameworkModel.objects.all()
    serializer_class = FrameworkSerializer
    lookup_field = 'language'

    def get_queryset(self):
        queryset = FrameworkModel.objects.filter(language=self.kwargs['language']).all()
        return queryset
