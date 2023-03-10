from django.http import HttpResponse
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions


class FirstView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        print("inininin")
        token = request.GET.get('hub.VERIFY_TOKEN')
        challenge = request.GET.get('hub.CHALLENGE')
        print(token)
        if token == "test":
            print(request.GET.get('hub.verify_token'),"token")
            # return HttpResponse(challenge)
            return Response(data=challenge,status=status.HTTP_200_OK)
        else:
            # return HttpResponse("error")
            return Response(data="", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
