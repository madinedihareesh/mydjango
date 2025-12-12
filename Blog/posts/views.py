from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse

# Create your views here.
posts=[
    {
       'id':1,
        'name':'HTML',
        'Dis':'HTML is used to structure to build static web pages'
    },
    {
        'id':2,
        'name':'CSS',
        'Dis':'CSS is used to style the web pages'
    },
    {
        'id':3,
        'name':'Js',
        'Dis':'It is used to create actions to the web pages'
    }]
def home(request):
    html=''
    for post in posts:
        html+=f'''
               <div>
                    <h4>{post['id']}. {post['name']}</h4>
               </div>
            '''
    return HttpResponse(html)

def details(request,id):
    html=''
    is_valid=False
    for post in posts:
        if post['id']==id:
            post_dir=post
            is_valid=True
    if is_valid:
        html=f'''
                <div>
                    <h4>{post_dir['id']}.{post_dir['name']}</h4>
                    <p>{post['Dis']}</p>
                </div>
            '''
        return HttpResponse(html)
    else:
        return HttpResponseNotFound('The number you have requested for is not Available')


def title(request,id):
    url=reverse('post',args=[id])
    return HttpResponseRedirect(f'/posts/{id}/')


