import os
from django.forms import model_to_dict
from django.http import HttpResponse
from django.shortcuts import redirect, render
from pytube import YouTube
def home(request):
    if request.method == "POST":
        link=request.POST['link']
        my_video = YouTube(link)
        emb_link="https://www.youtube.com/embed/"+link[17:]
        context= {
        'link': link,
        'tittle': my_video.title,
        'thumbnail': my_video.thumbnail_url,
        'emb_link': emb_link,
        }
        request.session['context'] = context
        return redirect("download")
    return render(request,"downloader/index.html",{})
def download(request):
    path=os.getcwd()
    context = request.session.get('context')
    if (request.method == "POST"):
        my_video = YouTube(context['link'])
        my_video = my_video.streams.get_highest_resolution()
        my_video.download(path)
        return render(request,"downloader/thanku.html",context)
    return render(request,"downloader/download.html",context)

