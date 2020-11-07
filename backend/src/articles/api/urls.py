from django.urls import path
#from .views import articlelist,articleretrive,articlecreate,articledelete,articleupdate
from .views import UserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'',UserViewSet,basename='articles')
urlpatterns = router.urls

# urlpatterns = [
#     path('',articlelist.as_view()),
#     path('<pk>',articleretrive.as_view()),
#     path('create/',articlecreate.as_view()),
#     path('<pk>/update/',articleupdate.as_view()),
#     path('<pk>/delete/',articledelete.as_view()),
# ]
