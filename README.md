# AmFOSS Portal
The repository managing the web portal of amFOSS (FOSS@Amrita), a computer science club based in
Amrita University, Amritapuri. 


### Installation
The portal is primarily a django based application, and to set it up we require to have 
python environment with django and other project dependencies installed. Though one can
work with the project without an virtual environment,  it is recommended to use one so 
as to avoid conflicts with other projects.

1. Make sure that you have `Python 3` and `pip` installed. 
   Install `virtualenvwrapper`, and add it to your terminal path.
   
    ```
       $ sudo pip install virtualenvwrapper
       $ echo 'export WORKON_HOME=~/Envs' >> ~/.bashrc
       $ echo 'mkdir -p $WORKON_HOME' >> ~/.bashrc   
       $ echo 'source /usr/local/bin/virtualenvwrapper.sh' >> ~/.bashrc   
    ```
    
2. Clone the repository, and create a virtual environment for the project, 
   and work on the newly set up environment.
   
    ```
        $ git clone <repository-url>
        $ cd amfoss-portal
        $ mkvirtualenv --python=python3 foss-website
        $ workon foss-website
    ```
    
3. Install the project dependencies from `requirements.txt`
    ```
        $ pip install -r requirements.txt
    ```

You have now successfully set up the project on your environment, 
now inside the `portal` directory you can work with the django application as usual - 

* `python manage.py migrate` - set up database
* `python manage.py createsuperadmin` - create admin user
* `python manage.py runserver`  - run the project locally


### Technical Specification

**Stack Details**

* **Languages** - Python 3 (Backend), JavaScript (Frontend), HTML 5 (Frontend), Markdown (Documentation)
* **Database** - mySQL (Production), SQLite3 (Development)
* **Frameworks** - Django (Full Stack), Bootstrap 4 (Frontend)
* **Libraries** - JQuery, Sass, HAML, C3JS / D3JS (Charts)
* **DevOps** - GitHub (Code Collaboration), Git (VCS), PyCharm (IDE), Atom (Text Editor)
* **Utilities** - Google Analytics, jsDeliver (CDN)

**Required Dependencies**
```
   Django==2.1.3
   django-ckeditor==5.6.1
   django-easy-select2==1.5.5
   django-js-asset==1.1.0
   djangorestframework==3.9.0
   Pillow==5.3.0
   pytz==2018.7
```

