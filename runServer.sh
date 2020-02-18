#!/bin/bash
if [ "$OSTYPE" = "msys" ]; then
  echo "Assuming this is windows, running with waitress"
  source venv/Scripts/activate
  waitress-serve --port=80 simplyroleplaying.setup:srp
else
  echo "Assuming this is a linux-based OS, running with gunicorn"
  source venv/bin/activate
  gunicorn -b :80 simplyroleplaying.setup:srp
fi
