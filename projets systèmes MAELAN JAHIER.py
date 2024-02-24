
from turtle import *
from pileNonBornee import *


speed("fastest")


speed("fastest")
# Permet de faire le dessin instantanément


# Fonctions avec exemples dans
#les done() permettent de garder la fenêtre ouverte après l'execution des exemples

def traceLsysteme(mot, angle, echelle):
    down()
    pile = Pile(None)
    for i in range(len(mot)):
        if mot[i] == "A" or mot[i] == "B" :
            forward(100 * echelle)      
        elif mot[i] == "a" : #modifications du 4.1)
            up()
            forward(100 * echelle)
            down()
        elif mot[i] == "g" :
            left(angle)
        elif mot[i] == "d" :
            right(angle)
        elif mot[i] == "[" :
            pile.empile(position())
            pile.empile(heading())
        elif mot[i] == "]" :
            up()
            setheading(pile.depile())
            goto(pile.depile())
            down()
    update()
    up()


def remplacer1(mot, lettre, motif):
    mot2 = ""
    for i in range(len(mot)):
        if mot[i] == lettre :
            mot2 += motif
        else :
            mot2 += mot[i]
    return mot2

#mot="BgAdB"
#print(remplacer1(mot,"A","ABA"))


def itereLsysteme1(depart, regle, k):
    for _ in range(k):
        depart = remplacer1(depart, regle[0], regle[1])
    return depart


# 1

#traceLsysteme("AgAdAAdAdA",90,1)
#done()

#traceLsysteme("AgAdAAdAdA",60, 0.5)
#done()

#traceLsysteme("AgAdAAdAdA",100,1)
#done()

#traceLsysteme("AgAdAAdAdA",90,2)
#done()

#traceLsysteme(echelle=0.5, mot="AgAdAAdAdA" ,angle=100)
#done()

#traceLsysteme("AgAdAAdAdA", 100, 0.5)
#done()








# 2

"""
up()
goto(-300, -300)
down()
traceLsysteme(itereLsysteme1("A", ("A", "AgAdAdAgA"), 5), 90, 1/(2**5))
done()


"""
#traceLsysteme(itereLsysteme1("AdAdAdA", ("A", "AgAgAAdAdAg"), 3), 90, 1/8)
#done()

#traceLsysteme(itereLsysteme1("AdAdAdA", ("A","AAdAdAdAdAdAgA"), 3), 90, 1/8)
#done()

#traceLsysteme(itereLsysteme1("AdAdAdA", ("A", "AAdAAdAdAgAgAAdAdAgAgAAgAAdA"), 3), 90, 1/8)
#done()

#traceLsysteme(itereLsysteme1("AdAdAdA", ("A", "AdAgAdAdAA"), 3), 90, 1/8)
#done()

#traceLsysteme(itereLsysteme1("AdAdAdA", ("A", "AdAdAdAdAdAgA"), 3), 90, 1/8)
#done()

#traceLsysteme(itereLsysteme1("AdAdAdA", ("A", "AdAAddAdA"), 3), 90, 1/8)
#done()

#traceLsysteme(itereLsysteme1("AdAdAdA", ("A", "AAdAddAdA"), 3), 90, 1/8)
#done()

#traceLsysteme(itereLsysteme1("AdAdAdA", ("A", "AdAgAdAdA"), 3), 90, 1/8)
#done()


def remplacer2(mot, lettre1, motif1, lettre2, motif2):
    mot2 = ""
    for i in range(len(mot)):
        if mot[i] == lettre1 :
            mot2 += motif1
        elif mot[i] == lettre2 :
            mot2 += motif2
        else :
            mot2 += mot[i]
    return mot2


def itereLsysteme2(depart,regle1,regle2,k):

    for _ in range(k):
        depart = remplacer2(depart, regle1[0], regle1[1], regle2[0], regle2[1])
    return depart

# 3

"""
up()
goto(-150, -150)
down()
"""


#Triangle de Sierpinski
#traceLsysteme(itereLsysteme2("AdBdB", ("A", "AdBgAgBdA"),("B", "BB"), 5), -120, 1/(5 + 1))
#done()

#La Courbe du dragon
#traceLsysteme(itereLsysteme2("AX", ("X", "XgYAg"),("Y", "dAXdY"), 10), 90, 1/(10 + 1))
#done()

# Une variante du triangle de Sierpinski 
#traceLsysteme(itereLsysteme2("A", ("A", "BdAdB"),("B", "AgBgA"), 5), 60, 1/10)
#done()

# La courbe de Gosper
#traceLsysteme(itereLsysteme2("A", ("A", "AgBggBdAddAAdBg"),("B", "dAgBBggBgAddAdB"), 3), 60, 1/10)
#done()





# 4
#Exemple  :

up()
goto(-120, 60)
down()
depart="AdAdAdA"
regle1=("A","AgadAAgAgAAgAagAAdagAAdAdAAdAadAAA")
regle2=("a","aaaaaa")

traceLsysteme(itereLsysteme2(depart, regle1,regle2, 2), 90, 1/25)
done()



# Exemple 4.2

left(90)  #permet que la tige soit verticale et non horizontale





#traceLsysteme(itereLsysteme1("A", ("A", "A[gA]A[dA]A"), 2), 20, 1/2)
#done()

#traceLsysteme(itereLsysteme1("A", ("A", "A[gA]A[dA][A]"), 2), 20, 1/2)
#done()
"""
up()
goto(-10, -350)
down()
traceLsysteme(itereLsysteme1("A", ("A", "AAd[dAgAgA]g[gAdAdA]"), 2), 20, 1/2)
done()
"""



"""
up()
goto(-10, -450)
down()
traceLsysteme(itereLsysteme2("X", ("X", "A[gX][X]A[gX]dAX"), ("A", "AA"), 5), 20, 1/10)
done()

"""

"""

up()
goto(-10, -350)
down()
traceLsysteme(itereLsysteme2("X", ("X", "A[gX]A[dX]AX"), ("A", "AA"), 5), 20, 1/16)
done()
"""


"""up()
goto(-10, -450)
down()
traceLsysteme(itereLsysteme2("X", ("X", "Ad[[X]gX]gA[gAX]dX"), ("A", "AA"), 5), 20, 1/10)
done()"""




