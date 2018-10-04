from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView


def index(request):
    return render(request, 'blog/index.html')


class SampleAPIView(APIView):
    def get(self, request):
        members = '민아,혜리,유라,소진'.split(',')
        images = [f'/static/images/{member}.jpg' for member in 'hyeri,mina,sojin,yura'.split(',')]
        data = [{'name': member, 'image': image} for member, image in zip(members, images)]
        return Response(data)
