from app.views.sendmailfunc import send_email
from app.models import CustomUser
from app.serializers import UserRegistrationSerializer

from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.views import APIView



class CurrentUserView(APIView):
    
    def get(self, request):
        user = request.user
        serializer = UserRegistrationSerializer(user)
        return Response(serializer.data)
    
    
    def put(self, request):       
        user_id = CustomUser.objects.get(pk=request.user.pk) 
        serializer = UserRegistrationSerializer(user_id, data=request.data, partial=True)  
        if serializer.is_valid():
            print(">>>>>>>>>>>>>>",request.user.password)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
 
 
class UserRegisterView(APIView): 
 permission_classes = [AllowAny] 
 def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_email = request.data.get('email')
        send_email(user_email)
        return Response(serializer.data)
        
        
    




  