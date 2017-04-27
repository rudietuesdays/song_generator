from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.views.generic import View
from .models import Song
from django.http import HttpResponse

# Create your views here.
class Welcome(View):
    def get(self, request):
        songs = Song.objects.all()
        print '*'*20
        print len(songs)

        return render(request, 'lyricsMaker_templates/index.html')

    def post(self, request):
        postData = {
            'genre': request.POST.get('genre'),
            'subj': request.POST.get('subject'),
            'pronouns': request.POST.get('pronouns'),
        }

        result = Song.objects.validate(postData)

        if result[0]:
            print '*'*20
            print result[0], result[1]
            request.session['song_id'] = result[1].id
            song_obj = result[1]

            context = {
                'song_obj': song_obj
            }
            return HttpResponse('Submitted. Thanks for your idea! It belongs to us now.')

        else:
            for err in range(len(result[1])):
                messages.error(request, result[1][err])
            return redirect('/')

class Songs(View):
    def get(self, request):
        song = Song.objects.get(id=3)

        context = {
            'song': song,
        }
        return render(request, 'lyricsMaker_templates/lyrics.html', context)
    def post(self, request):

        song = Song.objects.get(id=1)

        context = {
            'song': song,
        }
        return render(request, 'lyricsMaker_templates/lyrics.html', context)

class Library(View):
    def get(self, request):
        songs = Song.objects.all()

        context = {
            'songs': songs,
        }

        return render(request, 'lyricsMaker_templates/library.html', context)
        
    def post(self, request):
        songs = Song.objects.all()

        context = {
            'songs': songs,
        }

        return render(request, 'lyricsMaker_templates/library.html', context)
