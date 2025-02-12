import cv2
import numpy as np
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.core.files.base import ContentFile
from .models import ProcessedImage
from .serializers import ProcessedImageSerializer



class ProcessedImageViewSet(viewsets.ModelViewSet):
    queryset = ProcessedImage.objects.all()
    serializer_class = ProcessedImageSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=False, methods=['POST'])
    def process_image(self, request):
        if 'image' not in request.FILES:
            return Response({'error': 'No image provided'}, status=status.HTTP_400_BAD_REQUEST)

        image = request.FILES['image']

        img = cv2.imdecode(np.frombuffer(image.read(), np.uint8), cv2.IMREAD_COLOR)

        processed = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        _, buffer = cv2.imencode('.jpg', processed)
        content_file = ContentFile(buffer.tobytes())

        processed_image = ProcessedImage(user=request.user)
        processed_image.original_image.save(image.name, image)
        processed_image.processed_image.save(f"processed_{image.name}", content_file)

        serializer = self.get_serializer(processed_image)
        return Response(serializer.data, status=status.HTTP_201_CREATED)