# fragmenty dotyczące rozwiązania poszczególnych zadań proszę oddzielić odpowiednimi komentarzami

#Zadanie_2

from array import *

m_array = array('u', [])

number = int(input('Podaj ilość wprowadzanych znakow: '))
ii = 0
while ii < number:
    m_array.append(input('Wprowadz znak: '))
    ii += 1

for i in reversed(m_array):
    print(i)


#Zadanie_3

from array import * 
import random

print('Podaj ilosc znaków, ktore wylosować do tablicy: ')
number = input()

tab = array('f',[5])
for i in range(0,int(number)):
    tab.append(random.uniform(-5,5))


plik = open("result.txt","w")
for i in tab:
    plik.write(str(i)+", ")


#Zadanie_4

import numpy as numpy

def funkcja():
    tab = numpy.array(
        [[2, 3, 4, 5, 6], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])  
    i = 1
    while i < 5:
        for j in range(5):
            tab[i][j] = pow(tab[i - 1][j], 2)                                                   
        i += 1
    return tab

print(funkcja())


#Zadanie_5

import collections

def histogram(nazwa):
    plik = open(nazwa,"r")
    text = plik.readline()
    c = collections.Counter(text)
    return c
print(histogram("document.txt"))


#Zadanie_6

import random

def deck():
    talia = []
    rangi = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'D', 'K', 'A']
    kolory = ['c', 'd', 'h', 's']
    for i in rangi:
        for l in kolory:
            talia.append((i, l))
    return talia


def shuffle_deck(deck):
    random.shuffle(deck)
    return deck


def deal(deck, n):
    stolik = []
    for i in range(0, n):
        stolik.append(random.sample(deck, 5))
    return stolik


talia = deck()
potasowanaTalia = shuffle_deck(talia)
print('Podaj ilość graczy przy stole: ')
liczba_graczy = int(input())
rozdanie_dla_graczy = deal(potasowanaTalia,liczba_graczy )
print(rozdanie_dla_graczy)
