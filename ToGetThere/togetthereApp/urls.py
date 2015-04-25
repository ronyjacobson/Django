from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /ToGetThere/
	url(r'^$', views.index, name='index'),

    # ex: /ToGetThere/android/category/medical/
    url(r'^android/category/(?P<category_id>medical|restaurants|shopping|public_services|transportation|help)/$',
        views.spByCategoryList, name='sp_by_category'),

    # ex: /ToGetThere/android/sp/1
    url(r'^android/sp/(?P<sp_id>[0-9]+)/$', views.spView, name='spView'),

    # ex: /ToGetThere/android/add/
    url(r'^android/sp/add/$', views.addSp, name='add_sp'),

    # ex: /ToGetThere/android/sp/1/rank/
    url(r'^android/sp/(?P<sp_id>[0-9]+)/rank/$', views.rankSp, name='rank_sp_view'),

    # ex: /ToGetThere/android/sp/1/edit/
    url(r'^android/sp/(?P<sp_id>[0-9]+)/edit/$', views.editSP, name='rank_sp_view'),

    # ex: /ToGetThere/android/sp/1/reviews/
    url(r'^android/sp/(?P<sp_id>[0-9]+)/reviews/$', views.spReviews, name='rank_sp_view'),

     # ex: /ToGetThere/android/sp/1/addreview/
    url(r'^android/sp/(?P<sp_id>[0-9]+)/addreview/$', views.spAddReview, name='rank_sp_view'),

    # ex: /ToGetThere/android/user/1/
    url(r'^android/user/(?P<user_id>[0-9]+)/$', views.userProfile, name='user_profile'),

    # ex: /ToGetThere/android/myprofile/
    url(r'^android/myprofile/(?P<user_id>[0-9]+)/$', views.userProfile, name='my_profile'),

    # ex: /ToGetThere/android/editprofile/1/
    url(r'^android/editprofile/(?P<user_id>[0-9]+)/$', views.editProfile, name='my_profile'),

]