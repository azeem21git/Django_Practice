from django.shortcuts import render



def HomePage(request):

    data={
        "name": "azeem",
        "role":"admin",
        "numbers":[1,2,3,5,7,],
        "marks":{
            "Tamil":50,
            "English":100,
        }
    }

    return render(request,'home.html',data)


def AboutPage(request):
    return render(request,'about.html')


def ContactPage(request):
    return render(request,'contact.html')


def ServicePage(request):
    return render(request,'service.html')
