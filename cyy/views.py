# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from cyy.models import Article,Comment
from django.template import RequestContext
from django.utils import simplejson as json
import re

def index(request):
	result_article = Article.objects.all().order_by('-pk')
	return render_to_response('index.html',{'result_article':result_article,'pos':False},context_instance=RequestContext(request))	

def pic(request):
	source = request.GET.get('source',None)
	if source:
		return HttpResponseRedirect(source)
	else:
		return HttpResponseRedirect('404.html')

def search(request):
	keywd = request.GET.get('q',None)
	return get_tag(request,keywd)	

def get_tag(request,tag):
	result = Article.objects.all().order_by('-pk')
	tag_result=[]
	for A in result:
		if A.tags:
			if tag in re.split(' *',A.tags.strip()):	
				tag_result.append(A)
	return render_to_response('index.html',{'result_article':tag_result,'pos':False},context_instance=RequestContext(request))	

def home(request):
	return HttpResponseRedirect('/index/')

def none(request):
	return render_to_response('none.html')

def detail(request,num_pk):
	result_comment = Comment.objects.filter(article=Article.objects.get(pk=num_pk)).order_by('pk')
	result_article = Article.objects.filter(pk=num_pk)
	return render_to_response('detail.html',{'result_article':result_article,'pos':True,'result_comment':result_comment},context_instance=RequestContext(request))

def error(request):
	return render_to_response('404.html')

def post_msg(request):
	if request.method == "POST":
		from_addr	= request.POST.get('from_addr',None)	
		to_addr		= request.POST.get('to_addr',None)	
		msg 		= request.POST.get('msg',None)	
		atc_pk		= request.POST.get('atc_pk',None)
		C = Comment(article=Article.objects.get(pk=atc_pk),msg=msg,from_addr=from_addr,to_addr=to_addr)
		A = Article.objects.get(pk=atc_pk)
		A.comment_count += 1
		if C.save() and A.save():
			#d={'from_addr':from_addr,"to_addr":to_addr,"msg":msg}
			d={'status':'success'}
			return HttpResponse(json.dump(d))
		else:
			return HttpResponseRedirect('/error/')
	else:
		return HttpResponseRedirect('/error/')
