from django.shortcuts import render

# Create your views here.


def anasayfa(request):
    context={
        "hello":"helloworld!!"
    }
    return render(request, "sayfalar/anasayfa/anasayfa.html" , context)