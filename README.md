# omdh2gpx
Les anciennes montres OnMove sauvent leurs données GPS dans des formats inconnus de Strava (OMD et OMH) ; ce script les convertit en gpx. Plus besoin de passer par l'application OnConnect qui est parfois en carafe.

Plusieurs convertisseurs existaient déjà sur github mais pouvaient être complexes à mettre en oeuvre ou produisaient plus de données que certains modèles de montre ne sauvaient effectivement, j'ai donc écrit une version simplifiée et la plus basique possible où seuls les données GPS sont conservées. Merci à Riccardo Boninsegna (https://github.com/rboninsegna/OnMove200) et Denis Paris (http://uncledens.chez-alice.fr/python/montregps.htm) pour avoir fait le gros du boulot de compréhension de la structure de ces fichiers.

Exécuter ce script dans un répertoire où les fichiers ACT_0000.OMH et ACT_0000.OMD sont présents produira un fichier ACT_0000.gpx dans ce même répertoire.
