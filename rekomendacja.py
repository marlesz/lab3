#  Wzorowane na przykładzie Rona Zacharskiego
#

from math import sqrt
import numpy

users = {
        "Ania": 
            {"Blues Traveler": 1.,
            "Broken Bells": 1.5,
            "Norah Jones": 2,
            "Deadmau5": 2.5,
            "Phoenix": 3.0,
            "Slightly Stoopid": .5,
            "The Strokes": 0.0,
            "Vampire Weekend": 2.0},
         "Bonia":
            {"Blues Traveler": 4.0,
            "Broken Bells": 4.5, 
            "Norah Jones": 5.0,
            "Deadmau5": 5.5, 
            "Phoenix": 6.0, 
            "Slightly Stoopid": 3.5, 
            "The Strokes": 2.0,
            "Vampire Weekend": 5.0}
        }

        
def manhattan(rating1, rating2):
    
    """Oblicz odległość w metryce taksówkowej między dwoma  zbiorami ocen
       danymi w postaci: {'The Strokes': 3.0, 'Slightly Stoopid': 2.5}
       Zwróć -1, gdy zbiory nie mają… wspólnych elementów"""
       
    # TODO: wpisz kod
    klucze1 = rating1.keys()
    klucze2 = rating2.keys()
    odleglosc = 0
    udaloSiePorownac = False

    for klucz in klucze1:
        if klucz in rating2.keys():
            udaloSiePorownac = True
            odleglosc = odleglosc + abs(rating2[klucz] - rating1[klucz])

    if (udaloSiePorownac==True):
        return odleglosc
    else:
        return -1

def pearson(rating1, rating2):
    klucze1 = rating1.keys()
    klucze2 = rating2.keys()
    udaloSiePorownac = False
    korelacja=0
    n=0
    xy = 0
    x=0
    y=0
    x2 = 0
    y2 = 0
    for klucz in klucze1:
        if klucz in rating2.keys():
            udaloSiePorownac = True
            n += 1
            xy += rating1[klucz]*rating2[klucz]
            x += rating1[klucz]
            y += rating2[klucz]
            x2 += (rating1[klucz])**2
            y2 += (rating2[klucz])**2


    if (udaloSiePorownac==True):
        korelacja = (xy - (x*y)/n)/((sqrt(x2-(x**2)/n))*(sqrt(y2 - (y**2)/n)))
        return korelacja
    else:
        return -1

def pearsonNumpy(rating1, rating2):
    
    korelacja=0
    klucze1 = rating1.keys()
    klucze2 = rating2.keys()
    udaloSiePorownac = False
    x=[]
    y=[]
    for klucz in klucze1:
        if klucz in rating2.keys():
            udaloSiePorownac = True
            x.append(rating1[klucz])
            y.append(rating2[klucz])

    if (udaloSiePorownac==True):
        korelacja = numpy.corrcoef(x,y)[0,1]
        return korelacja
    else:
        return -1


#print "Wartość odległości manhattan dla preferncji Boni i Ani wynosi: " + str(manhattan(users["Bonia"],users["Ania"]))
#print "Wartość korelacji między preferencjami Boni i Ani, obliczona z przybliżonego wzoru na współczynnik koleracji Pearsona wynosi: "+ str(pearson(users["Bonia"],users["Ania"]))
#print "Korelacja obliczona dla preferencji Boni i Ani z numpy - funkcja corrcoef wynosi: " + str(pearsonNumpy(users["Bonia"],users["Ania"])[0][1])

print "Odległosć Manhattan wynosi: " + str(manhattan(users["Ania"],users["Bonia"]))
print "Współczynnik korelacji Pearsona z obliczeń wynosi: " + str(pearson(users["Ania"],users["Bonia"]))
print "Współczynnik korelacji Pearsona z Numpy (corrcoef) wynosi: " +str(pearsonNumpy(users["Ania"],users["Bonia"]))
print "Gusta Ani i Boni są podobne - współczynnik korelacji bliski 1. Współczynniki Pearsona z obliczeń i z wykorzystaniem biblioteki Numpy nie różnią się."