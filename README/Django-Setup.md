# Prerequsits
Have an active Virtual Environment
Be located inside the directory for your project
## Starting setup
install django

`pip install django`

## Create the project
```
django-admin startproject <name of project>
 
```
### Rearrange folders
If you are creating a single project in the directory, and the name of the project matches the name of your current directory; you may consider making navigation easier by deleting an empty directory. To do this move all the files in your new project folderr up one, then delete the empty directory. Commands as follows:

```
mv <project>/manage.py ./
mv <project>/<project>/* <project>
rm -r <project>/<project>

```

## Local Host
Navigate to the folder were your python application "manage.py" is and utilize the command: 
`python3 manage.py runserver <port>`
if you do not specify a port, django defaults to port 8000.<br>
`python3 manage.py runserver 8000`<br>
`python3 manage.py runserver` <br>
both do the same thing.

## Creating the application
- From the project folder run the command
- `python3 manage.py startapp <app name>` 
- Use command 'p' + settings.py to navigate to the settings file
- Under Installed_apps add the name of your application
- update urls.py in project folder
```python
from djang.contrib import admin
from django.urls import path, include
urlpatterns = [ path('',include(<app name.urls>))]
```
- in the app views page
```python
from django.shortcuts import render
from django.http import HttpResponse
def helloWorld(request):
    return HttpResponse('Hello World!')
```
- create urls.py in the application to store local urls
```python
from django.urls import path
from . import views
urlpatterns = [ path('', views.helloWorld)]
```
