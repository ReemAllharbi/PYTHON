from django.shortcuts import redirect, render
from poorly_coded_store.models import Order, Product


def index(request):
    return redirect("/amadon")

def amadon(request):
    context = { "all_products": Product.objects.all() }

    return render(request,"index.html", context)



def checkout(request,product_id):
   if request.method=="POST":
     quantity = int(request.POST["quantity"])
     product_id = request.POST["product_id"]
     price_for_selected_product=Product.objects.get(id=product_id)
     price= price_for_selected_product.price
     total_charge=quantity*price
     selected_order=Order.objects.create(quantity_ordered=quantity, total_price=total_charge)
     order_id=selected_order.id
     return redirect(f"/amadon/checkout/{product_id}/{order_id}")

     
def checkoutt(request,product_id,order_id):
   allOrders=Order.objects.all()
   selected_order=Order.objects.get(id=order_id)
   quantity_for_order=selected_order.quantity_ordered
   price_for_selected_product=Product.objects.get(id=product_id)
   price= price_for_selected_product.price
   total_charge=quantity_for_order*price
   total_charge_spend = 0
   for order in allOrders:
     total_charge_spend += order.total_price 
   context = {  "quantity":quantity_for_order, "total_charge":total_charge ,"total_charge_spend":total_charge_spend }
   return render(request,"checkout.html",context)


