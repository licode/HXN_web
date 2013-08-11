from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.views.generic.base import TemplateView
from django.shortcuts import render_to_response
from article.models import Article, Comment
from forms import ArticleForm, CommentForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.utils import timezone



def articles(request):

    if request.POST:
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/articles/all')

    else:
        form = ArticleForm()

    args = {}
    args.update(csrf(request))

    args['form'] = form
    args['articles'] = Article.objects.filter(myname=request.user.username)
    args['fullname'] = request.user.username

    return render_to_response('articles.html',args)


def all_functions(request):
    args = {}
    args['articles'] = Article.objects.filter(myname=request.user.username)
    args['fullname'] = request.user.username
    return render_to_response('all_functions.html',args)

#def all_beamlines(request):
#    return render_to_response('all_beamlines.html')


def beamline_status(request):
    return render_to_response('status.html')

def all_publications(request):
    return render_to_response('publications.html')

def tools(request):
    return render_to_response('data_tool.html')

def contacts_infor(request):
    return render_to_response('contacts.html')

