
import tkinter as tk


class AB:
    def __init__(self, racine=[None], gauche=None, droite=None):
        self.racine = racine
        self.gauche = gauche
        self.droite = droite

    def set_gauche(self, gauche):
        self.gauche = gauche

    def set_racine(self, racine):
        self.racine = racine

    def set_droite(self, droite):
        self.droite = droite

    def estVide(self):
        return self.racine == [None]

    def taille(self):
        if self.estVide():
            return 0
        else:
            return 1 + (self.gauche.taille() if self.gauche is not None else 0) + (self.droite.taille() if self.droite is not None else 0)

    def prefixe(self):
        if self.racine is not None:
            print(self.racine)
            if self.gauche is not None:
                self.gauche.prefixe()
            if self.droite is not None:
                self.droite.prefixe()

    def infixe(self):

        if self.gauche is not None:
            self.gauche.infixe()
        print(self.racine)
        if self.droite is not None:
            self.droite.infixe()

    def postfixe(self):
        if not self.estVide():
            if self.gauche is not None:
                self.gauche.postfixe()
            if self.droite is not None:
                self.droite.postfixe()
        print(self.racine)

    def hauteur(self):
        if self.estVide():
            return -1
        else:
            return 1 + max((self.gauche.hauteur() if self.gauche is not None else -1), (self.droite.hauteur() if self.droite is not None else -1))

    def estABR(self):
        if self.estVide():
            return True
        elif self.gauche is None and self.droite is None:
            return True
        elif self.gauche is None:
            return self.droite.racine > self.racine and self.droite.estABR()
        elif self.droite is None:
            return self.gauche.racine < self.racine and self.gauche.estABR()
        else:
            return self.gauche.racine < self.racine < self.droite.racine and self.gauche.estABR() and self.droite.estABR()


A1 = AB()
print("\nest-il vide ?\n")
print(A1.estVide())


A2 = AB(racine=[5])
print("\nest-il vide ?\n")

print(A2.estVide())


A3 = AB(racine=[3])
print("\nest-il vide ?\n")

print(A3.estVide())

A2.set_gauche(A3)
print("\ncreation de Atest")

Atest = AB(racine=[10], gauche=AB(racine=[5], gauche=AB(
    racine=[3]), droite=AB(racine=[8])), droite=AB(racine=[12]))
print("\nest-il vide ?\n")
print(Atest.estVide())
print("\nHauteur : ")
print(Atest.hauteur())
print("\n postfixe ?\n")
print(Atest.postfixe())
print("\n prefixe ?\n")
print(Atest.prefixe())
print("\n infixe ?\n")
print(Atest.infixe())
print("\n Il est ABR ?\n")
print(Atest.estABR())
print("\n test abr\n")
print("\n non abr \n")
AnotABR = AB(4, AB(2, AB(5), AB(3)), AB(6, AB(1), AB(7)))
print(AnotABR.estABR())
print("\n vide donc abr \n")
AnotABR = AB(4, AB(2, AB(5), AB(3)), AB(6, AB(1), AB(7)))
print(A1.estABR())


Atest = AB(racine=[10], gauche=AB(racine=[5], gauche=AB(
    racine=[3]), droite=AB(racine=[8])), droite=AB(racine=[12]))


def dessinerAB(ab, canvas, x, y, ecart):
    if ab is not None:
        canvas.create_oval(x-15, y-15, x+15, y+15,
                           fill='white', outline='black')
        canvas.create_text(x, y, text=str(ab.racine[0]))

        if ab.gauche is not None:
            x_gauche = x - ecart
            y_gauche = y + 50
            canvas.create_line(x, y, x_gauche, y_gauche, arrow='last')
            dessinerAB(ab.gauche, canvas, x_gauche, y_gauche, ecart/2)

        if ab.droite is not None:
            x_droite = x + ecart
            y_droite = y + 50
            canvas.create_line(x, y, x_droite, y_droite, arrow='last')
            dessinerAB(ab.droite, canvas, x_droite, y_droite, ecart/2)


root = tk.Tk()
root.title("Arbre Atest")


canvas = tk.Canvas(root, width=800, height=600)
canvas.pack()

dessinerAB(Atest, canvas, 400, 50, 100)

root.mainloop()
