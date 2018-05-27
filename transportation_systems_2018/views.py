from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET',])
def baseView(request):
    content = {'please move along': 'nothing to see here'}
    return Response(content, status=status.HTTP_200_OK)
