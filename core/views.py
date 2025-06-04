from django.http import HttpResponse

def home(request):
    return HttpResponse("Olá, jogador! Seu app está funcionando no Render 🎮")
