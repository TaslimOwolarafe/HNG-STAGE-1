from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

def index(request, *args, **kwargs):
    return JsonResponse({
            "slackUsername" : 'TaslimOwolarafe',
            'backend' : True,
            'age' : 18,
            'bio' : 'student, backend developer.' 
        })

@api_view(['POST', 'GET'])
def operationView(request, *args, **kwargs):
    response = {"slackUsername" : 'TaslimOwolarafe'}
    print(request.data)
    if request.method == 'POST':
        operation = request.data.get('operation_type')
        x = int(request.data.get('x'))
        y = int(request.data.get('y'))
        result = None
        if operation == 'addition':
            result = x + y
        elif operation == 'subtraction':
            result = x - y
        elif operation == 'multiplication':
            result = x * y
        
        response = {
            "slackUsername" : 'TaslimOwolarafe',
            "result" : result,
            "operation_type" : operation
        }
    return Response(response)
