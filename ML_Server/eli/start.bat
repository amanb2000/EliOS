set FLASK_APP=eli
set FLASK_ENV=development
set GOOGLE_APPLICATION_CREDENTIALS=serviceAccountKey.json
pip install -e .
python -m flask run
PAUSE