from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import stripe

stripe.api_key = 'sk_test_51KbPVaL10zxMRfSILB2TMEdk47dtc0MLTnbi8c1pycGKLhN4xnDUalV8JvQeH9mrifZVprtQ3W1dLsqZJ91jJwgg00s7QXnz4b'

class StripeCheckoutView(APIView):
    def post(self, request):

        line_items = []
        for item in request.data['items']:
            dict = {'price': item['price_id'], 'quantity': item['quantity']}
            line_items.append(dict)

        try:
            checkout_session = stripe.checkout.Session.create(
                line_items=line_items,
                payment_method_types=['card', ],
                mode='payment',
                success_url=settings.SITE_URL + '/?success=true&session_id={CHECKOUT_SESSION_ID}',
                cancel_url=settings.SITE_URL + '/?canceled=true',
            )

            return Response({'url': checkout_session.url})
        except:
            return Response(
                {'error': 'Something went wrong when creating stripe checkout session'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
