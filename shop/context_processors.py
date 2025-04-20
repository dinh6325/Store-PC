from .models import Category

def categories(request):
    return {
        'categories': Category.objects.all(),
        'current_category': getattr(request, 'current_category', None),
    }
