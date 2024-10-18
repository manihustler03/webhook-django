from rest_framework import viewsets
from .models import Destination
from .serializers import DestinationSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class DestinationViewSet(viewsets.ModelViewSet):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer

    @action(detail=False, methods=['GET'])
    def by_account(self, request):
        account_id = request.query_params.get('account_id')
        if account_id:
            destinations = Destination.objects.filter(account__account_id=account_id)
            serializer = self.get_serializer(destinations, many=True)
            return Response(serializer.data)
        return Response({"error": "account_id is required"}, status=400)