from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

import os
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def get_operation_value(text):
    response = openai.Completion.create(
    model="text-davinci-002",
    prompt=f"Can you please add the following numbers together - 13 and 25: addition\ncan you subtract 4 from 5: subtraction\ncan you add 4 and 5: addition\ncan you multiply 5 and 6: multiplication\nCan you please multiply the following numbers together - 13 and 25: multiplication\nCan you please add the following numbers together - 13 and 34: addition\n{text}: ",
    temperature=0.7,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
    return response["choices"][0]['text'][1::].split()[0]

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
    if request.method == 'POST':
        
        operation = request.data.get('operation_type')
        x = int(request.data.get('x'))
        y = int(request.data.get('y'))
        result = None
        operation_type = get_operation_value(operation)
        if operation_type == 'addition':
            result = x + y
        elif operation_type == 'subtraction':
            result = x - y
        elif operation_type == 'multiplication':
            result = x * y
        
        response = {
            "slackUsername" : 'TaslimOwolarafe',
            "result" : result,
            "operation_type" : operation_type
        }
    return Response(response)
