# views.py trong app 'shop'
from django.shortcuts import render,redirect
from .models import Product, Category
from .forms import ProductForm

from django.shortcuts import render, get_object_or_404

# View cho danh sách sản phẩm
def product_list(request):
    products = Product.objects.all()  # Lấy tất cả sản phẩm
    return render(request, 'shop/product_list.html', {'products': products})

# View cho chi tiết sản phẩm
def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)  # Lấy sản phẩm theo ID
    return render(request, 'shop/product_detail.html', {'product': product})

def search_products(request):
    query = request.GET.get('q', '')  # Lấy từ khóa tìm kiếm từ URL
    if query:
        products = Product.objects.filter(name__icontains=query)  # Tìm sản phẩm có tên chứa từ khóa
    else:
        products = Product.objects.all()  # Nếu không có từ khóa, hiển thị tất cả sản phẩm
    
    return render(request, 'shop/search_results.html', {'products': products, 'query': query})

def filter_products(request):
    categories = Category.objects.all()
    category_filter = request.GET.get('category', '')
    price_min = request.GET.get('price_min', 0)
    price_max = request.GET.get('price_max', 1000000)
    rating_min = request.GET.get('rating_min', 0)
    
    products = Product.objects.filter(
        category__id=category_filter,
        price__gte=price_min,
        price__lte=price_max,
        rating__gte=rating_min
    )

    return render(request, 'shop/product_list.html', {
        'products': products,
        'categories': categories,
        'category_filter': category_filter,
        'price_min': price_min,
        'price_max': price_max,
        'rating_min': rating_min,
    })
def cart_view(request):
    # Đây chỉ là ví dụ mẫu. Bạn có thể thay đổi nội dung tuỳ ý
    return render(request, 'shop/cart.html', {})

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'shop/add_product.html', {'form': form})