from django.shortcuts import render
from django.http import JsonResponse
from random import randint

def reset_game():
    global number_to_find, remaining_attempts
    number_to_find = randint(0, 100)
    remaining_attempts = 5

# Initialisation lors du démarrage du serveur
reset_game()

def index(request):
    reset_game()  # Réinitialiser le jeu à chaque chargement de page
    return render(request, 'projet02/index.html')

def game_view(request):
    global number_to_find, remaining_attempts

    if request.method == "POST":
        try:
            user_choice = int(request.POST.get('guess'))
        except (ValueError, TypeError):
            return JsonResponse({"message": "Veuillez entrer un nombre valide.", "status": "error"})

        if remaining_attempts <= 0:
            return JsonResponse({"message": f"Dommage ! Le nombre mystère était {number_to_find}", "status": "game_over"})

        if number_to_find > user_choice:
            message = f"Le nombre mystère est plus grand que {user_choice}"
        elif number_to_find < user_choice:
            message = f"Le nombre mystère est plus petit que {user_choice}"
        else:
            return JsonResponse({"message": f"Bravo ! Le nombre mystère était bien {number_to_find} !", "status": "success", "attempts": 6 - remaining_attempts})

        remaining_attempts -= 1

        if remaining_attempts == 0:
            return JsonResponse({"message": f"Dommage ! Le nombre mystère était {number_to_find}", "status": "game_over"})

        return JsonResponse({"message": message, "status": "continue", "remaining_attempts": remaining_attempts})

    return render(request, 'projet02/index.html')
