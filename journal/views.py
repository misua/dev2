from django.shortcuts import render, redirect
from . forms import CreateUserForm, LoginForm

from django.contrib.auth import authenticate,login as auth_login,logout
from django.contrib import auth
import logging


from django.contrib.auth.decorators import login_required


logger = logging.getLogger(__name__)

def home(request):
    return render(request, 'journal/index.html')





def register(request):
 
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST or None)
        
        if form.is_valid():
            try:
                form.save()
            except Exception as e:
                print(f"error saving form: {e}")
                return render(request, 'journal/register.html', {'RegistrationForm': form})
            return redirect('my-login')
         
    context = {'RegistrationForm': form}
         
    return render(request, 'journal/register.html', context)




def my_login(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST,data=request.POST)

        if form.is_valid(): 
            try:
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(request, username=username, password=password)
            except Exception as e:
                print(f"error authenticating user: {e}")
                return render(request, 'journal/my-login.html', {'LoginForm': form})    
            
            if user is not None:
                auth_login(request, user)
                return redirect('dashboard')
            else:
                form.add_error(None, 'Invalid username or password')
            
    context = {'LoginForm': form}
    return render(request, 'journal/my-login.html', context)
 
    


@login_required(login_url='my-login')
def user_logout(request):
    auth.logout(request)

    return redirect('index')



@login_required(login_url='my-login')
def dashboard(request):
    websites = [
        {"url": "www.walmart.com", "country": "US", "created": "Feb 4, 2024", "language": "EN"},
        {"url": "www.amazon.com", "country": "US", "created": "Mar 5, 2025", "language": "EN"},
        {"url": "www.homedepot.com", "country": "US", "created": "April 4, 2023", "language": "EN"},
        {"url": "www.target.com", "country": "US", "created": "Mar 5, 2025", "language": "EN"},
        {"url": "www.ebay.com", "country": "US", "created": "Feb 4, 2024", "language": "EN"},
        {"url": "www.nike.com", "country": "US", "created": "Mar 6, 2025", "language": "EN"},
        {"url": "www.etsy.com", "country": "Unknown", "created": "Feb 4, 2024", "language": "SPAN"},
        {"url": "www.macys.com", "country": "US", "created": "Mar 5, 2025", "language": "EN"},
        {"url": "www.rakuten.com", "country": "JP", "created": "Sept 4, 2024", "language": "JP"},
        {"url": "www.walgress.com", "country": "US", "created": "Mar 5, 2025", "language": "EN"},
        ]
    platforms = ["WooCommerce", "Shopify", "Wix", "Squarespace", "Big Cartel", "Prestashop","BandaCamp", "Magento", "OpenCart", "Volusion", "3dcart", "Weebly", "BigCommerce", "Ecwid", "Joomla", "Drupal", "Zen Cart", "osCommerce", "X-Cart", "Spree Commerce", "nopCommerce", "VirtueMart", "Pinnacle Cart", "Ubercart", "CS-Cart", "CubeCart", "AbleCommerce", "Miva Merchant", "ShopSite", "AgoraCart", "Avactis", "CoreCommerce", "Fortune3", "Jigoshop", "LemonStand", "LiteCart", "Loaded Commerce", "Mozu", "PrestaShop", "RomanCart", "Satchmo", "Shopp", "SunShop", "Tictail", "UltraCart", "Vendio", "VTEX", "WebSphere Commerce", "X-Cart", "Yola", "Zepo", "Znode"]
    context = {'username': request.user.username, 'websites': websites, 'platforms': platforms}
    return render(request, 'journal/dashboard.html', context)
