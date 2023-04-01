### Configuration of Django
 * python manage.py runserver
 * python manage.py makemigrations
 * python manage.py migrate
 * python manage.py createsuperuser

### README Format
 * https://www.markdownguide.org/basic-syntax/

### Review
 * https://snyk.io/learn/code-review/python-tools/

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

### Installing & Uninstalling Packages
 * pip3 uninstall PyCrypto
 * pip3 install -U PyCryptodome, pipenv install celery

### Setting Up for Environments
 * pip install -r requirements.txt
 * pip install -r requirements-dev.txt
 * pip install -r requirements-test.txt
 * pip install -r requirements-prod.txt
 * https://thinkster.io/tutorials/configuring-django-settings-for-production
 * https://stackoverflow.com/questions/10664244/django-how-to-manage-development-and-production-settings
 * https://djangostars.com/blog/configuring-django-settings-best-practices/

### Tools
 * https://www.sonarsource.com/plans-and-pricing/
 * https://www.sonarqube.org/downloads/
 * https://mustafaakgul.jetbrains.space/
 * Github Copilot