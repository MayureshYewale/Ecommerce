from .models import Product,category,User,OrderItem,Payment
from .serializers import productserializer,categoryserializer,Userserializer,orderitemsserializers,OrderSerializer,paymentserializer
from .views import productviewset,catogeryviewset,userviewset,orderitemsviewset,orderviewset,PaymentViewSet
from rest_framework.routers import DefaultRouter
from django.urls import path,include

router=DefaultRouter()
router.register(r"User",userviewset)
router.register(r'Products',productviewset)
router.register(r'categories',catogeryviewset)
router.register(r"orders",orderviewset)
router.register(r"orderitems",orderitemsviewset)
router.register(r'payments', PaymentViewSet)

urlpatterns = [
    path('',include(router.urls))
]
