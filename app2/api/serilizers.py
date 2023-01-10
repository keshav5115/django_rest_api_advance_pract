from app2.models import Customer,Products,Review

from rest_framework import serializers

class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model=Review
        # fields='__all__'
        exclude=('product',)



class ProductSerializer(serializers.ModelSerializer):
    reviews=ReviewSerializer(many=True,read_only=True)

    class Meta:
        model=Products
        fields='__all__'


class CustomerSerial(serializers.ModelSerializer):
    # products=ProductSerializer(many=True,read_only=True)
    # products=serializers.StringRelatedField(many=True,read_only=True)
    products=serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='cone')
    class Meta:
        model=Customer
        fields='__all__'

