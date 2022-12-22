from django import forms
from django.core.exceptions import ValidationError
from .models import Post
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class PostForm(forms.ModelForm):
    # text = forms.CharField(min_length=20)    # валидация по минимальному количеству
    # text = forms.CharField(widget=SummernoteWidget())  # instead of forms.Textarea

    class Meta:
        model = Post
        fields = [
            'category',
            'caption',
            'text',
            'author'
        ]

        widgets = {
            'text': SummernoteWidget(),
           # 'text': SummernoteInplaceWidget(),
        }

    def clean(self):
        cleaned_data = super().clean()
        caption = cleaned_data.get("caption")
        if caption is not None and len(caption) < 10:
            raise ValidationError({
                "caption": "Заголовок не может быть менее 10 символов."
            })

        text = cleaned_data.get("text")
        if caption == text:
            raise ValidationError("Заголовок не должно быть идентичен тексту.")

        return cleaned_data


class ReplyForm(forms.ModelForm):
    text = forms.CharField(min_length=10)    # валидация по минимальному количеству



