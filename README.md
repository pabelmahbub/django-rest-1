### django-rest-1

django rest framework porject:
1. create a folder in pc: ```django-rest-framework```

2. open in vs code in terminal and create a virtual env: 
```python3 -m venv drenv(drenv is our venv name)```

3. Now activate venv in terminal by, 
```source drenv/bin/activate(for mac)```
```drenv/Scripts/activate (for windows)```

4. Need to install django in venv: ```pip install django djangorestframework```
[if error of cpuldn't find a version that satifies the requirements djangorest.... 
```pip install djangorestframework-jsonapi```

5. If pip upgrading needed: ```pip install --upgrade pip```

5a.  root app (apiproject) in settings: add in ```INSTALLED_APP= ['rest_framework']```

6. create a project of django by: ```django-admin startproject apiproject(our root app name)```

```cd apiproject```

```python3 manage.py migrate```

```python3 manage.py startapp myapp(app name)```

7. create a superuser: ```python3 manage.py createsuperuser(name,email,password) and app will start in 127.0.0.0/admijn```

```python3 manage.py runserver```
