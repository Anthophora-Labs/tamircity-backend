### README Format
 * https://www.markdownguide.org/basic-syntax/

### Dependency Management
 * pip freeze > requirements.txt
 * pip install -r requirements.txt

### Venv
 * source /ven/bin/activate
 * venv\Scripts\activate
 * python3 -m venv env
 * source env/bin/activate

### DB Dumping Data
 * python manage.py dumpdata -format json -indent 2 > initial_data.json
 * python manage.py syncdb

### Check TODO
 * //TODO: Note Sample