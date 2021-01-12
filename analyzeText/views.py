from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homepage(request):
    return render(request, 'home.html')


def analyze_text(request):
    textdj = request.POST.get('text' , 'default')

    fullcap = request.POST.get('capitalize', 'off')
    removepuc = request.POST.get('removepunc' , 'off')
    remove_space = request.POST.get('removespace' , 'off')
    if removepuc == 'on':
        punctuations = ''' !()-[]{};:'"\, <>./?@#$%^&*_~ '''
        analyze = ''
        for char in textdj:
            if char not in punctuations:
                analyze = analyze + char

        var = {'remove' : 'unwanted punctuations has been removed form the sentence', 'ana' : analyze}
        textdj = analyze
    
    if(fullcap == 'on'):
        analyze = ''
        for char in textdj:
            analyze = analyze + char.capitalize()
                
        var = {'remove' : 'text has capitalized', 'ana' : analyze}
        textdj = analyze

    if(remove_space == 'on'):
        analyze = ''
        char = " ".join(textdj.split())
        analyze = analyze + char

        var = {'remove' : 'Extra space has been removed form the sentence', 'ana' : analyze}

    if(fullcap != 'on' and removepuc != 'on' and  remove_space != 'on'):
        return HttpResponse("<h2>please select the vaild option and retry</h2>")


    return render(request, 'analyzed.html', var)
        
