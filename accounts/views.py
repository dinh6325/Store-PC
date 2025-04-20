from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, get_user_model
from django.contrib.auth.views import LoginView
from django.urls import reverse
from .forms import RegisterForm

User = get_user_model()
class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        # Nếu là admin, chuyển đến trang CRUD sản phẩm
        if self.request.user.is_superuser:
            return reverse('admin_product_list')
        return reverse('home')
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            # UserCreationForm.save() đã gọi set_password(password1)
            user = form.save()
            # Tự động đăng nhập
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()

    return render(request, 'accounts/register.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')
