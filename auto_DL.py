import requests
from requests.auth import HTTPBasicAuth
import json
import os
from shapely.geometry import box
import urllib3
from tqdm import tqdm

# === PARAMÈTRES ===
CLIENT_ID = 'sh-ad8b11ef-30e6-4c11-a4e8-b758bd61f323'
CLIENT_SECRET = 'EVLi8UwJ4RDJK6SowvVQLSyNr0hsbvAj'

USERNAME = "maxime.jose22@gmail.com"
PASSWORD = "Ntf080603!!*"
BBOX =  [1.4, 48.0, 3.5, 49.2]  #-->PARIS   Format [minLon, minLat, maxLon, maxLat] 
START_DATE = "2022-07-02T00:00:00.000Z"
END_DATE = "2022-08-29T23:59:59.999Z"
MAX_RESULTS = 1000 # Nombre maximum de fichiers à récupérer
DOWNLOAD_FOLDER = "C:/Users/josema.E3/Desktop/2022"  
MAX_FILES_PER_MONTH = 30  # nombre de fichiers max à télécharger par mois
monthly_counter = {}  # dictionnaire pour compter par mois



auth_url = 'https://identity.dataspace.copernicus.eu/auth/realms/CDSE/protocol/openid-connect/token'
search_url = "https://catalogue.dataspace.copernicus.eu/stac/search"


# === Récupération du token ===
auth_payload = {
    'client_id': 'cdse-public',
    'username': USERNAME,
    'password': PASSWORD,
    'grant_type': 'password'
}
auth_response = requests.post(auth_url, data=auth_payload)
auth_response.raise_for_status()
access_token = auth_response.json()['access_token']
print("Token récupéré")
#print("access_token (début) :", access_token[:30])

headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json"
}

# === Requête envoyée ===
search_payload = {
    "collections": ["SENTINEL-5P"],
    "bbox": BBOX,
    "datetime": f"{START_DATE}/{END_DATE}",
    "limit": MAX_RESULTS
}

search_response = requests.post(search_url, headers=headers, json=search_payload)
search_response.raise_for_status()
items = search_response.json().get("features", [])
print(len(items))


if not items:
    print("❌ Aucun produit trouvé pour la période et la zone définies.")
    exit()


os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

for i, item in enumerate(items):
    if "NO2" not in item["id"]:     #filtrage des jeux de donnees par la ressource souhaitee
        #print(f" Produit ignoré (pas du NO2) : {item['id']}")  
        continue

    print(f"\n Produit NO2 trouvé : {item['id']}")
    #print("Assets disponibles :", list(item['assets'].keys()))
    #print(" Détail de l'asset PRODUCT :", json.dumps(item['assets']['PRODUCT'], indent=2))
    
    asset = item['assets'].get('PRODUCT', {})
    asset_url = asset.get('href', None)

      # Si le lien vers S3 existe dans l'asset 'alternate', on l'utilise
    s3_url = item['assets']['PRODUCT'].get('alternate', {}).get('s3', {}).get('href', None)
    if s3_url:
        s3_url = "https://catalogue.dataspace.copernicus.eu" + s3_url #recuperation du lien de telechargement 
        #print(s3_url)
        filename = s3_url.split('/')[-1]  # Extraire le nom du fichier depuis l'URL
        
        # Télécharger via S3 
        headers = {
            "Authorization": f"Bearer {access_token}"
        }
     
    asset = item['assets'].get('PRODUCT', {})
    asset_url = asset.get('href', None)

    if not asset_url:
        print("Aucun lien 'href' dans l'asset 'PRODUCT'.")
        continue

    filename = item["id"]  # Ajout de l'extension
    print(f"Téléchargement de : {filename}")
    #print("Lien initial :", asset_url)

    headers_download = {
        "Authorization": f"Bearer {access_token}"
    }

    # Première requête (peut rediriger)
    r = requests.get(asset_url, headers=headers_download, stream=True, allow_redirects=False, verify=False)
    # suivi des redirection 
    if r.status_code in [301, 302, 303, 307, 308]:
        redirect_url = r.headers.get("Location")
        if not redirect_url:
            print(" Redirection sans URL détectée.")
            continue

        #print(" Redirection vers :", redirect_url)
        final_url = redirect_url
    elif r.status_code == 200:
        final_url = asset_url
    else:
        print(f"Erreur lors de la requête initiale : {r.status_code}")
        continue

    try:
        date_str = filename.split("__")[-1][:8]  # ex: '20181015'
        year_month = date_str[:4] + "-" + date_str[4:6]  # ex: '2018-10'
    except Exception as e:
        print(f"Impossible d'extraire la date pour {filename} : {e}")
        continue

    #Vérifier si on dépasse la limite mensuelle
    if monthly_counter.get(year_month, 0) >= MAX_FILES_PER_MONTH:
        print(f"Limite de {MAX_FILES_PER_MONTH} fichiers atteinte pour {year_month}")
        continue

    monthly_counter[year_month] = monthly_counter.get(year_month, 0) + 1
    
    #verification si le fichier est deja present
    full_path = os.path.abspath(os.path.join(DOWNLOAD_FOLDER, filename))    
    if os.path.exists(full_path):
        print(f"Fichier déjà présent, téléchargement ignoré : {filename}")
        continue

    #telechargement du set de donnees    
    with requests.get(final_url, headers=headers_download, stream=True, verify=False) as r:
            if r.status_code == 200:
                total_size = int(r.headers.get('content-length', 0))
                block_size = 1024  # 1 KB

                tqdm_bar = tqdm(total=total_size, unit='iB', unit_scale=True, desc=filename)
                with open(os.path.join(DOWNLOAD_FOLDER, filename), 'wb') as f:
                    for data in r.iter_content(block_size):
                        tqdm_bar.update(len(data))
                        f.write(data)
                tqdm_bar.close()
                full_path = os.path.abspath(os.path.join(DOWNLOAD_FOLDER, filename))
                #print(f"Fichier enregistré ici : {full_path}")

                if total_size != 0 and tqdm_bar.n != total_size:
                    print("Taille du fichier inattendue")
                else: 
                    print(f"Fichier téléchargé avec succès : {filename}")
            else:
                print(f"Erreur lors du téléchargement final : {r.status_code}")