from django.shortcuts import render
import re
from django.http import HttpResponse
from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Weather,ReportData, CrisisState
from .Serializers import WeatherSerializer,ReportDataSerializer, CrisisStateSerializer
from rest_framework.settings import api_settings
from sendsms import api
from django.views.decorators.csrf import csrf_exempt
from sendsms.message import SmsMessage
from twilio.rest import Client
# Create your views here.

class WeatherViewSet(viewsets.ModelViewSet):
    queryset = Weather.objects.all()
    serializer_class = WeatherSerializer

    def get_queryset(self):
        return Weather.objects.filter(weatherData="a")

class CrisisStateViewSet(viewsets.ModelViewSet):
    queryset = CrisisState.objects.all()
    serializer_class = CrisisStateSerializer

    def list(self, request, *args, **kwargs):
        try:
            queryset = CrisisState.objects.order_by('-id')[0]
            serializer = CrisisStateSerializer(queryset)
            return Response(serializer.data)
        except Exception as e:
            queryset = CrisisState.objects.all()
            serializer = CrisisStateSerializer(queryset,many=True)
            return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        print("Request Headers: ")
        printRequestHeader(request)
        print("Request Data: ")
        print(request.data)
        return super(CrisisStateViewSet,self).create(request)

class ReportDataViewSet(viewsets.ModelViewSet):
    queryset = ReportData.objects.all()
    serializer_class = ReportDataSerializer

    def list(self, request, *args, **kwargs):
        print("Request Headers: ")
        printRequestHeader(request)
        # print("Request Data: " + request.data)
        queryset = ReportData.objects.all()
        serializer = ReportDataSerializer(queryset,many=True)
        return Response(serializer.data)#,headers={"Access-Control-Allow-Origin":"*"})

    def retrieve(self, request, *args, **kwargs):
        try:
            parameter = int(self.kwargs['pk'])
            return super(ReportDataViewSet, self).retrieve(request, *args, **kwargs)
        except Exception as e:
            print(self.kwargs['pk'])
            parameter = self.kwargs['pk'].split('=')
            retrieveType = parameter[0]
            retrieveData = parameter[1]
            if (retrieveType == 'crisisType'):
                queryset = ReportData.objects.filter(crisisType=retrieveData)
                serializer = ReportDataSerializer(queryset, many=True)
                return Response(serializer.data)  # ,headers={"Access-Control-Allow-Origin":"*"})
            elif (retrieveType == 'verified'):
                queryset = ReportData.objects.filter(verified=retrieveData)
                serializer = ReportDataSerializer(queryset, many=True)
                return Response(serializer.data)  # ,headers={"Access-Control-Allow-Origin":"*"})


    def create(self, request, *args, **kwargs):
        print("Request Headers: ")
        printRequestHeader(request)
        print("Request Data: ")
        print(request.data)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()

    def get_success_headers(self, data):
        try:
            return {'Location': data[api_settings.URL_FIELD_NAME]}
        except (TypeError, KeyError):
            return {}

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()

    def update(self, request, *args, **kwargs):
        print("Request Headers: ")
        printRequestHeader(request)
        print("Request Data: ")
        print(request.data)
        response = super(ReportDataViewSet,self).update(request)
        if(response):
            if(request.data.has_key('verified') and request.data['verified']) and request.data.has_key('assistanceType') and request.data['assistanceType'] != None:
                sendSMS(request,"SCDF")
        return response
    # def update(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     print(instance)
    #     instance.crisisState = request.data.get("crisisState")
    #     instance.save()
    #
    #     serializer = self.get_serializer(instance)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_update(serializer)
    #
    #     return Response(serializer.data)

# class WeatherAPI(APIView):
#     def post(self,request):
#         queryset = Weather.objects.all()
#         serializer = WeatherSerializer(queryset,many=True)
#         return Response(serializer.data)
#
#     def get(self,request):
#         queryset = Weather.objects.all()
#         serializer = WeatherSerializer(queryset,many=True)
#         return Response(serializer.data)

def index(request):
    return HttpResponse("This is CMS Backend Service!!!")

@csrf_exempt
def sendSMS(request,number):
    print("Preparing Message To Send!!!")
    message = None
    if(request.method == "POST" or request.method == "PUT"):
        account = "ACa64c99246f5b583d0bc928b2c5c60c50"
        token = "9a84195984dcec9432c6c0dc87177e11"
        client = Client(account, token)
        numberToSend = '+6584016409'
        if(number == "SCDF"):
            numberToSend = '+6584016409'
        client.messages.create(
            to=numberToSend,
            from_='+13345398798',
            body=request.data['assistanceType'].upper()+ " at " + request.data['location'].upper() + " Need Assistance!!!",
        )
    print("Message Sent Successful!")
    return HttpResponse('Message Sent Successful!')

def printRequestHeader(request):
    regex = re.compile('^HTTP_')
    headers = dict((regex.sub('', header), value) for (header, value)
         in request.META.items() if header.startswith('HTTP_'))
    # headers = dict((header, value) for (header, value)
    #                in request.META.items() if header.startswith('HTTP_'))
    print(headers)
