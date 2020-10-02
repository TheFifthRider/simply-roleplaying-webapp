#!/bin/bash
if [ "$OSTYPE" = "msys" ]; then
  echo "Running on windows..."
  source venv/Scripts/activate
  cd simplyroleplaying
  mkdocs serve
else
  echo "Running on linux os..."
  source venv/bin/activate
  cd simplyroleplaying
  mkdocs serve
fi
