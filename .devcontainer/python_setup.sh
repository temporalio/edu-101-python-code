#!/bin/bash

python -m venv .env
source .env/bin/activate
python -m pip install -r requirements.txt
temporal server start-dev --ui-port 8080