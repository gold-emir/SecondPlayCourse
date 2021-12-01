from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status # http status codes
from . import serializers


class HelloApiView(APIView):
    ''' My First Api view '''
    serializer_class = serializers.HelloViewSerializer

    def get(self,request):
        '''First Api independent view'''
        an_api_features = [
            'Can do something or something'
        ]
        return Response({'message:': an_api_features})

    def post(self,request):
        '''First independent post API'''
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


    def put(self,request, pk=None):
        '''Put method '''

        return Response({'Method: ': 'Put method in this case'})

    def patch(self,request, pk=None):
        '''Patch method '''

        return Response({'Method: ': 'PATCH method in this case'})

    def delete(self,request, pk=None):
        '''Delete method '''

        return Response({'Method: ': 'Delete method in this case'})


class HelloViewset(viewsets.ViewSet):
    """Test API list method """
    serializer_class = serializers.HelloViewSerializer
    def list(self,request):
        '''Return a hello message'''
        serializer = self.serializer_class(data=request.data)
        a_viewset = [
            'uses actions (list,create,retrieve, update, partial_update)',
        ]

        return Response({'Message:': a_viewset})
#  #### #### #### #### #### #### #### #### #### #### #### #### #### ####

    def create(self,request):
        ''' Create a new hello message '''
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'Message:': message})
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,pk=None):
        """ Handle getting an object by its id"""
        return Response({'Http_method:' 'GET'})

    def update(self,request,pk=None):
        """ Handle updateing an object by its id"""
        return Response({'Http_method:' 'PUT'})

    def partial_update(self,request,pk=None):
        """ Handle updateing partion of an object"""
        return Response({'Http_method:' 'PATCH'})

    def destroy(self,request,pk=None):
        """ Handle removing an object"""
        return Response({'Http_method:' 'DELETE'})
