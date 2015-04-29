from django.http import *
from .forms import *
from django.shortcuts import get_object_or_404,get_list_or_404, render
import json
from django.core.urlresolvers import reverse
from django.core.serializers.json import DjangoJSONEncoder


def index(request):
    return HttpResponse("Hello, world. You're at the ToGetThere index.")

def spByCategoryList(request, category_id):
    sps = get_list_or_404(SP, category = category_id)
    results = [sp.as_json(False) for sp in sps]
    return HttpResponse(json.dumps(results))

def spView(request, sp_id):
    sp = get_object_or_404(SP,pk=sp_id)
#    return JsonResponse(sp.as_json(True),encoder=DjangoJSONEncoder)
    return HttpResponse(json.dumps(sp.as_json(True), ensure_ascii=False))


def addSp(request):
    DEBUGG = False;
    if (request.method == 'GET') & (DEBUGG):
        form = SPForm()
        return render(request, 'ToGetThere/addSP.html', {'form': form,})
    elif request.method == 'POST':
        form = SPForm(request.POST)
        if form.is_valid():
            sp = form.save()
            return HttpResponseRedirect(reverse('ToGetThere:spView', args=(sp.pk,)))
        else:
            raise Http404(form.errors)

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

#TODO
def spAddReview(request, sp_id):
    sp = SP.objects.get(pk = sp_id)
    form = UserForm(request.POST, instance= sp)
    try:
        form.save()
    except ValueError:
        return HttpResponseBadRequest(ValueError.message)
    #TODO - validate redirect
    return HttpResponseRedirect("SP was Added!")


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
