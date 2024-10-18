# data_handler/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from accounts.models import Account
from destinations.models import Destination
import requests
from urllib.parse import urlencode

class DataHandlerView(APIView):
    def post(self, request):
        app_secret_token = request.headers.get('CL-X-TOKEN')
        
        if not app_secret_token:
            return Response({"error": "Un Authenticate"}, status=status.HTTP_401_UNAUTHORIZED)
        
        if not request.data or not isinstance(request.data, dict):
            return Response({"error": "Invalid Data"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            account = Account.objects.get(app_secret_token=app_secret_token)
        except Account.DoesNotExist:
            return Response({"error": "Invalid app secret token"}, status=status.HTTP_401_UNAUTHORIZED)
        
        destinations = Destination.objects.filter(account=account)
        
        for destination in destinations:
            if destination.http_method == 'GET':
                url = f"{destination.url}?{urlencode(request.data)}"
                response = requests.get(url, headers=destination.headers)
            else:
                response = requests.request(
                    method=destination.http_method,
                    url=destination.url,
                    json=request.data,
                    headers=destination.headers
                )
            
            # You might want to log the response or handle errors here
        
        return Response({"message": "Data sent to all destinations"}, status=status.HTTP_200_OK)