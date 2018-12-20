# AmFOSS CMS
The repository managing the web portal of amFOSS (FOSS@Amrita), a computer science club based in
Amrita University, Amritapuri. 

### Installation Instructions
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
* **API** - REST API
* **Database** - PostgreSQL (Production), SQLite3 (Development)
* **Frameworks** - Django (Full Stack), Bootstrap 4 (Frontend)
* **Libraries** - JQuery, Sass, HAML, C3JS / D3JS (Charts)
* **DevOps** - GitHub (Code Collaboration), Git (VCS), PyCharm (IDE), Atom (Text Editor)
* **Utilities** - Google Analytics, jsDeliver (CDN)

### Changelog
Change log of this project can be found in [`HISTORY.md`](HISTORY.md).

### License
This project is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This project is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License (<https://www.gnu.org/licenses/>) for more details.

© 2018 Team AmFOSS. See the [Contributors](CONTRIBUTORS.md) list here.
