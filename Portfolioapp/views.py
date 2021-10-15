from django.shortcuts import render,redirect
from django.http import HttpResponse,StreamingHttpResponse, response
from wsgiref.util import FileWrapper
import mimetypes
import os
from django.core.mail import send_mail


# Create your views here.
def home(request):
    context={}
    return render(request,'portfolioapp/index.html',context)

#handle download fuctionality
def download(request):
    base_dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filename='Resume.pdf'
    filepath =base_dir + '/Files/' + filename
    thefile=filepath
    filename=os.path.basename(thefile)
    chunk_size=8192
    response=StreamingHttpResponse(FileWrapper(open(thefile,'rb'),chunk_size),content_type=mimetypes.guess_type(thefile)[0])
    response['Content-Length']=os.path.getsize(thefile)
    response['Content-Disposition']='Attachment;filename=%s'% filename     
    return response

#handle email fuctionality
def sendmail(request):
    if request.method =="POST":
        name=request.POST['contactName']
        message_email=request.POST['contactEmail']
        message_subject=request.POST['contactSubject']
        message=request.POST['contactMessage']
        body={'name':name, 'message_email':message_email,'message':message}
        message = "\n".join(body.values())        
        response=send_mail(
            message_subject,#subject            
            message,#message
            message_email,
            ['oihimekpen@gmail.com'],#to email
            fail_silently=False,
        )
        context={}
    return redirect('home')

    
   

