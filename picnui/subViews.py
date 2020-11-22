from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import response, decorators, permissions, status
from .serializers import RoutineSerializer
from rest_framework.response import Response
from .models import Routine
import json
import base64

#    ______________    For Testing Purpose  ______________________

@decorators.api_view(["POST"])
@decorators.permission_classes([permissions.AllowAny])
def Testing(request):

    print('Post response: ', json.loads(request.body.decode('utf-8')))

    json.loads(request.body.decode('utf-8'))

    return HttpResponse({'status': 200})

#    ______________    Recorded Video    ______________________

@decorators.api_view(["POST"])
@decorators.permission_classes([permissions.AllowAny])
def RecordedVideoEvent(request):

    # data = json.loads(request.body.decode('utf-8'))
    # video = json.loads(request.body)
    # video['file'] += '='
    # decodeVideo = base64.b64decode(video['file'])
    # print('Recorded Video Event response: ', decodeVideo)
    #
    #
    # with open("Testingvideo.txt", 'bw') as bin_file:
    #     bin_file.write(decodeVideo)


    # fh = open('testing.mp4', 'wb')
    # fh.write(base64.b64decode(video['file']))
    # fh.close()

    reqData = json.loads(request.body)
    print("Option: ", reqData['option'])
    print("File Path: ",reqData['url'])


    return HttpResponse({'status': 200})


#    ______________    Kinect Live Stream    ______________________

@decorators.api_view(["POST"])
@decorators.permission_classes([permissions.AllowAny])
def KinectLiveStreamEvent(request):

    reqData = json.loads(request.body)

    print('DATA: ',reqData)
    print("Option: ", reqData['option'])
    print("File Path: ",reqData['url'])


    return HttpResponse({'status': 200})

#    ______________    Camera Live Stream    ______________________

@decorators.api_view(["POST"])
@decorators.permission_classes([permissions.AllowAny])
def CameraLiveStreamEvent(request):

    reqData = json.loads(request.body)

    print('DATA: ',reqData)
    print("Option: ", reqData['option'])
    print("File Path: ",reqData['url'])


    return HttpResponse({'status': 200})

#    ______________    Camera Static Image    ______________________

@decorators.api_view(["POST"])
@decorators.permission_classes([permissions.AllowAny])
def CameraStaticImageEvent(request):

    reqData = json.loads(request.body)

    print('DATA: ',reqData)
    print("Option: ", reqData['option'])
    print("File Path: ",reqData['url'])


    return HttpResponse({'status': 200})


#    ______________    Static Image    ______________________

@decorators.api_view(["POST"])
@decorators.permission_classes([permissions.AllowAny])
def StaticImageEvent(request):

    reqData = json.loads(request.body)

    print('DATA: ',reqData)
    print("Option: ", reqData['option'])
    print("File Path: ",reqData['url'])


    return HttpResponse({'status': 200})

