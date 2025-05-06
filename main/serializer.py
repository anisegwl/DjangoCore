from rest_framework.serializers import ModelSerializer

from .models import Questions

class QuestionModelSerializer(ModelSerializer):
    class Meta:
        model = Questions
        fields ='__all__'

