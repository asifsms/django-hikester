from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.utils import timezone
from .models import Item, Order, OrderItem
from django.contrib import messages
# Create your views here.


def index(request):
    return render(request, "index.html")


class ItemList(ListView):
    model = Item
    context_object_name = 'products'
    template_name = 'item_list.html'


class ItemDetail(DetailView):
    model = Item
    template_name = 'single_product.html'


def add_to_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_item, created = OrderItem.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False

    )
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "This item updated")
        else:
            messages.info(request, "This item added")
            order.items.add(order_item)
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(
            user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)
        messages.info(request, "This item added")
    return redirect("core:product", slug=slug)


def remove_from_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            order.items.remove(order_item)
            messages.info(request, "This item removed")
        else:
            # add a message saying the user dont have an order
            messages.info(request, "This item not in your cart")
            return redirect("core:product", slug=slug)

    else:
        # add a message saying the user dont have an order
        messages.info(request, "Dont have an order")
        return redirect("core:product", slug=slug)
    return redirect("core:product", slug=slug)

    # def item_list(request):
    #     context = {
    #         'items': Item.objects.all()
    #     }
    #     return render(request, "item_list.html", context)

    # def product_details(request):
    #     return render(request, "single_product.html")
