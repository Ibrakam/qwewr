from django.shortcuts import render, redirect
from . import models
from . import handlers
def catalog(request):
  all_categories = models.Category.objects.all()
  all_products = models.Product.objects.all()


  search_value_from_front = request.GET.get('search')
  if search_value_from_front:
    all_products = models.Product.objects.filter(name__contains=search_value_from_front)

  context = {'all_categories': all_categories, 'all_products': all_products}

  return render(request, 'index.html', context)


def get_category_products(request, pk):
  exact_category_products = models.Product.objects.filter(category_name__id=pk)

  context = {'category_products': exact_category_products}

  return  render(request, 'category.html', context)


def get_product_products(request, pk, name):
  exact_products = models.Product.objects.get(name=name, id=pk)

  context = {'product': exact_products}

  return render(request, 'product.html', context)

def add_product_to_cart(request, pk):
  quantity = request.POST.get('pr_count')
  product_to_add = models.Product.objects.get(id=pk)
  models.UserCart.objects.create(user_id=request.user.id,
                                 user_product=product_to_add,
                                 user_product_quantity=quantity).save()

  return redirect('/')

def cart(request):
  cart = models.UserCart.objects.filter(user_id=request.user.id)
  context = {
    'cart_products': cart
  }
  return render(request, 'cart.html', context)


def complete_order(request):
  user_cart = models.UserCart.objects.filter(user_id=request.user.id)

  result_text = 'Новый заказ\n\n'
  if request.method == 'POST':
    result_text = 'Новый заказ\n\n'
    total = 0
    for cart in user_cart:
      result_text += f'Название товара:{cart.user_product}\n' \
                   f'Количество:{cart.user_product_quantity}\n'
      total+=cart.user_product.price*cart.user_product_quantity
    result_text += f'\n Итог: {total}'
    handlers.bot.send_message(889121031, result_text)
    user_cart.delete()
    return  redirect('/')
  return render(request, 'cart.html', {'user_cart': user_cart})


def delete_from_cart(request, pk):
  product_to_delete = models.Product.objects.get(id=pk)
  models.UserCart.objects.filter(user_id=request.user.id, user_product=product_to_delete).delete()
  return redirect('/cart/')






