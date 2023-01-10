from rest_framework.response import Response
from rest_framework.views import  APIView
from rest_framework import status
from app2.models import Customer,Products,Review
from .serilizers import CustomerSerial,ProductSerializer,ReviewSerializer

#-------------mixins----------------------------------------------------------------
from rest_framework import mixins,generics,viewsets

# class ReviewDetailView(mixins.RetrieveModelMixin,generics.GenericAPIView):
#     queryset=Review.objects.all()
#     serializer_class=ReviewSerializer
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

# class ReviewListMixin(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):

#     queryset=Review.objects.all()
#     serializer_class=ReviewSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

#-------------------------------------------------------------------------------------
class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):

    # queryset=Review.objects.all()
    serializer_class=ReviewSerializer

    
class ReviewCreateView(generics.CreateAPIView):

    serializer_class=ReviewSerializer
    def perform_create(self, serializer):
        pk = self.kwargs['pk']
        product=Products.objects.get(id=pk)
        serializer.save(product=product)






class ReviewListMixin(generics.ListAPIView):

    queryset=Review.objects.all()
    serializer_class=ReviewSerializer

    def get_queryset(self):
        pk=self.kwargs['pk']
        return Review.objects.filter(product=pk)




class CustomerListAV(APIView):

    def get(self, request ):
        customer=Customer.objects.all()
        serializer=CustomerSerial(customer,many=True,context={'request':request})
        return Response(serializer.data)

    def post(self,request):
        serializer=CustomerSerial(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class CustomerViewDetail(APIView):

    def get(self,request,pk):
        customer=Customer.objects.get(id=pk)
        serializer=CustomerSerial(customer,context={'request':request})
        return Response(serializer.data)
    
    def put(self,request,pk):
        customer=Customer.objects.get(id=pk)
        serializer=CustomerSerial(data=request.data,instance=customer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def delete(self,request,pk):
          customer=Customer.objects.get(id=pk).delete()
          serializer=CustomerSerial(data=request.data)
          return Response(serializer.data,status=status.HTTP_204_NO_CONTENT)

    


#-------------products views----------------------

    #--------------modelviewsets----------------
class ProductModelVW(viewsets.ModelViewSet):
    queryset=Products.objects.all()
    serializer_class=ProductSerializer
    #-----------------------------------------------

# class ProductListAV(APIView):

#     def get(self, request ):
#         product=Products.objects.all()
#         serializer=ProductSerializer(product,many=True)
#         return Response(serializer.data)

#     def post(self,request):
#         serializer=ProductSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)

# class ProductViewDetail(APIView):

#     def get(self,request,pk):
#         product=Products.objects.get(id=pk)
#         serializer=ProductSerializer(product)
#         return Response(serializer.data)
    
#     def put(self,request,pk):
#         product=Products.objects.get(id=pk)
#         serializer=ProductSerializer(data=request.data,instance=product)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)
    
    def delete(self,request,pk):
          product=Products.objects.get(id=pk).delete()
          serializer=ProductSerializer(data=request.data)
          return Response(serializer.data,status=status.HTTP_204_NO_CONTENT)