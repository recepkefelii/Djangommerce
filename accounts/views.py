from rest_framework import generics, status, permissions
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import SignUpSerializer, LoginSerializer, EmailVerificationSerializer
from .emails import sendEmail



class SignUpView(generics.GenericAPIView):
    serializer_class = SignUpSerializer
    permission_classes = []

    def post(self, request: Request):
        data = request.data

        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
 
            serializer.save()
            sendEmail(serializer.data['email'])
            

            response = {"message": "Kullanici olusturuldu",
                        "data": serializer.data}

            return Response(data=response, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    permission_classes = []
    serializer_class = LoginSerializer

    def post(self, request):
        serializer_class = self.serializer_class(data=request.data)

        if serializer_class.is_valid():
            token = serializer_class.validated_data['token']
            return Response(data=token, status=status.HTTP_200_OK)

    def get(self, request: Request):
        content = {"user": str(request.user), "auth": str(request.auth)}

        return Response(data=content, status=status.HTTP_200_OK)


class RetrieveUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        user = request.user
        user = SignUpSerializer(user)
        verificationStatus = request.user.verification
        if not verificationStatus:

            return Response(data={"Please verify your email"})
        
        return Response(data=user.data)

              

class VerificationUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self,request:Request):
        user = request.user
        
        data = request.data
        serializer = EmailVerificationSerializer(data=data)
        verificationCode = data['verificationCode']

        if serializer:
            code = request.user.verificationCode

            if user.verification == True:
                return Response(data={"info":"email veridication already"})

            if verificationCode == code:
                user.verification = True
                user.save()
                return Response(data={"info":"email verification succecess"})

            elif data != code:
                return Response(data={"wrong verification code"})
            
            else:
                return Response(data={"error":"invalid verificationCode"},status=status.HTTP_400_BAD_REQUEST)




        






            
           
            
             
        
