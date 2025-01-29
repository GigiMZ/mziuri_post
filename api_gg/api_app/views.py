import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def index(request):
    api_key = "4c64c2eb3e904a29ad4122526252201"
    endpoint = "https://www.weatherapi.com/v1"

    r = requests.post(f'{endpoint}/current.json?key={api_key}')
    # for i, j in request.META.items():
    #     print(f'{i} v:{j}')
    if request.method == 'GET':
        return Response({"message": "Hello World!"})
    elif request.method == 'POST':
        return Response({"message": "created!"})
    elif request.method == 'PUT':
        return Response({"message": "updated!"})
    elif request.method == 'DELETE':
        return Response({"message": "Hello World!"})

    return Response({'message': 'else'})