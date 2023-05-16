#RPG GECKO

from time import*
import sys
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os
import numpy
import random
import pandas as pd
from playsound import playsound
import pygame 

def musique_mennu():
    pygame.mixer.init()  # Initialisation du mixer
    global musique_menu
    musique_menu = pygame.mixer.Sound("Soundtrack/Metroid Dread Main Theme OST - Super Metroid.mp3")
    musique_menu.set_volume(0.3)
    musique_menu.play()
    


pts_explox = [100,170,270,400,350,450]
pts_exploy = [300,300,270,280,200,100]



nom_explo = ['Désert de la mort','Marécage du roi slime','Montagnes du zero absolu','Forêt de ténèbris','Plaines infinies','Rivère du léviathan']



#TEXTE ET DIVERS
def transf(string):
    L = []
    for i in string:
        L.append(i)
    return(L)  
def ecriture(string):
    
    L = transf(string)
    for i in range(0,len(L)):            
        print(L[i],end='')
        sys.stdout.flush()
        sleep(0.03)
    return('')     
def show_image(lien):
    plt.imshow(mpimg.imread(lien))
    plt.axis('off')
    plt.show()     
def show_imageetpoint(lien,x,y):
    plt.imshow(mpimg.imread(lien))
    plt.plot(x,y,marker = 'v', color = 'red',markersize=10)
    plt.axis('off')
    plt.show() 

#OBJETS, JOUEUR ET EVENT
class mob:
    def __init__(self,nom,pv,dps,capacite1,capacite2,capacite3,xpkill):
        self.nom = nom
        self.pv = pv
        self.dps = dps
        self.capacite1 = capacite1   
        self.capacite2 = capacite2  
        self.capacite2 = capacite2
        self.xpkill = xpkill
    
        
class geckoP:
    pv = 200
    class stats:
        
        xp = 10
        frc = 10
        end = 10
        dxt = 10
        inte = 10  
        pv = end*10
    def __init__(self, nom):
        self.nom = nom
        print(f'Invoquation du Gecko :{nom}')
        print('')     
        print(ecriture('[===================================]'))
        print('')
        print('Invoquation terminée')
        print('')
    def rename(self,nv_nom):
        self.nom = nv_nom
        print(f'Votre gecko à été renommé {nv_nom}')
        print('')
    
#ARMES

#ENNEMIS

liste_mob = pd.read_excel('C:/Users/erwan/Desktop/GeckoArtOnline/moblist.xlsx')
mob_names = liste_mob['NOM']
mob_pv = liste_mob['PV']
mob_dps = liste_mob['DPS']
mob_cap1 = liste_mob['CAPA1']
mob_cap2 = liste_mob['CAPA2']           #FONCTIONNE COMME DES LISTES
mob_cap3 = liste_mob['CAPA3']
mob_xp = liste_mob['PV']


#INITIALISATION DE TOUT LES MOBS

i=0
cactus = mob(mob_names[i], mob_pv[i], mob_dps[i], mob_cap1[i], mob_cap2[i],mob_cap2[i],mob_xp[i])
i=1
taliban = mob(mob_names[i], mob_pv[i], mob_dps[i], mob_cap1[i], mob_cap2[i],mob_cap2[i],mob_xp[i])
i=2
ver = mob(mob_names[i], mob_pv[i], mob_dps[i], mob_cap1[i], mob_cap2[i],mob_cap2[i],mob_xp[i])
i=3
tank = mob(mob_names[i], mob_pv[i], mob_dps[i], mob_cap1[i], mob_cap2[i],mob_cap2[i],mob_xp[i])
i=4
dio = mob(mob_names[i], mob_pv[i], mob_dps[i], mob_cap1[i], mob_cap2[i],mob_cap2[i],mob_xp[i])
i=5
slime = mob(mob_names[i], mob_pv[i], mob_dps[i], mob_cap1[i], mob_cap2[i],mob_cap2[i],mob_xp[i])
i=6
Sorcière = mob(mob_names[i], mob_pv[i], mob_dps[i], mob_cap1[i], mob_cap2[i],mob_cap2[i],mob_xp[i])
i=7
Zombie = mob(mob_names[i], mob_pv[i], mob_dps[i], mob_cap1[i], mob_cap2[i],mob_cap2[i],mob_xp[i])
i=8
Kraken = mob(mob_names[i], mob_pv[i], mob_dps[i], mob_cap1[i], mob_cap2[i],mob_cap2[i],mob_xp[i])
i=9
Bigdoggo = mob(mob_names[i], mob_pv[i], mob_dps[i], mob_cap1[i], mob_cap2[i],mob_cap2[i],mob_xp[i])
i=10
Bonhomedeneige = mob(mob_names[i], mob_pv[i], mob_dps[i], mob_cap1[i], mob_cap2[i],mob_cap2[i],mob_xp[i])
i=11
Loupdesneiges = mob(mob_names[i], mob_pv[i], mob_dps[i], mob_cap1[i], mob_cap2[i],mob_cap2[i],mob_xp[i])
i=12
yeti = mob(mob_names[i], mob_pv[i], mob_dps[i], mob_cap1[i], mob_cap2[i],mob_cap2[i],mob_xp[i])
i=13
EnfantdeDragon = mob(mob_names[i], mob_pv[i], mob_dps[i], mob_cap1[i], mob_cap2[i],mob_cap2[i],mob_xp[i])
i=14
Dragon = mob(mob_names[i], mob_pv[i], mob_dps[i], mob_cap1[i], mob_cap2[i],mob_cap2[i],mob_xp[i])
i=15
LechevalierTuba = mob(mob_names[i], mob_pv[i], mob_dps[i], mob_cap1[i], mob_cap2[i],mob_cap2[i],mob_xp[i])
i=16
LeTireurTuba = mob(mob_names[i], mob_pv[i], mob_dps[i], mob_cap1[i], mob_cap2[i],mob_cap2[i],mob_xp[i])
i=17
assasintuba = mob(mob_names[i], mob_pv[i], mob_dps[i], mob_cap1[i], mob_cap2[i],mob_cap2[i],mob_xp[i])
i=18
Les2mercenaires = mob(mob_names[i], mob_pv[i], mob_dps[i], mob_cap1[i], mob_cap2[i],mob_cap2[i],mob_xp[i])
i=19
Tubalovania = mob(mob_names[i], mob_pv[i], mob_dps[i], mob_cap1[i], mob_cap2[i],mob_cap2[i],mob_xp[i])
i=20
Amogus = mob(mob_names[i], mob_pv[i], mob_dps[i], mob_cap1[i], mob_cap2[i],mob_cap2[i],mob_xp[i])
i=21
Morshu = mob(mob_names[i], mob_pv[i], mob_dps[i], mob_cap1[i], mob_cap2[i],mob_cap2[i],mob_xp[i])
i=22
Rat = mob(mob_names[i], mob_pv[i], mob_dps[i], mob_cap1[i], mob_cap2[i],mob_cap2[i],mob_xp[i])
i=23
SonGoku = mob(mob_names[i], mob_pv[i], mob_dps[i], mob_cap1[i], mob_cap2[i],mob_cap2[i],mob_xp[i])
i=24
Gigachad = mob(mob_names[i], mob_pv[i], mob_dps[i], mob_cap1[i], mob_cap2[i],mob_cap2[i],mob_xp[i])
i=25
uneMeduse = mob(mob_names[i], mob_pv[i], mob_dps[i], mob_cap1[i], mob_cap2[i],mob_cap2[i],mob_xp[i])
i=26
Kappa = mob(mob_names[i], mob_pv[i], mob_dps[i], mob_cap1[i], mob_cap2[i],mob_cap2[i],mob_xp[i])
i=27
SpaceMarine = mob(mob_names[i], mob_pv[i], mob_dps[i], mob_cap1[i], mob_cap2[i],mob_cap2[i],mob_xp[i])
i=28
Armonstrong = mob(mob_names[i], mob_pv[i], mob_dps[i], mob_cap1[i], mob_cap2[i],mob_cap2[i],mob_xp[i])
i=29
Sakuya = mob(mob_names[i], mob_pv[i], mob_dps[i], mob_cap1[i], mob_cap2[i],mob_cap2[i],mob_xp[i])




#GAMEPLAY
def takedamage(dmg):
    gecko.stats.pv = gecko.stats.pv-dmg
    return(dmg)
    
def menu():
    
    print("----------------------------------------------------------")
    c = input(f'1 : Statistique de {gecko.nom}\n2 : Renommmer {gecko.nom}\n3 : Améliorer {gecko.nom}\n4 : Afficher la carte\n5 : Explorer\n6 : Quitter\n----------------------------------------------------------\n  : ')

    if c == '1':
        afficherstat()
    if c == '2':
        nv_nom = str(input('Entrez le nouveau nom'))
        gecko.rename(nv_nom)
        menu()
    if c == '3':
        choixstat()
    if c == '4':
        plt.imshow(mpimg.imread('C:/Users/erwan/Desktop/GeckoArtOnline/map.png'))
        plt.axis('off')
        plt.show()
        menu()
    if c == '5':
        exploration()
    if c == '6':
        musique_menu.stop()
        sys.exit(0)
    else:
        menu()
        
def rencontredesert(p):
    i=0
    cactus = mob(mob_names[i], mob_pv[i], mob_dps[i], mob_cap1[i], mob_cap2[i],mob_cap2[i],mob_xp[i])
    i=1
    taliban = mob(mob_names[i], mob_pv[i], mob_dps[i], mob_cap1[i], mob_cap2[i],mob_cap2[i],mob_xp[i])
    i=2
    Ver = mob(mob_names[i], mob_pv[i], mob_dps[i], mob_cap1[i], mob_cap2[i],mob_cap2[i],mob_xp[i])
    i=3
    Tank = mob(mob_names[i], mob_pv[i], mob_dps[i], mob_cap1[i], mob_cap2[i],mob_cap2[i],mob_xp[i])
    i=4
    Dio = mob(mob_names[i], mob_pv[i], mob_dps[i], mob_cap1[i], mob_cap2[i],mob_cap2[i],mob_xp[i])
    
    if p == 0:
        cactuss()
    if p == 1:
        talibann()
    if p == 2:
        verr()
    if p == 3:
        tankk()
    if p == 4:
        dioo()
        
        
def cactuss():
    
    print(ecriture(f'Vous tombez face à {cactus.nom}'))
    #afficher fond desert + cactus + barre de vie + stats
    show_image('C:/Users/erwan/Desktop/GeckoArtOnline/texture/zonesdesert/cactus.png')
    j  = 0
    while cactus.pv >= 0:
        j = j+1
        sleep(1)
        print('--------------------------------')
        print(ecriture(f'Tour {j}'))
    
        
        r = random.random() #Tour du cactus
        if r > 0.5:
            print(ecriture(f'Cactus utilise {cactus.capacite1}'))
            i = round(takedamage(0))
            print(ecriture(f'{gecko.nom} perd {i} PV,       PV Restant : {gecko.stats.pv}'))
        else:
            print(ecriture(f'Cactus utilise {cactus.capacite2}'))
            i = round(takedamage(cactus.dps))
            print(ecriture(f'{gecko.nom} perd {i} PV,       PV Restant : {gecko.stats.pv}'))
        sleep(1)    
        if gecko.stats.pv <= 0:
            break
        g = random.random()  #Tour du gecko, g est la précision lié à la dextérité
        cactus.pv = cactus.pv - round(10*g*gecko.stats.frc)
        print(ecriture(f'{gecko.nom} attaque!'))
        if cactus.pv > 0:
            print(ecriture(f'Cactus perd {round(10*g*gecko.stats.frc)} PV,    PV de Cactus : {cactus.pv}' ))
        else:
            print(ecriture(f'Cactus perd {round(10*g*gecko.stats.frc)} PV'))
            print(ecriture('Cactus a été vaincu'))
        
    if gecko.stats.pv <= 0:
        print(ecriture(f'Votre Gecko a péri au combat, vous rentrez à la base sans récompense'))
        menu()
    else:
        show_image('C:/Users/erwan/Desktop/GeckoArtOnline/texture/zonesdesert/desert.png')
        desert(1)
def talibann():
    
    print(ecriture(f'Vous tombez face à des Talibans, ils agitent leurs armes face à votre Gecko!'))
    #afficher fond desert + cactus + barre de vie + stats
    show_image('C:/Users/erwan/Desktop/GeckoArtOnline/texture/zonesdesert/taliban.png')
    j  = 0
    while taliban.pv >= 0:
        j = j+1
        sleep(1)
        print('--------------------------------')
        print(ecriture(f'Tour {j}'))
    
        
        r = random.random() #Tour du cactus
        if r > 0.5:
            print(ecriture(f'Taliban utilise {taliban.capacite1}'))
            i = round(takedamage(taliban.dps))
            print(ecriture(f'{gecko.nom} perd {i} PV,       PV Restant : {gecko.stats.pv}'))
        else:
            print(ecriture(f'taliban utilise {taliban.capacite2}'))
            i = round(takedamage((taliban.dps)*2))
            taliban.pv = taliban.pv - round(50)
            print(ecriture(f'{gecko.nom} perd {i} PV,  Talibans perdent 50 PV,      PV Restant : {gecko.stats.pv}'))
        sleep(1)    
        if gecko.stats.pv <= 0:
            break
        g = random.random()  #Tour du gecko, g est la précision lié à la dextérité
        taliban.pv = taliban.pv - round(10*g*gecko.stats.frc)
        print(ecriture(f'{gecko.nom} attaque!'))
        if taliban.pv > 0:
            print(ecriture(f'taliban perd {round(10*g*gecko.stats.frc)} PV,    PV de Taliban : {taliban.pv}' ))
        else:
            print(ecriture(f'taliban perd {round(10*g*gecko.stats.frc)} PV'))
            print(ecriture('Le Taliban a été vaincu'))
        
    if gecko.stats.pv <= 0:
        print(ecriture(f'Votre Gecko a péri au combat, vous rentrez à la base sans récompense'))
        menu()
    else:
        show_image('C:/Users/erwan/Desktop/GeckoArtOnline/texture/zonesdesert/desert.png')
        desert(2)
def verr(): 
    print(ecriture(f'Vous sentez le sol trember... c est un {ver.nom} de sable !'))
    #afficher fond desert + cactus + barre de vie + stats
    show_image('C:/Users/erwan/Desktop/GeckoArtOnline/texture/zonesdesert/ver.png')
    j  = 0
    while ver.pv >= 0:
        j = j+1
        sleep(1)
        print('--------------------------------')
        print(ecriture(f'Tour {j}'))
    
        
        r = random.random() #Tour du cactus
        if r > 0.5:
            print(ecriture(f'Ver utilise {ver.capacite1}'))
            i = round(takedamage((ver.dps)*1.5))
            print(ecriture(f'{gecko.nom} perd {i} PV,       PV Restant : {gecko.stats.pv}'))
        else:
            print(ecriture(f'ver utilise {ver.capacite2}'))
            i = round(takedamage(ver.dps))
            print(ecriture(f'{gecko.nom} perd {i} PV,       PV Restant : {gecko.stats.pv}'))
        sleep(1)    
        if gecko.stats.pv <= 0:
            break
        g = random.random()  #Tour du gecko, g est la précision lié à la dextérité
        ver.pv = ver.pv - round(10*g*gecko.stats.frc)
        print(ecriture(f'{gecko.nom} attaque!'))
        if ver.pv > 0:
            print(ecriture(f'ver perd {round(10*g*gecko.stats.frc)} PV,    PV du Ver : {ver.pv}' ))
        else:
            print(ecriture(f'Ver perd {round(10*g*gecko.stats.frc)} PV'))
            print(ecriture('Le Ver a été vaincu'))
        
    if gecko.stats.pv <= 0:
        print(ecriture(f'Votre Gecko a péri au combat, vous rentrez à la base sans récompense'))
        menu()
    else:
        show_image('C:/Users/erwan/Desktop/GeckoArtOnline/texture/zonesdesert/desert.png')
        desert(3)
def tankk():
    
    print(ecriture(f'Vous entendez un Char d assault américain, il vous prend pour un taliban!'))
    #afficher fond desert + cactus + barre de vie + stats
    show_image('C:/Users/erwan/Desktop/GeckoArtOnline/texture/zonesdesert/tank.png')
    j = 0
    while tank.pv >= 0:
        j = j+1
        sleep(1)
        print('--------------------------------')
        print(ecriture(f'Tour {j}'))
    
        
        r = random.random() #Tour du cactus
        if r > 0.5:
            print(ecriture(f'tank utilise {tank.capacite1}'))
            i = round(takedamage(200))
            print(ecriture(f'{gecko.nom} perd {i} PV,       PV Restant : {gecko.stats.pv}'))
        else:
            print(ecriture(f'tank utilise {tank.capacite2}'))
            i = round(takedamage(tank.dps))
            print(ecriture(f'{gecko.nom} perd {i} PV,       PV Restant : {gecko.stats.pv}'))
        sleep(1)    
        if gecko.stats.pv <= 0:
            break
        g = random.random()  #Tour du gecko, g est la précision lié à la dextérité
        tank.pv = tank.pv - round(10*g*gecko.stats.frc)
        print(ecriture(f'{gecko.nom} attaque!'))
        if tank.pv > 0:
            print(ecriture(f'tank perd {round(10*g*gecko.stats.frc)} PV,    PV du Tank : {tank.pv}' ))
        else:
            print(ecriture(f'Tank perd {round(10*g*gecko.stats.frc)} PV'))
            print(ecriture('Les américain ont été défaits'))
        
    if gecko.stats.pv <= 0:
        print(ecriture(f'Votre Gecko a péri au combat, vous rentrez à la base sans récompense'))
        menu()
    else:
        show_image('C:/Users/erwan/Desktop/GeckoArtOnline/texture/zonesdesert/desert.png')
        desert(4)
def dioo():
    print(ecriture(f'Vous sentez une présence qui vous angoisse, c est un manieur de Stand !!!'))
    #afficher fond desert + cactus + barre de vie + stats
    show_image('C:/Users/erwan/Desktop/GeckoArtOnline/texture/zonesdesert/dio.png')
    j = 0
    while dio.pv >= 0:
        j = j+1
        sleep(1)
        print('--------------------------------')
        print(ecriture(f'Tour {j}'))
    
        
        r = random.random() #Tour du cactus
        if r > 0.5:
            print(ecriture(f'dio utilise {dio.capacite1}'))
            i = round(takedamage(300))
            print(ecriture(f'{gecko.nom} perd {i} PV,       PV Restant : {gecko.stats.pv}'))
        else:
            print(ecriture(f'Dio utilise {dio.capacite2}'))
            i = round(takedamage(dio.dps))
            print(ecriture(f'{gecko.nom} perd {i} PV,       PV Restant : {gecko.stats.pv}'))
        sleep(1) 
        if gecko.stats.pv <= 0:
            break
        g = random.random()  #Tour du gecko, g est la précision lié à la dextérité
        dio.pv = dio.pv - round(10*g*gecko.stats.frc)
        print(ecriture(f'{gecko.nom} attaque!'))
        if dio.pv > 0:
            print(ecriture(f'dio perd {round(10*g*gecko.stats.frc)} PV,    PV de Dio : {dio.pv}' ))
        else:
            print(ecriture(f'Dio perd {round(10*g*gecko.stats.frc)} PV'))
            print(ecriture('Votre gecko à vaincu Dio, faisant de lui un vrai Heros ! \n Vous avez terminer le niveau du Desert'))
        
    if gecko.stats.pv <= 0:
        print(ecriture(f'Votre Gecko a péri au combat, vous rentrez à la base sans récompense'))
        menu()
    else:
        show_image('C:/Users/erwan/Desktop/GeckoArtOnline/texture/zonesdesert/desert.png')
        desert(5)
    
    
    
def choixstat():
    ecran_stats()
    son_amelio = pygame.mixer.Sound("C:/Users/erwan/Desktop/GeckoArtOnline/Soundtrack/bruitage/amelioration.mp3")
    print(f'Choisissez les stats de {nom} que vous souhaitez améliorer')
    i = input('1 force\n2 endurance\n3 dextérité\n4 Intelligence')
    
    if i == '1':
        h = 0
        print(f'Vous avez  {gecko.stats.xp} points à dépenser\nForce actuelle: {gecko.stats.frc}')
        h = int(input('\nDe combien voulez vous améliorer la force?: '))
        if gecko.stats.xp >= h:
            son_amelio.play()
            gecko.stats.frc += h
            gecko.stats.xp -= h
            print(f'Xp restant: {gecko.stats.xp}')
            ecran_stats()
        else:
            print('Xp insuffisants')
    if i == '2':
        h = 0
        print(f'Vous avez  {gecko.stats.xp} points à dépenser\nEndurance actuelle: {gecko.stats.end}')
        h = int(input('\nDe combien voulez vous améliorer l endurance?: '))
        if gecko.stats.xp >= h:
            son_amelio.play()
            gecko.stats.end += h
            gecko.stats.xp -= h
            gecko.stats.pv = gecko.stats.end*10
            print(f'Xp restant: {gecko.stats.xp}, pv max ont changé à {gecko.stats.pv}')
            ecran_stats()
        else:
            print('Xp insuffisants')
    if i == '3':
        h = 0
        print(f'Vous avez  {gecko.stats.xp} points à dépenser\nDextérité actuelle: {gecko.stats.dxt}')
        h = int(input('\nDe combien voulez vous améliorer la dextérité?: '))
        if gecko.stats.xp >= h:
            son_amelio.play()
            gecko.stats.dxt += h
            gecko.stats.xp -= h
            print(f'Xp restant: {gecko.stats.xp}')
            ecran_stats()
        else:
            print('Xp insuffisants')
    if i == '4':
        h = 0
        print(f'Vous avez  {gecko.stats.xp} points à dépenser\nIntelligence actuelle: {gecko.stats.inte}')
        h = int(input('\nDe combien voulez vous améliorer l intelligence?: '))
        if gecko.stats.xp >= h:
            son_amelio.play()
            gecko.stats.inte += h
            gecko.stats.xp -= h
            print(f'Xp restant: {gecko.stats.xp}')
            ecran_stats()
        else:
            print('Xp insuffisants')    
   
    menu()
    
    
def afficherstat():
    print('-----------------------------------------------------')
    print(f'Xp : {gecko.stats.xp}\nForce : {gecko.stats.frc}\nEndurance : {gecko.stats.end}\nDextérité : {gecko.stats.dxt}\nIntelligence : {gecko.stats.inte}')
    print('-----------------------------------------------------')
    print('PV :', gecko.stats.pv)
    stats = [gecko.stats.xp,gecko.stats.frc,gecko.stats.end,gecko.stats.dxt,gecko.stats.inte]
    legende = ['xp', 'force', 'endurance', 'dextérité', 'intelligence']
    c = ('red','black','black','black','black')
    plt.barh(legende,stats, color = c,align='center')
    plt.ylim(top = 5)
    plt.ylim(bottom = -1)
    plt.xlim(right = 30)
    plt.xlim(left = -1)
    
   
    plt.show()
    i = input('\nAppuyez sur un touche pour continuer')  
    menu()
def ecran_stats():
    stats = [gecko.stats.xp,gecko.stats.frc,gecko.stats.end,gecko.stats.dxt,gecko.stats.inte]
    legende = ['xp', 'force', 'endurance', 'dextérité', 'intelligence']
    c = ('red','black','black','black','black')
    plt.barh(legende,stats, color = c,align='center')
    plt.ylim(top = 5)
    plt.ylim(bottom = -1)
    plt.xlim(right = 30)
    plt.xlim(left = -1)
    plt.show()
def exploration():
    print('------------------------------------')
    z = int(input('Ou voulez vous allez?\n1 : Désert de la mort\n2 : Marécage du roi slime\n3 : Montagnes du zero absolu\n4 : Forêt de ténèbris\n5 : Plaines infinies\n6 : Rivère du léviathan'))
    if z == 1:
        musique_menu.stop()
        plt.imshow(mpimg.imread('C:/Users/erwan/Desktop/GeckoArtOnline/map.png'))
        plt.plot(pts_explox[0],pts_exploy[0],marker = 'v', color = 'red',markersize=10)
        plt.axis('on')
        plt.show()
        sleep(3)
        desert(0)
    if z == 2:
        musique_menu.stop()
        plt.imshow(mpimg.imread('C:/Users/erwan/Desktop/GeckoArtOnline/map.png'))
        plt.plot(pts_explox[1],pts_exploy[1],marker = 'v', color = 'red',markersize=10)
        plt.axis('on')
        plt.show()
        sleep(3)
        marecage()
    if z == 3:
        musique_menu.stop()
        plt.imshow(mpimg.imread('C:/Users/erwan/Desktop/GeckoArtOnline/map.png'))
        plt.plot(pts_explox[2],pts_exploy[2],marker = 'v', color = 'red',markersize=10)
        plt.axis('on')
        plt.show()
        sleep(3)
        montagne()
    if z == 4:
        musique_menu.stop()
        plt.imshow(mpimg.imread('C:/Users/erwan/Desktop/GeckoArtOnline/map.png'))
        plt.plot(pts_explox[3],pts_exploy[3],marker = 'v', color = 'red',markersize=10)
        plt.axis('on')
        plt.show()
        foret()
    if z == 5:
        musique_menu.stop()
        plt.imshow(mpimg.imread('C:/Users/erwan/Desktop/GeckoArtOnline/map.png'))
        plt.plot(pts_explox[4],pts_exploy[4],marker = 'v', color = 'red',markersize=10)
        plt.axis('on')
        plt.show()
        sleep(3)
        plaine()
    if z == 6:
        musique_menu.stop()
        plt.imshow(mpimg.imread('C:/Users/erwan/Desktop/GeckoArtOnline/map.png'))
        plt.plot(pts_explox[5],pts_exploy[5],marker = 'v', color = 'red',markersize=10)
        plt.axis('on')
        plt.show()
        sleep(3)
        leviathan()
 
def desert(i):
    newxp =  [0,1,3,6,12,20]
    show_image('C:/Users/erwan/Desktop/GeckoArtOnline/texture/zonesdesert/desert.png')
    print('~~ ~~ ~~~~ ~~~~~~~~ ~~~~ ~~~~~ ~~~~')
    if i == 0:
        ecriture(f'Vous envoyez {gecko.nom} explorer le désert, étant un reptile, il est habitué à la chaleur!\n')
    progression_desert = 0
    o = 'y'
    x = 0
    while o != 'n' and x <550 and i < 5:
        
         o = str(input(ecriture(f'{gecko.nom} doit il continuer à explorer? (y:n)')))
         if o == 'y':
             
             progression_desert += 1
             show_imageetpoint('C:/Users/erwan/Desktop/GeckoArtOnline/texture/zonesdesert/desert.png', x,350)
             print('Niveau',i)
             rencontredesert(i)
             x += 100
         
            
    print(f'{gecko.nom} rentre à la base, gagnant de cette aventure',newxp[i],'XP !')
    gecko.stats.xp += newxp[i]
    menu()

musique_mennu()    
nom = str(input(ecriture('Entrez le nom de votre gecko de combat ! : ')))
gecko = geckoP(nom)
if nom.lower() == 'terra':
    gecko.stats.frc = 10000
    gecko.stats.dxt = 10000
    gecko.stats.end = 10000
    gecko.stats.inte = 10000
    gecko.stats.pv = gecko.stats.end*10
else:
    gecko.stats.frc = 10
    gecko.stats.dxt = 10
    gecko.stats.end = 10
    gecko.stats.inte = 10
menu()   
    
    
             

  






