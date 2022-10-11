from datetime import date

from joueur import Joueur
from sexe import Sexe
from tournoi import Tournoi
from match import Match

def main():
    joueur  = Joueur("a", "a", date.today(), Sexe.HOMME, 2500)
    print(joueur)
    joueur.__nom = "b"
    print(joueur)

if __name__=="__main__":
    main()

