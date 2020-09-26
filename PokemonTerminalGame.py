import random
import requests


def generateID():
    ID = random.randint(1, 151)
    return ID


def getPokemon():
    url = 'https://pokeapi.co/api/v2/pokemon/' + str(generateID())
    get = requests.get(url)
    pokemon = get.json()
    return pokemon


class Pokemon:
    def __init__(self):
        pokemon = getPokemon()

        self.name = pokemon['name'].title()
        self.ID = pokemon['id']
        self.height = pokemon['height']
        self.weight = pokemon['weight']


def compare(player, comp):
    if(player > comp):
        won = 1
        print('You Won!')
    elif(player == comp):
        won = 0
        print("It's a Draw")
    else:
        won = 0
        print('You Lost!')
    return won


def compareStats(stat, playerPokemon, COMPokemon):
    if(stat == 'id'):
        result = compare(playerPokemon.ID, COMPokemon.ID)
        return result
    elif(stat == 'weight'):
        result = compare(playerPokemon.weight, COMPokemon.weight)
        return result
    elif(stat == 'height'):
        result = compare(playerPokemon.height, COMPokemon.height)
        return result


def playGame(score):
    COMPokemon = Pokemon()
    playerPokemon = Pokemon()
    print(
        f'Your Card: \n Pokemon: {playerPokemon.name} (ID: {playerPokemon.ID}) \n Height: {playerPokemon.height} \n Weight: {playerPokemon.weight}')
    print(f'Your opponent chose: {COMPokemon.name}')

    chosenStat = str(
        input('Which stat would you like to use? ID / Height / Weight \n')).lower()

    result = compareStats(chosenStat, playerPokemon, COMPokemon)
    score += int(result)
    print(f'Current Score: {score}')
    playGame(score)


# Game Starts Here
score = 0
playGame(score)

