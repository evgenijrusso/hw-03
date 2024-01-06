# Теперь, имея у себя в багаже знания о фильтрах, нам не составит труда разобраться с тегами.
# Представим, что текущую дату нам нужно выводить на множестве страниц.
# Только из-за этой незначительной вещи ходить и изменять множество классов представлений неприятно.
# Вспомните, как мы переопределяли метод 'get_context_data' в ProductList.
# Так нам нужно было бы сделать со всеми представлениями, где нам понадобилось время.
# Подобное дублирование кода — отличный кандидат на вынесение в тег. Приступим!
#
# Добавим в папку simpleapp/templatetags/ новый файл 'custom_tags.py' и опишем в нем наш тег вывода текущего времени.

from datetime import datetime
from django import template

register = template.Library()

@register.simple_tag()
def current_time(format_string='%d %b %Y'):    # b -  прописной месяц
   return datetime.utcnow().strftime(format_string)


@register.simple_tag(takes_context=True)
def url_replace(context, **kwargs):
   d = context['request'].GET.copy()
   for k, v in kwargs.items():
       d[k] = v
   return d.urlencode()
