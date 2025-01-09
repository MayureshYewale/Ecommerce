from rest_framework import  serializers 
from .models import Product ,category,User ,Order,OrderItem ,Payment


class Userserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=User 
        fields='__all__'

class productserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Product
        fields='__all__'
        

class categoryserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=category
        fields="__all__"
        
        
class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

        
class orderitemsserializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=OrderItem
        fields="__all__"
        
class paymentserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'