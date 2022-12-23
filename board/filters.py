from django_filters import FilterSet
from .models import Reply

# FilterSet, который мы наследуем,
# должен чем-то напомнить знакомые вам Django дженерики.
class ReplyFilter(FilterSet):
   class Meta:
       # В Meta классе мы должны указать Django модель,
       # в которой будем фильтровать записи.
       model = Reply
       # В fields мы описываем по каким полям модели
       # будет производиться фильтрация.
       fields = {
           # поиск по тексту
           'text': ['icontains'],
           'post__caption': ['icontains'],
       }