#!/bin/sh

############### Couleurs
GREEN='\033[1;32m'
WHITE='\033[1;0m' #real white \033[1;37m

############### Vérification de la présence du logiciel.
if [ ! -x /usr/bin/sqlite3 ] ; then
echo "Le logiciel sqlite n'est manquant, veulliez l'installer."
echo "Instrucrion :"
echo "Debian : sudo apt install sqlite3"
echo "Fedora : sudo dnf install sqlite"
exit 1
fi

############### delete previous file
echo -e "${GREEN}>>>${WHITE} Delete old ArticlesData.db"
rm ArticlesData.db

############### Database
echo -e "${GREEN}>>>${WHITE} Converting DataBase"
sqlite3 ArticlesData.db <<'END_SQL'
.timeout 2000
.mode csv
.import ArticlesData.csv ArticlesData
.quit
END_SQL
echo -e "${GREEN}>>>${WHITE} Done."
