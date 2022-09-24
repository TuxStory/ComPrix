#!/bin/sh

#delete previous file
rm ArticlesData.db

#Database
sqlite3 ArticlesData.db <<'END_SQL'
.timeout 2000
.mode csv
.import ArticlesData.csv ArticlesData
.quit
END_SQL
