#!/usr/bin/env bash
#
#echo "*************** creating database ****************"
#alembic create schema flask_db if not exists
#
echo "_______________running autogenerate_______________"
#alembic revision --autogenerate -m "Create tables"

echo "_______________executing migrations_______________"
alembic upgrade head

python app.py