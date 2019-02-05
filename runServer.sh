if [ "$OSTYPE" = "msys" ]; then
  echo "Assuming this is windows, running with waitress"
  waitress-serve --port=80 simplyroleplaying.setup:srp
else
  echo "Assuming this is a linux-based OS, running with gunicorn"
  gunicorn --port=80 simplyroleplaying.setup:srp
fi
