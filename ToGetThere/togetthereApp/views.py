from django.http import *
from .forms import *
from django.shortcuts import get_object_or_404,get_list_or_404, render
import json
from django.core.urlresolvers import reverse
from django.core.serializers.json import DjangoJSONEncoder
from togetthereApp import forms


def index(request):
    return HttpResponse("Hello, world. You're at the ToGetThere index.")

def spByCategoryList(request, category_id):
    sps = get_list_or_404(SP, category = category_id)
    results = [sp.as_json(False) for sp in sps]
    return HttpResponse(json.dumps(results))

def spView(request, sp_id):
    sp = get_object_or_404(SP,pk=sp_id)
 #  return JsonResponse(sp.as_json(True),encoder=DjangoJSONEncoder)
    return HttpResponse(json.dumps(sp.as_json(True), ensure_ascii=False))


def addSp(request):
    DEBUGG = True;
    if (request.method == 'GET') & (DEBUGG):
        sp_form = AddSPForm()
        address_form = AddAddressForm()
        street_form = AddStreetForm()
        city_form = AddCityForm()
        return render(request, 'ToGetThere/addSP.html', {'address_form': address_form,
            'sp_form':sp_form, 
            'street_form':street_form, 
            'city_form':city_form})
    elif request.method == 'POST':
        sp_form = AddSPForm(request.POST)
        address_form = AddAddressForm(request.POST)
        street_form = AddStreetForm(request.POST)
        city_form = AddCityForm(request.POST)

        if (sp_form.is_valid() and address_form.is_valid() and street_form.is_valid() and city_form.is_valid()):
            fname = sp_form.cleaned_data['name']
            fdesc = sp_form.cleaned_data['desc']
            fcategory = sp_form.cleaned_data['category']
            flongitude = sp_form.cleaned_data['longitude']
            flatitude = sp_form.cleaned_data['latitude']
            fphone = sp_form.cleaned_data['phone']
            fdiscount = sp_form.cleaned_data['discount']
            fwebsite = sp_form.cleaned_data['website']
            fcity_name = city_form.cleaned_data['city_name']
            fstreet_name = street_form.cleaned_data['street_name']
            fstreet_num = address_form.cleaned_data['street_num']

            formCity= City.objects.get_or_create(city_name = fcity_name)
            formStreet = Street.objects.get_or_create(street_name  = fstreet_name, city = formCity)
            formAddress = Address.objects.get_or_create(street_num= fstreet_num, street=formStreet, city = formCity)
            formsp = Address.objects.get_or_create(name= fname, desc= fdesc, sp_address=formAddress , longitude=flongitude, latitude=flatitude, phone=fphone,
                discount= fdiscount, category=fcategory, website=fwebsite)
            return HttpResponseRedirect(reverse('ToGetThere:spView', args=(formsp.pk,)))
        else:

            raise Http404(str(sp_form.errors) + '\n' +
                str(address_form.errors) + '\n' +
                str(city_form.errors) + '\n' +
                str(street_form.errors))
                
                

#TODO
def rankSp(request, sp_id):
    sp = SP.objects.get(pk = sp_id)
    form = UserForm(request.POST, instance= sp)
    try:
        form.save()
    except ValueError:
        return HttpResponseBadRequest(ValueError.message)
    #TODO - validate redirect
    return HttpResponseRedirect("SP was ranked!")


def spReviews(request, sp_id):
    reviews = get_list_or_404(Review, sp=sp_id)
    results = [rev.as_json() for rev in reviews]
    return HttpResponse(json.dumps(results), ensure_ascii=False)

def spAddReview(request, sp_id):
    DEBUGG = True;
    if (request.method == 'GET') & (DEBUGG):
        form = AddReviewForm()
        return render(request, 'ToGetThere/addReview.html', {'form': form,})
    elif request.method == 'POST':
        form = AddReviewForm(request.POST)
        if form.is_valid():
            formTitle = form.cleaned_data['title']
            formContent = form.cleaned_data['content']
            formUser = form.cleaned_data['user']
            formSp = SP.objects.get(pk = sp_id)
            review = Review(title = formTitle, content= formContent, user = formUser, sp= formSp)
            review.save()
            return HttpResponseRedirect(reverse('ToGetThere:spView', args=(review.sp.pk,)))
        else:
            raise Http404(form.errors)


#TODO
def editSP(request, sp_id):
    sp = SP.objects.get(pk = sp_id)
    form = UserForm(request.POST, instance= sp)
    try:
        form.save()
    except ValueError:
        return HttpResponseBadRequest(ValueError.message)
    #TODO - validate redirect
    return HttpResponseRedirect("SP was edited!")

def userProfile(request, user_id):
    user = get_object_or_404(User,pk=user_id)
    return HttpResponse(json.dumps(user.as_json()), ensure_ascii=False)

#TODO
def editProfile(request, user_id):
    user = User.objects.get(pk = user_id)
    form = UserForm(request.POST, instance= user)
    try:
        form.save()
    except ValueError:
        return HttpResponseBadRequest(ValueError.message)
    return HttpResponseRedirect(reverse('togetthereApp:userProfile', args=(user.id,)))
