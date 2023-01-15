#!/bin/bash
exec gunicorn server.wsgi:application -b 0.0.0.0:8080 --reload