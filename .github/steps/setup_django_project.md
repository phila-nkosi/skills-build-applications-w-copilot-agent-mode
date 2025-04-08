# Setting Up the Django Project for Octofit Tracker

1. Navigate to the `octofit-tracker/backend` directory:
   ```bash
   cd octofit-tracker/backend
   ```

2. Create the Django project:
   ```bash
   django-admin startproject octofit_tracker .
   ```

3. Create the Django app:
   ```bash
   python manage.py startapp octofit_tracker
   ```

4. Add the app to `INSTALLED_APPS` in `octofit_tracker/settings.py`:
   ```python
   INSTALLED_APPS = [
       # ...existing apps...
       'octofit_tracker',
   ]
   ```

5. Apply migrations:
   ```bash
   python manage.py migrate
   ```

6. Run the development server:
   ```bash
   python manage.py runserver
   ```

7. Access the server at `http://127.0.0.1:8000/`.
