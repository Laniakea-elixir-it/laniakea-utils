Laniakea Utils
==============

Laniakea utilites package

Api
---

test

start: gunicorn --workers 2 --bind 0.0.0.0:5001 --timeout 300 app:app

curl: curl -H 'Accept: application/json' -H "Authorization: Bearer ${TOKEN}" http://90.147.102.14:5000/valid_user/${SUB}
