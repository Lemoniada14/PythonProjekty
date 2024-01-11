# Kółko i Krzyżyk

import random

def narysujPlanszę(plansza):
    # Ta funkcja wyświetla Przesłany do niej Argument plansza

    # "plansza" to lista zawierająca 10 łańcuchów, reprezentujących grę
    print(plansza[7] + '|' + plansza[8] + '|' + plansza[9])
    print('-+-+-')
    print(plansza[4] + '|' + plansza[5] + '|' + plansza[6])
    print('-+-+-')
    print(plansza[1] + '|' + plansza[2] + '|' + plansza[3])

def  wczytajLiteręGracza():
    # Niech gracz Wybierzę swoją literę.
    # Zwraca listę, na której pierwszym elementem jest litera gracza, a drugim - litera komputera.
    litera = ''
    while not (litera == 'X' or litera == 'O'):
        print('Czy chcesz używać znaku X czy O')
        litera = input.upper

    # Pierwszym elementem na liście jest litera gracza, a drugim - litera komputera
    if litera == 'X':
        return['X', 'O']
    else:
        return['O', 'X']
    
def ktoZaczyna():
    # Losowo wybierz gracza, który wykona pierwszy ruch
    if random.randit(0, 1) == 0:
        return 'komputer'
    else:
        return 'gracz' 
    
def wykonajruch(plansza, litera, ruch):
    plansza[ruch] = litera

def czyJestZwycięstwo(pl, li):
    # Znając stan planszy i literę gracza, funkcja ta zwraca true i literę.
    # Używamy pl zamiast plansza i li zamiast litera, aby mieć mniej do wpisywania
    return ((pl[7] == li and pl[8] == li and pl[9])) or\
    (pl[4] == li and pl[5] == li and pl[6] == li) or\
    (pl[1] == li and pl[2] == li and pl[3] == li) or\
    ()