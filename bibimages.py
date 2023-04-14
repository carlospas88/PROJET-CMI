#-*- coding: utf-8 -*-

import PIL.Image
import sys

image = PIL.Image.Image
couleur = tuple

try:
    import isnotebook
    _is_notebook = isnotebook.isnotebook()
    if _is_notebook:
        print("is notebook")
        import IPython.display
except Exception:
    _is_notebook = False

if sys.hexversion < 3 << 24:
    print("bibimages ne fonctionne qu'avec idle3 (python3), pas avec idle (python)")
    sys.exit(1)



class __ErreurParametre (TypeError):
    def __init__(self, arg, param):
        self.arg = arg
        self.param = param
    def __str__(self):
        # affichage discutable
        if isinstance(self.arg, str):
            strArg = "'" + self.arg + "'"
        else:
            strArg = str (self.arg)
        return "\n\n" + strArg + " n'est pas " + self.param

def __verif_type_image(i):
    if "Image" not in i.__class__.__name__:
        raise __ErreurParametre(i, "une image")

def __verif_type_chaine(s):
    if not isinstance(s, str):
        raise __ErreurParametre(s, "un nom d'image")

def __verif_type_entier(i):
    if i.__class__.__name__ != 'int':
        raise __ErreurParametre(i, "un entier")

def __verif_type_coord(c):
    if c.__class__.__name__ != 'tuple':
        raise __ErreurParametre(c, "des coordonnées (x, y)")
    if c.__len__() != 2:
        raise __ErreurParametre(c, "des coordonnées avec 2 composantes (x, y)")
    if c[0].__class__.__name__ != 'int':
        raise __ErreurParametre(c, "des coordonnées entières (x, y)")
    if c[1].__class__.__name__ != 'int':
        raise __ErreurParametre(c, "des coordonnées entières (x, y)")

def __verif_coords(img,x,y):
    if x < 0:
        raise Exception("La coordonnée x est strictement inférieure à 0")
    if y < 0:
        raise Exception("La coordonnée y est strictement inférieure à 0")
    if x >= largeurImage(img):
        raise Exception("La coordonnée x est supérieur à la largeur de l'image")
    if y >= hauteurImage(img):
        raise Exception("La coordonnée y est supérieur à la hauteur de l'image")

def __verif_type_couleur(c):
    if c.__class__.__name__ != 'tuple':
        raise __ErreurParametre(c, "une couleur (R, G, B)")
    if c.__len__() != 3:
        raise __ErreurParametre(c, "une couleur avec 3 composantes (R, G, B)")
    if c[0].__class__.__name__ != 'int':
        raise __ErreurParametre(c, "une couleur avec 3 composantes entières (R, G, B)")
    if c[1].__class__.__name__ != 'int':
        raise __ErreurParametre(c, "une couleur avec 3 composantes entières (R, G, B)")
    if c[2].__class__.__name__ != 'int':
        raise __ErreurParametre(c, "une couleur avec 3 composantes entières (R, G, B)")

def _errMaj(wrong, right):
    raise Exception("Attention aux majuscules/minuscules: la fonction " + wrong + " n'existe pas, c'est la fonction " + right + " qui existe")

def _errS(wrong, right):
    raise Exception("Attention aux s: la fonction " + wrong + " n'existe pas, c'est la fonction " + right + " qui existe")

def ouvrirImage(nom: str) -> image:
    """ Ouvre le fichier nom et retourne l’image contenue dedans
    Par exemple:

    >>> img = ouvrirImage('teapot.png')"""
    __verif_type_chaine(nom)
    try:
        return PIL.Image.open(nom).convert("RGB")
    except FileNotFoundError as e:
        raise Exception("Attention, le fichier " + nom + " n'existe pas, peut-être le nom est mal écrit, ou bien ce fichier n'est pas dans le même répertoire que le fichier .py ?")

def ouvririmage(nom: str) -> image:
    _errMaj("ouvririmage", "ouvrirImage")
def OuvrirImage(nom: str) -> image:
    _errMaj("OuvrirImage", "ouvrirImage")
def ouvrirImages(nom: str) -> image:
    _errS("ouvrirImages", "ouvrirImage")
def ouvririmages(nom: str) -> image:
    _errS("ouvririmages", "ouvrirImage")

def ecrireImage(img: image, nom: str) -> None:
    """Sauvegarde l’image img dans le fichier nom
    Par exemple:

    >>> ecrireImage(img, "monimage.png")"""
    __verif_type_image(img)
    __verif_type_chaine(nom)
    PIL.Image.Image.save(img, nom)

def ecrireimage(img: image, nom: str) -> None:
    _errMaj("ecrireimage", "ecrireImage")
def EcrireImage(img: image, nom: str) -> None:
    _errMaj("EcrireImage", "ecrireImage")
def ecrireImages(img: image, nom: str) -> None:
    _errS("ecrireImages", "ecrireImage")
def ecrireimages(img: image, nom: str) -> None:
    _errS("ecrireimages", "ecrireImage")

def nouvelleImage(largeur: int, hauteur: int) -> image:
    """ Retourne une image de taille largeur × hauteur, initialement noire
    Par exemple:

    >>> img = nouvelleImage(300,200)"""
    __verif_type_entier(largeur)
    __verif_type_entier(hauteur)
    return PIL.Image.new ("RGB", (largeur, hauteur))

def nouvelleimage(largeur: int, hauteur: int) -> image:
    _errMaj("nouvelleimage", "nouvelleImage")
def NouvelleImage(largeur: int, hauteur: int) -> image:
    _errMaj("NouvelleImage", "nouvelleImage")
def nouvelleImages(largeur: int, hauteur: int) -> image:
    _errS("nouvelleImages", "nouvelleImage")
def nouvelleimages(largeur: int, hauteur: int) -> image:
    _errS("nouvelleimages", "nouvelleImage")

def afficherImage(img):
    """ Affiche l’image img
    Par exemple:

    >>> afficherImage(img)"""
    __verif_type_image(img)
    try:
        if _is_notebook:
            IPython.display.display(img)
        else:
            PIL.Image.Image.show(img)
    except Exception:
    	print("Affichage non disponible")

def afficherimage(img) -> None:
    _errMaj("afficherimage", "afficherImage")
def AfficherImage(img) -> None:
    _errMaj("AfficherImage", "afficherImage")
def afficherImages(img) -> None:
    _errS("afficherImages", "afficherImage")
def afficherimages(img) -> None:
    _errS("afficherimages", "afficherImage")

def largeurImage(img) -> int:
    """ Récupère la largeur de img
    Par exemple:

    >>> l = largeurImage(img)"""
    __verif_type_image(img)
    return img.width

def largeurimage(img) -> int:
    _errMaj("largeurimage", "largeurImage")
def LargeurImage(img) -> int:
    _errMaj("LargeurImage", "largeurImage")
def largeurImages(img) -> int:
    _errS("largeurImages", "largeurImage")
def largeurimages(img) -> int:
    _errS("largeurimages", "largeurImage")

def hauteurImage(img) -> int:
    """ Récupère la hauteur de img
    Par exemple:

    >>> h = hauteurImage(img)"""
    __verif_type_image(img)
    return img.height

def hauteurimage(img) -> int:
    _errMaj("hauteurimage", "hauteurImage")
def HauteurImage(img) -> int:
    _errMaj("HauteurImage", "hauteurImage")
def hauteurImages(img) -> int:
    _errS("hauteurImages", "hauteurImage")
def hauteurimages(img) -> int:
    _errS("hauteurimages", "hauteurImage")


def colorierPixel(img: image, x: int, y: int, c: couleur) -> None:
    """ Peint le pixel de coordonnées (x,y) dans l’image img de la couleur c
    Exemple d'utilisation :

    >>> colorierPixel(img, 50,50, (255,255,255))
    """
    __verif_type_image(img)
    __verif_type_entier(x)
    __verif_type_entier(y)
    __verif_coords(img,x,y)
    __verif_type_couleur(c)
    img.putpixel((x,y), c)

def colorierpixel(img: image, x: int, y: int, c: couleur) -> None:
    _errMaj("colorierpixel", "colorierPixel")
def ColorierPixel(img: image, x: int, y: int, c: couleur) -> None:
    _errMaj("ColorierPixel", "colorierPixel")
def colorierPixels(img: image, x: int, y: int, c: couleur) -> None:
    _errS("colorierPixels", "colorierPixel")
def colorierpixels(img: image, x: int, y: int, c: couleur) -> None:
    _errS("colorierpixels", "colorierPixel")

def couleurPixel (img: image, x: int, y: int) -> couleur:
    """ Retourne la couleur du pixel (x, y) dans l’image img
    Exemple d'utilisation :

    >>> c = couleurPixel(img, 50,50)
    """
    __verif_type_image(img)
    __verif_type_entier(x)
    __verif_type_entier(y)
    __verif_coords(img,x,y)
    return img.getpixel((x,y))

def couleurpixel(img: image, x: int, y: int) -> couleur:
    _errMaj("couleurpixel", "couleurPixel")
def CouleurPixel(img: image, x: int, y: int) -> couleur:
    _errMaj("CouleurPixel", "couleurPixel")
def couleurPixels(img: image, x: int, y: int) -> couleur:
    _errS("couleurPixels", "couleurPixel")
def couleurpixels(img: image, x: int, y: int) -> couleur:
    _errS("couleurpixels", "couleurPixel")

print("bibimages.py")
