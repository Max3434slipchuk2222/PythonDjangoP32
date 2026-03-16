from django import forms
from .models import Category


class CategoryForm(forms.ModelForm):
    name = forms.CharField(
        label="Назва категорії",
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введіть назву...'
        })
    )
    description = forms.CharField(
        label="Опис",
        required=False,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 3,
            'placeholder': 'Короткий опис категорії...'
        })
    )
    slug = forms.SlugField(
        label="Slug",
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'my-category'
        })
    )
    image = forms.ImageField(
        label="Зображення",
        required=False,
        widget=forms.FileInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Category
        fields = ('name', 'description', 'slug', 'image')

    def clean_name(self):
        name = self.cleaned_data.get('name')
        qs = Category.objects.filter(name=name)
        if self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise forms.ValidationError("Категорія з такою назвою вже існує.")
        return name