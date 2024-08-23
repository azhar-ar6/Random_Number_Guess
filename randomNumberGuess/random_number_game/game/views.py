from django.shortcuts import render, redirect
import random


def start_game(request):
    # Reset game state for a new round
    request.session['random_number'] = random.randint(1, 100)
    request.session['attempts'] = 0
    request.session['rounds'] = request.session.get('rounds', 0) + 1
    request.session['max_attempts'] = 10
    request.session['message'] = "Guess a number between 1 and 100."
    request.session['game_over'] = False
    if 'score' not in request.session:
        request.session['score'] = 0
    return redirect('play_round')



def play_round(request):
    if request.method == 'POST':
        user_guess = int(request.POST.get('guess', 0))
        request.session['attempts'] += 1

        if user_guess < request.session['random_number']:
            request.session['message'] = "Hint! Higher Number"
        elif user_guess > request.session['random_number']:
            request.session['message'] = "Hint! Lower Number"
        else:
            request.session['message'] = f"Hurray! You guessed the number in {request.session['attempts']} attempts."
            score_increment = max(0, 10 - request.session['attempts'])
            request.session['score'] = request.session.get('score', 0) + score_increment
            request.session['game_over'] = True
            return redirect('game_over')

        if request.session['attempts'] >= request.session['max_attempts']:
            request.session[
                'message'] = f"Sorry! You have exhausted all attempts. The number was {request.session['random_number']}."
            request.session['game_over'] = True
            return redirect('game_over')

    return render(request, 'game/play_round.html', {'game_state': request.session})


def game_over(request):
    if request.method == 'POST':
        play_again = request.POST.get('play_again', 'no').lower()
        if play_again == 'yes':
            return redirect('start_game')
        else:
            return redirect('game_summary')

    return render(request, 'game/game_over.html', {'game_state': request.session})


def game_summary(request):
    return render(request, 'game/game_summary.html', {'game_state': request.session})
