from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
class HelloApiView(APIView):
    """Test api view"""

    def get(self,request,format=None):
        """Request a list of APIView features"""
        an_apiview=[
            'Uses Http methods as function(get,post,patch,delete,put,delete)',
            'Is similar to a tradional django ',
            'Gives you the most control over your application logic',
            'Is mapped manually to urls',

        ]
        return Response({'message':"Hello!",'an_apiview':an_apiview})