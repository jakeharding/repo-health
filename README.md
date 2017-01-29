# Repository Health Project for CSCI 4900

The repository hold the proof of concept for the repository health and sustainability project for CSCI 4900 at the Univeristy of Nebraska at Omaha.  This repository will hold the backend and frontend source code to extract data from Github and ghtorrent and prodvide statistics about a selected repository.  Description of the backend and frontend source are provided.

## Backend
The Django web framework is used in the project to leverage quick development and the third party packages available.  Python requirements are kept in the requirements.txt file, and this file is generated using `pip freeze > requirements.txt`.

Python 3.5 is recommended for this project.  It can be downloaded and installed at [python.org](python.org).

## Frontend
The frontend source is written using Angular and Angular UI-Router.  

## Development Environment
A Unix dev environment is recommended because the setup instructions provided are known to work in these environments using a bash terminal.  The instructions may work in a Windows bash terminal but have not been tested.

## Production Environment
A Linux production environment is recommmended, and Ubuntu version 12 and greater is preferred.  A database will be needed and configuration for the database will need to be provided.  See below for database configuration.

## Database configuration
Both production and development environments use MySql for a DBMS and require a database configuration specific to the individual environment.

#### Development
For development, a subset of data is used for testing and provided by ghtorrent [here](http://ghtorrent.org/msr14.html).  Use this link to download the database, and after successful download, unpack the archive to your desired location.  Take note of the location.  The supplied data requires a database to hold so we need to create one using MySql.  The installation of MySql varies on the package manager being used, so it is assumed MySql is installed and running.

Open the MySql interpreter with root access using: `mysql -u root -p`.  If you have a password setup for the root MySql user, you will be prompted to enter it.  Create a database to hold the data by running `create database msr;`.  This names the databae 'msr'. You can name it however you like.  Create a user for the database by running `create user 'msr'@'localhost' identified by password;`. The password will need to be added to the local_settings.py file for database connection, and please do not commit the password, or any passwords, to the repository.

The user needs to have access to the database. Run `grant all on msr.* to 'msr'@'localhost;`.  After commands have been run successfully, run `quit;` to exit the interpreter.  We can now load the data into the database by running `mysql -u root -p msr < path_to_extracted_data_file`.  The `path_to_extracted_data_file` is the absolute path noted earlier, and `msr` is the name of the database created.  Once this is successful, you can enter the information into the local_settings.py.

Located in the `repo_health` directory of this repository is a `local_settings.py.example` file. Save a copy of this file as `local_settings.py` to the same directory.  Please do not remove the example file from the repo.  If you created the database and user as `msr` then you will need insert the password for the user in the `PASSWORD` placeholder.  Otherwise enter the required information into the correct places and save the file.

#### Production
Production database is configured in a similar fashion, but the project is not ready for a production setup so this will be revisited.

## Development setup

### Backend Configuration
Developers develop on many projects, and each project has it's own dependancies or deps.  
For this reason, a virtual environment is created on the developer's machine in order to isolate Python dependancies between projects.  
Virtualenv and virtualenvwrapper are used to create and maintain the environment and need to be installed in the base Python using the pip command line tool.  
An explanation of how to install pip is [here](https://pip.pypa.io/en/stable/installing/), but if you can run `which pip` and see a result, you have pip installed.  
To install virtualenv and virtualenvwrapper use:
  `pip install virtualenv virtualenvwrapper`
and wait for a success message.
Some environment variables need to be set and is explained [here](http://virtualenvwrapper.readthedocs.io/en/latest/install.html), but a bare bones setting is:
- Open up your .bash_profile or .bashrc
- Add the following lines:
   `export WORKON_HOME=$HOME/.envs
   source <(echo which virtualenvwrapper.sh)
   ` 
- Run `source ~/.bash_profile` or `source ~/.bashrc` depending on what file you edited and verify no errors.
Once this is configured, you are able to run commands such as `mkvirtualenv`, and `workon` with no errors (maybe a usage message).
To create a virtualenv for our project:
- Run `which python3` and copy the output
- Run `mkvirtualenv <virtualenv name> -p <paste output of previous command>`.  The name of the virtualenv is of your choosing.
If this is successful, you will see the command prompt change to begin with `(<virtualenv name>)`.  You are now working inside your virtualenv and running `which python` should result to a path in your `~/.envs` folder.
To stop using the virtualenv, run `deactivate`.
To start using the virtualenv, run `workon <virtualenv name>`.
From inside the virtualenv and in the project root folder, run `pip install requirements.txt` to install the deps from the file.
Once successful, run `cd project` to change dir and `python manage.py migrate` to create the database and all the default tables.
Run `python manage.py runserver` to start the built in dev server, and navigate a browser to [http://localhost:8000](http://localhost:8000) to view the index page.

### Frontend configuration
Frontend confuration is yet to be determined.


#### Some common commands to help determine what python is being used
- `which python` or `which python3`
  - Shows path python version.
  - The `python3` should display version 3.5 when development is configured correctly.
- `python --version` 
  - Show current version of Python used by the command line command.

### Production setup
The app is not ready for production yet so this part is incomplete.

Assumptions made about production:
- Operating system: Ubuntu 12.04 or greater
- Application will be running in it's own isolated environment, and a virtualenv is not needed.
- Apache httpd server is used to serve app using mod_wsgi.
- All static files are served from Apache using a redirect from url `/static/` to a static documents folder. This folder is created using `python manage.py collectstatic`.  This is not necessary in development.

