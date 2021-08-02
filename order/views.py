from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from order.models import ShopCart
from user.models import Profile


@login_required(login_url='login')
def shopcart(request):
    user = Profile.objects.get(user=request.user)
    shopcart_ = ShopCart.objects.filter(user=user)
    total = 0
    for shop in shopcart_:
        total += shop.product.price * shop.quantity
    context = {
        'shopcart': shopcart_,
        'total': total,
    }
    return render(request, 'order/shopcart.html', context)
