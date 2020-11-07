from rest_framework import serializers
from articles.models import article
class Articleserializer(serializers.ModelSerializer):
    class Meta:
        model=article
        fields =('id','title','content','description')