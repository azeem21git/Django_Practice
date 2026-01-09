##---------Django Practice-----------##

create folder and virtual environment
1) python3 -m venv .venv
2) source ./.venv/bin/activate

pip use for install python packages 
  instal django package 
      --> pip install django


next create new django project 
      -->django-admin startproject DjangoProject .
        {ending must want add dot ,nothing it can double folder structure}

run django Project 
      -->python3 manage.py runserver


creating App
       -->python3 manage.py startapp Inventory

app (Inventory) file is connect withProjectFile (DjangoProject)
       -->setting.py ->INSTALLED_APPS ->'Inventory' add there

forntend is created on DjangoProject folder so not want chane in setting
template is created on Front end   for HTML Files
     there not vant filer such as 
       view.py ,adin.py ,model.py , migrations , __pycahe__