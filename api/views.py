from api.models import Koochooloo
from .serializers import KoochoolooSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist





@api_view(["GET"])
def get_all(request):

    queryset = Koochooloo.objects.all()
    data = KoochoolooSerializer(queryset , many=True)
    return Response(data.data)


@api_view(["GET"])
def get_instance(request , name):

    try:
        instance = Koochooloo.objects.get(name = name)
    except ObjectDoesNotExist:
        return Response({} , status=404)
    
    serialized_ins = KoochoolooSerializer(instance)
    return Response(serialized_ins.data)

@api_view(["POST"])
def add_pashiz(request , name , num):
    
    if request.data.get("token" , False) == "12345":

        try:
            instance = Koochooloo.objects.get(name=name)
        except ObjectDoesNotExist:
            return Response(status=404)
        
        instance.pashiz += float(num)
        instance.save()
        return Response(KoochoolooSerializer(instance).data)

    return Response({} , status=403)

@api_view(["POST"])
def subtract_pashiz(request , name , num):

    if request.data.get("token" , False) == "12345":

        try:
            instance = Koochooloo.objects.get(name=  name)
        except ObjectDoesNotExist:
            return Response(status=404)

        instance.pashiz -= float(num)
        instance.save()
        return Response(KoochoolooSerializer(instance).data)

    return Response({} , status=403)

@api_view(["POST"])
def set_pashiz(request , name , num):
    


    if request.data.get("token" , False) == "12345":

        try:
            instance = Koochooloo.objects.get(name=name)
        except ObjectDoesNotExist:
            Response({} , status=404)

        instance.pashiz = float(num)
        instance.save()
        return Response(KoochoolooSerializer(instance).data)

    return Response({} , status=403)
