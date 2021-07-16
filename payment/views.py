from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from orders.models import Order
from django.views.generic import View



class EsewaRequestView(View):
    def get(self, request, *args, **kwargs):
        order_id = request.session.get('order_id')
        print(order_id)
        order = get_object_or_404(Order, id=order_id)
        total_cost = order.get_total_cost()
        context = {
            "member": total_cost
        }
        return render(request, "esewa_request.html", context)


class EsewaVerifyView(View):
    def get(self, request, *args, **kwargs):
        import xml.etree.ElementTree as ET
        oid = request.GET.get("oid")
        amt = request.GET.get("amt")
        refId = request.GET.get("refId")

        url = "https://uat.esewa.com.np/epay/transrec"
        d = {
            'amt': amt,
            'scd': 'epay_payment',
            'rid': refId,
            'pid': oid,
        }
        resp = requests.post(url, d)
        root = ET.fromstring(resp.content)
        status = root[0].text.strip()

        order_id = oid.split("_")[1]
        member_obj = Member.objects.get(id=order_id)
        if status == "Success":
            member_obj.payment_completed = True
            member_obj.save()
            return redirect("/")
        else:

            return redirect("/esewa_request/?o_id="+order_id)
