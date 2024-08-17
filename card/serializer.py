from rest_framework.serializers import ModelSerializer
from card.models import FlashCard

class CreateFlashCardSerilizer(ModelSerializer):
    class Meta:
        model = FlashCard
        fields = '__all__'
        
        
class UpdateFlashCardSerilizer(ModelSerializer):
    class Meta:
        model = FlashCard
        fields = ("question", "answer")
        

class ListFlashCardSerilizer(ModelSerializer):
    class Meta:
        model = FlashCard
        fields = "__all__"