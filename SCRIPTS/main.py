import logging
logger = logging.getLogger(__name__)
logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)

def show_complete_grid():
    nb_col = int(input("Nombre de colonnes : "))
    nb_lig = int(input("Nombre de lignes : "))

    vals_col = input(f"Colonnes (séparées par /) : ")
    vals_lig = input(f"Lignes (séparées par /) : ")

    logging.info(f"Initalisation grille {nb_col} x {nb_lig}")

    vals_col = clean_input_user(vals_col)
    vals_lig = clean_input_user(vals_lig)

    logging.debug(f"Nettoyage des données de colonnes : {vals_col}")
    logging.debug(f"Nettoyage des données de lignes : {vals_lig}")

    logging.debug(f"Validation des données utilisateur")
    check_user_input(nb_col, nb_lig, vals_col, vals_lig)




def clean_input_user(entry: str):
    """Méthode utilisée pour nettoyer les données d'entrées de l'utilisateur.
    L'utilisateur doit fournir les données de ligne et de colonne, séparées par des '/' (pour délimiter chaque colonne et chaque ligne).
    Au sein d'une même ligne (ou colonne), les blocs doivent être délimités par des virgules.

    Args:
        entry (str): La donnée utilisateur, par exemple : "1,2/4,5,2/4". Ce qui signifie qu'il y a un bloc de 1 et un bloc de 2
        sur la 1ère colonne puis un bloc de 4, un bloc de 5 et un bloc de 2 sur la 2ème colonne, etc...

    Returns:
        list: Les données nettoyer, par exemple [[1,2], [4,5,2], [2,4]]
    """

    entry = entry.strip()
    entries = entry.split('/')
    return [elem.split(',') for elem in entries]

def check_user_input(nb_col, nb_lig, input_col, input_lig):
    """Méthode utilisée pour s'assurer que le nombre de ligne et de colonne correspondent bien à la longueur des données
    d'entrées saisies par l'utilisateur.

    Args:
        nb_col (int): Nombre de colonnes indiquée par l'utilisateur.
        nb_lig (int): Nombre de lignes indiquée par l'utilisateur.
        input_col (list): Les données d'entrées de colonnes saisies par l'utilisateur.
        input_lig (list): Les données d'entrées de lignes saisies par l'utilisateur.

    Raises:
        ValueError: Dans le cas où les dimensions ne correspondent pas aux données d'entrées.
    """

    if int(nb_col) != len(input_col) or int(nb_lig) != len(input_lig):
        logging.critical(f"Données d'entrées non raccord avec les dimensions de la grille !")
        raise ValueError("Erreur !\nLes données d'entrées de lignes et de colonnes ne correspondent pas aux dimensions de la grille indiquée.")


if __name__ == '__main__':
    show_complete_grid()