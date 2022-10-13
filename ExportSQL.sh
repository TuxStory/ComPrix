#!/bin/bash

#Export SQL
sqlite3 ArticlesData.db <<'END_SQL'
.output ArticlesData.sql
.dump
.exit
END_SQL
