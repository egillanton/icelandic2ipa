from django.shortcuts import render
from django.http import HttpResponse
import json
import os


def home(request):
    context_dir = {"title": ""}
    return render(request, 'home/home.html', context=context_dir)


def transcribe(request):
    if request.method == 'GET':
        icelandicText = request.GET['icelandicText']
        transcribedText = ''
        words = icelandicText.split(' ')
        error = False
        for word in words:
            word = ''.join(c for c in word if c.isalpha())
            try:
                result = os.popen("echo " + word.lower() + " | g2p.py --encoding='utf-8' --model g2pModels/model-6 --apply -").read()
                transcribedText += result.split('\t')[1].replace(" ", "").replace("\n", "")
            except:
                error = True
                break

        if error:
            transcribedText = 'ERROR PLEASE TRY ANOTHER TEXT'
        else:
            transcribedText = '[' + transcribedText + ']'

        return HttpResponse(json.dumps({'transcribedText': transcribedText}), content_type="application/json")
