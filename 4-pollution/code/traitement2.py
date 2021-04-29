#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Importation des bibliotheque
import numpy as np
from netCDF4 import Dataset
import pickle


nom_sauv="sauvegarde2019conf"
nom_sauv_pix="sauvegardePix2019conf"


#variable pour la discretisation spatial
pas_long=0.2
debut_long=0
fin_long=10
N_long= int ((fin_long-debut_long)/pas_long)+1

pas_lat=0.2
debut_lat=40
fin_lat=50
N_lat=int ((fin_lat-debut_lat)/pas_lat)+1

#discretisation
longitude=np.linspace(debut_long,fin_long,N_long)   #0=>10 pas 0.02
latitude=np.linspace(debut_lat,fin_lat,N_lat)  #40=>50 pas 0.02
   


#Carte à faire
nom_fichier=[]
nom_fichier.append('S5P_OFFL_L2__NO2____010519.nc')
nom_fichier.append('S5P_OFFL_L2__NO2____020519.nc')
nom_fichier.append('S5P_OFFL_L2__NO2____030519.nc')
nom_fichier.append('S5P_OFFL_L2__NO2____040519.nc')
nom_fichier.append('S5P_OFFL_L2__NO2____050519.nc')
nom_fichier.append('S5P_OFFL_L2__NO2____060519.nc')
nom_fichier.append('S5P_OFFL_L2__NO2____070519.nc')
nom_fichier.append('S5P_OFFL_L2__NO2____080519.nc')
nom_fichier.append('S5P_OFFL_L2__NO2____090519.nc')
nom_fichier.append('S5P_OFFL_L2__NO2____100519.nc')
nom_fichier.append('S5P_OFFL_L2__NO2____300419.nc')
nom_fichier.append('S5P_OFFL_L2__NO2____290419.nc')
nom_fichier.append('S5P_OFFL_L2__NO2____280419.nc')
nom_fichier.append('S5P_OFFL_L2__NO2____270419.nc')
nom_fichier.append('S5P_OFFL_L2__NO2____260419.nc')


fh=[]
for i in range (0,len(nom_fichier)):
    fh.append(Dataset (nom_fichier[i], mode = 'r' ))
    
no=[]#nouvelles maps discretisées

#partie pour la discretisation
for i in range(0,len(fh)):
    #vrai longitude et latitude
    long = fh[i].groups['PRODUCT'].variables['longitude'][:][0,:,:]
    lat = fh[i].groups['PRODUCT'].variables['latitude'][:][0,:,:]
    
    #shape pour faire les for
    shape_long=fh[i].groups['PRODUCT'].variables['longitude'].shape
    
    #donnée
    no_nd=fh[i].groups['PRODUCT'].variables['nitrogendioxide_tropospheric_column_precision'][0,:,:]
    qa_nd=fh[i].groups['PRODUCT'].variables['qa_value'][:][0,:,:]
    
    #donnée avec discretisation
    pixel=np.zeros([N_lat,N_long])
    nb_pix=np.zeros([N_lat,N_long])
    
    
    indice_lat=0
    indice_long=0
    
    #pourcentage de réalisation
    print(float(i/len(fh)))
    
    #on parcours tous les pixels
    for i in range(0,shape_long[1]):
        for j in range(0,shape_long[2]):
            
            #on verifie si on est dans l'intervalle de long et lat
            if((long[i,j]>=debut_long and long[i,j]<=fin_long) and (lat[i,j]>=debut_lat and lat[i,j]<=fin_lat)):
                #nouveau indice pour discretisation
                indice_long=int ((long[i,j]-debut_long)/pas_long)
                indice_lat=int ((lat[i,j]-debut_lat)/pas_lat)
                
            #valeur qui permet d'évaluer si un pixel n'est pas faussé
            if(qa_nd[i,j]>=0.7):
                pixel[indice_lat,indice_long]=no_nd[i,j]
                nb_pix[indice_lat,indice_long]+=1
  
    #si plusieurs pixels sont pris en compte, on fait une moyenne
    for i in range(0,N_lat):
        for j in range(0,N_long):
            if(nb_pix[i,j]!=0):
                pixel[i,j]=pixel[i,j]/nb_pix[i,j]  
                
    #nouvelles maps discretisées
    no.append(pixel)


#Partie du traitement pour faire la moyenne

#nombre de pixel pris en compte (qa valide)
nb_pix=np.zeros([N_lat,N_long]) 

#moyenne des pixels
res_no = np.zeros([N_lat,N_long]) 

#on fait la moyenne
for i in range (0,N_lat):
    #pourcentage pour voir l'avancement
    print(float (i/N_lat))
    for j in range (0,N_long):
        for k in range (0,len(fh)):
            if no[k][i][j]!=0: #pixel nul?
                res_no[i][j]+=no[k][i][j]
                nb_pix[i][j]+=1
        if(nb_pix[i][j]!=0):
            res_no[i][j]=res_no[i][j]/nb_pix[i][j]
        else:
            res_no[i][j]=0



#enregistrement de données
fichierSauvegarde = open(nom_sauv,"wb")
pickle.dump(res_no, fichierSauvegarde)
fichierSauvegarde.close()

fichierSauvegarde = open(nom_sauv_pix,"wb")
pickle.dump(nb_pix, fichierSauvegarde)
fichierSauvegarde.close()

