from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from card.serializer import (
    CreateFlashCardSerilizer, 
    UpdateFlashCardSerilizer,
    ListFlashCardSerilizer
)
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404, get_list_or_404
from . models import FlashCard


class FlashCardGenericView(generics.ListCreateAPIView):
    queryset = FlashCard.objects.all()
    serializer_class = ListFlashCardSerilizer



class FlashCardDetailGenericView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FlashCard.objects.all()
    serializer_class= ListFlashCardSerilizer
    
    
    



# class CreateFlashCardView(APIView):
#     permission_classes=(IsAuthenticated,)
#     def post(self, request):
#         serilizer = CreateFlashCardSerilizer(data=request.data)
#         serilizer.is_valid(raise_exception=True)
#         serilizer.save()
        
#         return Response(serilizer.data,status=status.HTTP_201_CREATED)
        
        


# class UpdateFlashCardView(APIView):
#     permission_classes=(IsAuthenticated,)
#     def put(self, request, id):
#         flash_card = get_object_or_404(FlashCard, id=id)
#         serilizer = UpdateFlashCardSerilizer(data=request.data, instance=flash_card)
#         serilizer.is_valid(raise_exception=True)
#         serilizer.save()
        
#         return Response(serilizer.data,status=status.HTTP_200_OK)
        
        
        
        

# class DeleteFlashCardView(APIView):
#     permission_classes=(IsAuthenticated,)
#     def delete(self, request, id):
#         flash_card = get_object_or_404(FlashCard, id=id)
#         flash_card.delete()
        
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
    
    
# class ListFlashCardView(APIView):
#     permission_classes=(IsAuthenticated,)
#     def get(self, request, user_id):
#         all_user_flash_cards = get_list_or_404(FlashCard, user__id=user_id)
#         serilizer = ListFlashCardSerilizer(all_user_flash_cards, many=True)
        
#         return Response(serilizer.data)
            
    