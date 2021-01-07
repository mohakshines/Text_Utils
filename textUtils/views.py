# MADE BY ME
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'index.html')

def analyse(request):
    #GET THE TEXT
    text=request.POST.get('text','NO TEXT')
    punc=request.POST.get('check1','off')
    caps=request.POST.get('check2','off')
    lineremove=request.POST.get('check3','off')
    spaceremove=request.POST.get('check4','off')
    count=request.POST.get('check5','off')
    c=''

    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    res=''
    purpose=''
    if punc=='on':
        for i in text:
            if i not in punctuations:
                res=res+i
        text=res

    #CAPITALIZE
    if caps=='on':
        text=text.upper()
        purpose+='| CAPITALIZE '

    #LINE_REMOVER
    if lineremove=='on':
        text=text.replace("\n",'')
        text=text.replace('\r','')
        purpose+='|REMOVE NEW LINES'

    #SPACE_REMOVER
    if spaceremove=='on':
        temp=''
        for i in range(len(text)-1):
            if text[i]==' ' and text[i+1]==' ':
                pass
            else:
                temp+=text[i]
        text=temp
        purpose+='| REMOVE EXTRA SPACES |'

    #CHARACTER_COUNT
    if count=='on':
        c=len(text)
        purpose+='| CHARACTER COUNT '
    params={'purpose':purpose,'analysed_text':text,'count':c}

    if punc=='on' or caps=='on' or lineremove=='on' or spaceremove=='on' or count=='on':
        return render(request,'analyse.html',params)
    else:
        return HttpResponse("ERROR")



# def capfirst(request):
#     return HttpResponse('''CAP_FIRST<button type="button"><a href="http://127.0.0.1:8000/">BACK</a></button>''')
# def newlineremove(request):
#     return HttpResponse('''NEW_LINE_REMOVER<button type="button"><a href="http://127.0.0.1:8000/">BACK</a></button>''')
# def spaceremover(request):
#     return HttpResponse('''SPACE_REMOVER<button type="button"><a href="http://127.0.0.1:8000/">BACK</a></button>''')
# def charcount(request):
#     return HttpResponse('''CHAR_COUNT<button type="button"><a href="http://127.0.0.1:8000/">BACK</a></button>''')


