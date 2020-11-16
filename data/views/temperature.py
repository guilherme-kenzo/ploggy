from data.models import TemperatureData
from data.serializers.temperature import TemperatureSerializer
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from django.core.paginator import Paginator

class TemperatureViewSet(viewsets.ViewSet):
    """Viewset for listing (with filters), retrieving and creating data.
    """

    def list(self, request):
        page_n = request.GET.get('page', 1)
        paginator = Paginator(TemperatureData.objects.all(), per_page=10)
        page = paginator.get_page(page_n)
        return Response(
            [
                i.to_dict() for i in page
            ]
        )

    def retrieve(self, request, pk):
        temp_data = TemperatureData.objects.get(id=pk)
        return Response(temp_data.to_dict())

    def create(self, request):
        temp_serializer = TemperatureSerializer(data=request.data)
        if temp_serializer.is_valid():
            temp_data = TemperatureData(**temp_serializer.validated_data)
            temp_data.save()
            return Response(temp_data.to_dict())
        else:
            return Response(
                temp_serializer.error_messages, 
                status=status.HTTP_400_BAD_REQUEST
            )