#  i have created this file : shubham sharma
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request, 'index.html')
def analyze(request):
    # Get the text  
    djtext = request.POST.get('text' , 'default')
    # check checkbox values
    removepunk = request.POST.get('removepunk', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')
    # check which checkbox is on 
    params = {}
    print(type(params))
    print(len(params))
    if removepunk == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
    if (fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed= analyzed + char.upper()
        params = {'purpose ': 'Make All caps', 'analyzed_text': analyzed}
        djtext = analyzed
    if newlineremover == 'on':
        analyzed=''
        for char in djtext:
            if char != "\n" and char!="\r":
                analyzed=analyzed+char
        params = {'purpose ': 'Removed newline', 'analyzed_text': analyzed}
        djtext =analyzed
    if(extraspaceremover=="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext =analyzed
    if(charcount=="on"):
        analyzed = djtext
        flag = 0
        for char in djtext:
            if not (char == ' '):
                flag+=1
        params = {'purpose': flag, 'analyzed_text': analyzed}
    if(params == {}):
        return HttpResponse ("Error")
    return render(request, 'analyze.html', params)
    