from django.shortcuts import render


def anasayfa(request):
    context={
        "hello":"helloworld!!"
    }
    return render(request, "sayfalar/anasayfa/anasayfa.html" , context)