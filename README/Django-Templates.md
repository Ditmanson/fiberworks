# Prerequsits
Active python virtual environment
Django application set up complete

## Under views.py
You'll need an http request for an html document
```python 
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
# Render index.html
    return render( request, 'portfolio_app/index.html')
```
## Create templates folder
For this application create the following file path to store templates<br>
app/templates/app <br>
create a base html template for reuse. <br>
create an index.html template to call from<br>
- index.html is the naming convention for a web applications homepage.
Insert the base template into your index
```python
 
<!-- inherit from base.html -->
{% extends 'portfolio_app/base_template.html' %}

<!-- Replace block content in base_template.html -->
{% block content %}
  <h1>Computer Science Portfolios</h1>

  <h2>More to come</h2>
{% endblock %}
```
## Static Files
Static files such as css/images/documents should be sourced from a static folder.<br>
- At the same layer as your project, application, and virtual environment, add a directory called satic.
- Create sub directories for file types.
- To use import static objects at the top of the page
- `{%load static%}` 
An example of how to import a static item into a html tag:
- ` <img src="{% static 'images/uccs_logo.gif' %}">`