# Libraries used for the Widget
For the installation of the libraries we recomend to create a venv:
```sh
python -m venv .venv
```
Once made the venv, activate it with:
```sh
.venv/scripts/activate
```
* PySide6 (6.7.0. Version)
```sh
pip install pyside6==6.7.0
```
* Spotipy
```sh
pip install spotipy
```
## How to use this Widget
1.- Go to your [Spotify Dashboard](https://developer.spotify.com/dashboard), login to your account and create an App.

2.- On the screen for creating the App, you can put whatever title and description you want for the application, but for the section of "Redirect URIs" make sure to write down:
```sh
https://localhost:8888/callback
```
3.- Once created the app in the Dashboard, open it and head to settings.

4.- In the Basic Information section, you'll need to copy your CLIENT_ID and CLIENT_SECRET and paste it on the SPOTIFY_CREDENTIALS archive.

(resources/constants/SPOTIFY_CREDENTIALS.py)

5.- Once paste the credentials, you can start up the Widget in the App.py section and you are ready to go.

## Captures of the Widget

![image](https://github.com/EmilianoAnaya/Spotify-Visualizer/assets/150195114/56cc2a58-7796-4a0e-a4ae-771d87dcccf4)

![image](https://github.com/EmilianoAnaya/Spotify-Visualizer/assets/150195114/3bcb4ed9-2698-4449-bbd1-4950ec8cf486)

![image](https://github.com/EmilianoAnaya/Spotify-Visualizer/assets/150195114/e3ba096b-1402-4da7-89f8-34080a6c2b65)
