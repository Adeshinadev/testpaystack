from django.shortcuts import render
from rest_framework.response import Response

# Create your views here.
from rest_framework.views import APIView
from .models import PaystackData, Client as MyClient
from .serializers import PaystackDataSerializer, MyClientSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class PayStackRequest(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = PaystackDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': True, **serializer.data})
        else:
            return Response({'status': False, 'errors': serializer.errors})


class Client(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = MyClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': True, **serializer.data})
        else:
            return Response({'status': False, 'errors': serializer.errors})
