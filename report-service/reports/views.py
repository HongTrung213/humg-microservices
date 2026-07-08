import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def thong_ke_sinh_vien(request):
    try:
        resp = requests.get('http://localhost:8001/api/sinhvien/')
        if resp.status_code == 200:
            return Response(resp.json())
        else:
            return Response({'error': 'Cannot fetch students'}, status=status.HTTP_503_SERVICE_UNAVAILABLE)
    except:
        return Response({'error': 'Student service unavailable'}, status=status.HTTP_503_SERVICE_UNAVAILABLE)

@api_view(['GET'])
def thong_ke_thi(request):
    try:
        resp = requests.get('http://localhost:8002/api/lichsuthi/')
        if resp.status_code == 200:
            return Response(resp.json())
        else:
            return Response({'error': 'Cannot fetch exam data'}, status=status.HTTP_503_SERVICE_UNAVAILABLE)
    except:
        return Response({'error': 'Exam service unavailable'}, status=status.HTTP_503_SERVICE_UNAVAILABLE)