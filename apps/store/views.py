from django.shortcuts import render, redirect
from io import BytesIO # nos ayuda a convertir un html en pdf
from django.http import HttpResponse
from django.views import View
from xhtml2pdf import pisa
from django.template.loader import get_template
def index(request):
    return render(request, 'store/index.html')

def buy(request):
    if 'list' not in request.session:
        request.session['list'] = {
            'counter':0,
            'sum':0.0,
            'price':0.0
        }
 
    price = 0
    if request.POST['id'] == '0':
        price = 18.50
    elif request.POST['id'] == '1':
        price = 22.90
    elif request.POST['id'] == '2':
        price = 18.40
 
    
    price*= int(request.POST['amount'])

    request.session['list']['counter']+=int(request.POST['amount'])
    request.session['list']['sum']+=price
    request.session['list']['price']=price
    request.session.modified = True
    print (request.session['list']['price'])

    return redirect('/store/checkout/')

def reset(request):
    request.session.clear()
    return redirect('/store/')

def checkout(request):
    return render(request, 'store/checkout.html')

def home (request):
    return render(request,'store/index.html')


def SaleInvoicePdfView(request, *callback_args, **callback_kwargs):
    try:
        template=get_template('store/invoice.html')
        context ={'title':''}
        html=template.render(context)
        response =HttpResponse(content_type='application/pdf')
        pisaStatus =pisa.CreatePDF(html,dest=response)
        return response
    except:
        pass
    return render(request,'store/index.html')


        

