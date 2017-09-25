from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from battles.models import BattleSet
import json


# Create your views here.

@api_view(['GET'])
def battle_details(request):

    battle_list = []
    success = True
    query = request.GET.get('q')
    print("query ", query)
    print("Check  ", BattleSet.objects.filter(name=query).exists())
    if query:
        if BattleSet.objects.filter(name=query).exists():
            battle_list = BattleSet.objects.filter(name=query).values()            
        else:
            success = False
    
    return Response({"result": battle_list, "success": success})

