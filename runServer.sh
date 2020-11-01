#!/bin/bash
if [ ! -d "venv" ]; then
  echo "No virtual environment detected, running first time setup..."
  virtualenv venv
  initialize=true
else
  initialize=false
fi

if [ "$OSTYPE" = "msys" ]; then
  echo "Running on windows..."
  source venv/Scripts/activate
else
  echo "Running on linux os..."
  source venv/bin/activate
fi

if [ "$initialize" = "true" ]; then
  pip install -r requirements.txt
fi

mkdocs serve "$@"
