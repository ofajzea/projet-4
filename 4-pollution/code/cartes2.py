#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#Importation des bibliotheque
import numpy as np
import matplotlib.pyplot as plt
from netCDF4 import Dataset
from matplotlib.colors import LogNorm
import os
import pickle

#Debug de la bibliotheque pour windows
os.environ['PROJ_LIB'] = r'C:\Users\gauth_000\Documents\miniconda3\pkgs\proj4-5.2.0-ha925a31_1\Library\share'
from mpl_toolkits.basemap import Basemap

nom_sauv="sauvegarde2019conf"
nom_sauv_pix="sauvegardePix2019conf"

#variable pour faire le plot
pas_long=0.2
debut_long=0
fin_long=10
N_long= int ((fin_long-debut_long)/pas_long)+1

pas_lat=0.2
debut_lat=40
fin_lat=50
N_lat=int ((fin_lat-debut_lat)/pas_lat)+1


longitude=np.linspace(debut_long,fin_long,N_long)   #0=>10 pas 0.01
latitude=np.linspace(debut_lat,fin_lat,N_lat)  #40=>50 pas 0.01
   

#recupere des données
fichierSauvegarde = open(nom_sauv,"rb")
res_no = pickle.load(fichierSauvegarde)
fichierSauvegarde.close()
fichierSauvegarde1 = open(nom_sauv_pix,"rb")
nb_pix = pickle.load(fichierSauvegarde1)
fichierSauvegarde1.close()


#Unité
fh=Dataset('S5P_OFFL_L2__NO2____010519.nc', mode = 'r' )
no2_units = fh.groups['PRODUCT'].variables['nitrogendioxide_tropospheric_column_precision'].units


#MAP pour le NO2 
m = Basemap(width=1000000,height=1000000,resolution='l',projection='stere',lat_ts=40,lat_0=45.1667,lon_0=5.717)   
xi, yi = m(longitude, latitude)


# Plot Data
cs = m.pcolor(xi,yi,np.squeeze(res_no),vmin=6e-7, vmax=3e-5,norm=LogNorm(), cmap='jet')


#add grid    
m.drawparallels(np.arange(-80., 81., 20.), labels=[1,0,0,0], fontsize=5)
m.drawmeridians(np.arange(-180., 181., 20.), labels=[0,0,0,1], fontsize=5)


#Add coastlines, states and country
m.drawcoastlines()
m.drawcountries()


# Add Colorbar
cbar = m.colorbar(cs, location='bottom', pad="10%")
cbar.set_label(no2_units)

# Add Title
plt.title('NO2 in atmosphere')
plt.savefig('NO2 in atmosphere', dpi = 600)
plt.show()


#MAP 2 pour les qa
m1 = Basemap(width=1000000,height=1000000,resolution='l',projection='stere',lat_ts=40,lat_0=45.1667,lon_0=5.717)


#plot data  
cs1 = m1.pcolor(xi,yi,np.squeeze(nb_pix), cmap='jet')


#add grid    
m1.drawparallels(np.arange(-80., 81., 20.), labels=[1,0,0,0], fontsize=5)
m1.drawmeridians(np.arange(-180., 181., 20.), labels=[0,0,0,1], fontsize=5)


#Add coastlines, states and country
m1.drawcoastlines()
m1.drawcountries()


#Add color bar
cbar1 = m1.colorbar(cs1, location='bottom', pad="10%") 


# Add Title
plt.title('nombre de pixel comptabilisé')
plt.savefig('nombre de pixel qa.png', dpi = 600)
plt.show()

