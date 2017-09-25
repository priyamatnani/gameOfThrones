from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from battles.models import BattleSet
import json


# Create your views here.

@api_view(['GET'])
def battle_details(request):

    #battle_list = []
    success = True
    query = request.GET.get('q')
    print("query ", query)
    print("ajbvskjb ", BattleSet.objects.filter(year=query).exists())
    if query:
        if BattleSet.objects.filter(year=query).exists():
            battle_list = list(BattleSet.objects.filter(year=query))  # contains
            print(">>>>>>>>>>>>>>",battle_list)
        else:
            success = False

    return Response({"result": json.dumps(battle_list), "success": success})

