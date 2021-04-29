import numpy as np
import matplotlib.pyplot as plt
from netCDF4 import Dataset
from matplotlib.colors import LogNorm
import os

os.environ['PROJ_LIB'] = r'C:\Users\gauth_000\Documents\miniconda3\pkgs\proj4-5.2.0-ha925a31_1\Library\share'
from mpl_toolkits.basemap import Basemap


#Carte à faire

nom_fichier='S5P_OFFL_L2__NO2____100320.nc'


fh=Dataset(nom_fichier, mode = 'r' )

    
long = fh.groups['PRODUCT'].variables['longitude'][:][0,:,:]
lat = fh.groups['PRODUCT'].variables['latitude'][:][0,:,:]
    

#shape pour faire les for
shape_long=fh.groups['PRODUCT'].variables['longitude'].shape
    
#donnée
no=fh.groups['PRODUCT'].variables['nitrogendioxide_tropospheric_column_precision'][0,:,:]
qa=fh.groups['PRODUCT'].variables['qa_value'][:][0,:,:]

shape=fh.groups['PRODUCT'].variables['nitrogendioxide_tropospheric_column_precision'].shape

#nombre de pixel pris en compte (qa valide)
pix=np.zeros([shape[1],shape[2]]) 


#on fait la moyenne
for i in range (0,shape[1]):
    #pourcentage pour voir l'avancement
    print(float (i/shape[1]))
    for j in range (0,shape[2]):
        if no[i][j]!=0: #pixel nul?
            pix[i][j]=1


  
m = Basemap(width=1000000,height=1000000,resolution='l',projection='stere',lat_0=45.1667,lon_0=5.717)   
xi, yi = m(long, lat)


# Plot Data
cs = m.pcolor(xi,yi,np.squeeze(no),vmin=1e-5, vmax=9e-4,norm=LogNorm(), cmap='jet')


#add grid    
m.drawparallels(np.arange(-80., 81., 10.), labels=[1,0,0,0], fontsize=5)
m.drawmeridians(np.arange(-180., 181., 10.), labels=[0,0,0,1], fontsize=5)


#Add coastlines, states and country
m.drawcoastlines()
m.drawcountries()


# Add Colorbar
no2_units = fh.groups['PRODUCT'].variables['nitrogendioxide_tropospheric_column_precision'].units
cbar = m.colorbar(cs, location='bottom', pad="10%")
cbar.set_label(no2_units)

# Add Title
plt.title('NO2 in atmosphere')
plt.savefig('No1', dpi = 600)
plt.show()


