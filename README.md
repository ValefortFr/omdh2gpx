# omdh2gpx

Old OnMove GPS watches use file formats (OMD and OMH) unknown by Strava, since OnConnect application is unreliable I wrote a little script to convert those files to gpx format.

Several GitHub repositories already existed for this purpose but came with their own limitations, complex to run or creating more data than some watch models actually saved, therefore I wrote the simplest version I could where only GPS data is saved. Thanks to Riccardo Boninsegna (https://github.com/rboninsegna/OnMove200) and Denis Paris (http://uncledens.chez-alice.fr/python/montregps.htm) for doing the actual work of understanding how the files were structured.

Les anciennes montres OnMove sauvent leurs données GPS dans des formats inconnus de Strava (OMD et OMH) ; ce script les convertit en gpx. Plus besoin de passer par l'application OnConnect qui est parfois en carafe.

Plusieurs convertisseurs existaient déjà sur github mais pouvaient être complexes à mettre en oeuvre ou produisaient plus de données que certains modèles de montre ne sauvaient effectivement, j'ai donc écrit une version simplifiée et la plus basique possible où seuls les données GPS sont conservées. Merci à Riccardo Boninsegna (https://github.com/rboninsegna/OnMove200) et Denis Paris (http://uncledens.chez-alice.fr/python/montregps.htm) pour avoir fait le gros du boulot de compréhension de la structure de ces fichiers.

# Usage

Execute this script in a folder where the ACT_0000.OMH and ACT_0000.OMD are located, it will output an ACT_0000.gpx in that same folder.

# Utilisation

Exécuter ce script dans un répertoire où les fichiers ACT_0000.OMH et ACT_0000.OMD sont présents produira un fichier ACT_0000.gpx dans ce même répertoire.
