from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class TestView(APIView):

    def post(self, request):
        return Response({"This is a Test API"}, status=status.HTTP_200_OK)