from rest_framework.decorators import api_view
from rest_framework.response import Response
from customer.models import Review
from rest_framework import serializers
from rest_framework import status
from customer.serializers import review_serializer


@api_view(['GET'])
def get_reviews(req):
    reviews = Review.objects.all()
    serializer = review_serializer(reviews, many=True)
    return Response(serializer.data)


@api_view(['POST', 'GET'])
def add_review(request):
    review = review_serializer(data=request.data)

    # validating for already existing data
    if Review.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This review already exists')

    if review.is_valid():
        review.save()
        return Response(review.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
