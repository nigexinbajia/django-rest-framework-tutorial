from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

# Create your models here.

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class Snippet(models.Model):
    """
    一个存储代码的Model，并且有MarkDown代码高亮
    """
    created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    title = models.CharField(max_length=100, blank=True, null=True, verbose_name='标题')
    code = models.TextField(verbose_name='代码')
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100, verbose_name='语言')
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100, verbose_name='样式')

    class Meta:
        ordering = ('created',)  # 按照创建时间排序
