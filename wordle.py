from random import randint
from termcolor import colored
from unidecode import unidecode
from dic import dic_accents

def input_valide(secret: str, tour: int):
    """Prend une entrée standard et la renvoie quand elle satisfait les conditions

    Args:
        secret (str): mot à deviner

    Returns:
        list: liste des lettres de la porposition
    """
    prop = input(f"Proposition {tour}/6 :\n")

    while not(unidecode(prop) in dic_sans_accents) or len(prop) != len(secret):
        if not(unidecode(prop) in dic_sans_accents):
            prop = input("Votre mot n'est pas dans notre dictionnaire, réessayez :\n")
        elif len(prop) < len(secret):
            prop = input("Mot trop court :\n")
        elif len(prop) > len(secret):
            prop = input("Mot trop long :\n")
    
    return list(dic_accents[dic_sans_accents.index(prop)])

def output(secret: list, prop: list):
    """Donne les indices pour chaque lettre

    Args:
        secret (list): mot secret à deviner
        prop (list): mot proposé par le joueur

    Returns:
        output (list): rouge mauvaise lettre, bleu mauvais emplacement, vert bon emplacement
    """
    output = []
    for l in prop:
        if l in secret:
            if prop.index(l) == secret.index(l):
                output.append(colored('◉', 'green'))
            else:
                output.append(colored('◉', 'blue'))
        else:
            output.append(colored('◉', 'red'))
    return output

def main():
    """Exécute une partie

    Args:
        mot_secret (str): mot à deviner

    Returns:
        jeu (str): 'oui' pour rejouer, autre pour quitter
    """
    mot_secret_accents = dic_accents[randint(0, len(dic_accents)-1)]
    mot_secret = unidecode(mot_secret_accents)
    
    mot_secret_accents = list(mot_secret_accents)
    mot_secret = list(mot_secret)
    
    print("Votre mot est composé de ", len(mot_secret), " lettres.\n")
    
    for chance in range(1,7):
        prop_mot = input_valide(mot_secret, chance)

        if prop_mot == mot_secret:
            print(f"\n{colored('Bravo','green')} ! Vous avez deviné le mot ",
                  *[colored(l.upper(),'green',attrs=['bold']) for l in mot_secret_accents], ".")
            return input("\nPour rejouer entrez 'oui'.\n")

        indices = output(mot_secret, prop_mot)
        
        print(*[colored(l.upper(),attrs=['bold']) for l in prop_mot],sep=' ')
        print(*indices, sep=' ')
    print(f"\n{colored('Dommage','red')}, vous avez épuisé votre nombre de chances.\nLe mot était ",
          *[colored(l.upper(),'red',attrs=['bold']) for l in mot_secret_accents])
    return input("Pour rejouer entrez 'oui'.")


dic_sans_accents = []
for e in dic_accents:
    dic_sans_accents.append(unidecode(e))

print(f"{colored('Trouvez le mot secret en proposant des mots de même taille !',attrs=['bold'])}\nUne lettre est absente du mot secret si marquée {colored('rouge','red')},\nprésente mais au mauvais emplacement avec {colored('bleu','blue')},\net au bon emplacement avec {colored('vert','green')}.\nBonne chance !")
jeu = 'oui'
while jeu == 'oui':
    jeu = main()
print("A bientôt !")