from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import categoryserializer,productserializer ,Userserializer,OrderSerializer,orderitemsserializers,paymentserializer
from .models import category,Product,User,Order,OrderItem,Payment
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

# Create your views here.
class userviewset(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=Userserializer

class productviewset(viewsets.ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=productserializer
    
    
class catogeryviewset(viewsets.ModelViewSet):
    queryset=category.objects.all()
    serializer_class=categoryserializer
    



# Order Viewset
class orderviewset(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Only show orders for the authenticated user
        return Order.objects.filter(user=self.request.user)

# Order Cancellation
class OrderCancelView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, order_id, *args, **kwargs):
        order = Order.objects.filter(id=order_id, user=request.user).first()
        if order and order.status == 'pending':
            order.status = 'cancelled'
            order.save()
            return Response({"detail": "Order cancelled successfully"}, status=status.HTTP_200_OK)
        return Response({"detail": "Invalid order or order cannot be cancelled"}, status=status.HTTP_400_BAD_REQUEST)

    
class orderitemsviewset(viewsets.ModelViewSet):
    queryset=OrderItem.objects.all()
    serializer_class=orderitemsserializers
    
        


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = paymentserializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Ensure that users can only view their own payments
        return Payment.objects.filter(order__user=self.request.user)

    def create(self, request, *args, **kwargs):
        # Override the create method to process the payment when it is created.
        order = get_object_or_404(Order, id=request.data['order'])
        
        # You would integrate with a payment gateway API here, e.g., Stripe, PayPal.
        # For now, let's assume we are simulating a successful payment.

        payment = Payment.objects.create(
            order=order,
            amount=order.total_price,
            status='completed',  # Simulating successful payment
            payment_method='Credit Card',  # Example method
            payment_reference='REF123456789',  # Simulate a payment reference
        )
        
        # Update the order status to 'completed' or 'paid'
        order.status = 'completed'
        order.save()

        # Return response with payment details
        return Response(paymentserializer(payment).data, status=status.HTTP_201_CREATED)
