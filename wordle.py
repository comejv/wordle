from random import randint
from termcolor import colored
from unidecode import unidecode
from dic import dic_accents

def input_valide(secret: str, tour: int):
    """Prend une entrée standard et la renvoie quand elle satisfait les conditions

    Args:
        secret (str): mot à deviner

    Returns:
        tuple: mot sans accents et mot avec accents du dic
    """
    prop = unidecode(input(f"Proposition {tour}/6 :\n"))

    while not(prop in dic_sans_accents) or len(prop) != len(secret):
        if not(prop in dic_sans_accents):
            prop = input("Votre mot n'est pas dans notre dictionnaire, réessayez :\n")
        elif len(prop) < len(secret):
            prop = input("Mot trop court :\n")
        elif len(prop) > len(secret):
            prop = input("Mot trop long :\n")
    
    return (list(prop),list(dic_accents[dic_sans_accents.index(prop)]))

def output(secret: list, prop: list):
    """Donne les indices pour chaque lettre

    Args:
        secret (list): mot secret à deviner
        prop (list): mot proposé par le joueur

    Returns:
        output (list): rouge mauvaise lettre, bleu mauvais emplacement, vert bon emplacement
    """
    output = []
    secret_sans_accent = [unidecode(l) for l in secret]
    for i in range(len(secret)):
        if unidecode(secret[i])==unidecode(prop[i]):
            output.append(colored('◉', 'green'))
        elif unidecode(prop[i]) in secret_sans_accent:
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

        if prop_mot[0] == mot_secret:
            print(f"\n{colored('Bravo','green')} ! Vous avez deviné le mot ",
                  *[colored(l.upper(),'green',attrs=['bold']) for l in mot_secret_accents], ".")
            return input("\nPour rejouer entrez 'oui'.\n")

        indices = output(mot_secret, prop_mot[0])
        
        print(*[colored(l.upper(),attrs=['bold']) for l in prop_mot[1]],sep=' ')
        print(*indices, sep=' ')
    print(f"\n{colored('Dommage','red')}, vous avez épuisé votre nombre de chances.\nLe mot était ",
          *[colored(l.upper(),'red',attrs=['bold']) for l in mot_secret_accents])
    return input("Pour rejouer entrez 'oui'.\n")


dic_sans_accents = []
for e in dic_accents:
    dic_sans_accents.append(unidecode(e))

print(f"{colored('Trouvez le mot secret en proposant des mots de même taille !',attrs=['bold'])}\nUne lettre est absente du mot secret si marquée {colored('rouge','red')},\nprésente mais au mauvais emplacement avec {colored('bleu','blue')},\net au bon emplacement avec {colored('vert','green')}.\nBonne chance !")
jeu = 'oui'
while jeu == 'oui':
    jeu = main()
print("A bientôt !")
