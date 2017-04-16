# Repository Health Project for CSCI 4900

[![Build Status](https://travis-ci.org/jakeharding/repo-health.svg?branch=travis)](https://travis-ci.org/jakeharding/repo-health)

This repository holds the proof of concept for the repository health and sustainability project for CSCI 4900 at the University of Nebraska at Omaha.  This repository will hold the backend and frontend source code to extract data from Github and ghtorrent and provide statistics about a selected repository.  Description of the backend and frontend source are provided.

This project is not meant to be in production. Charts for the user interface are not implemented yet, so arrays of integers are displayed where charts will be placed in the future.  

## Technologies
#### Backend
The Django web framework is used in the project to leverage quick development and the third party packages available.  Python requirements are kept in the requirements.txt file, and this file is generated using `pip freeze > requirements.txt`.

Python 3.5 is recommended for this project.  It can be downloaded and installed at [python.org](python.org).

#### Frontend
The frontend source is written in ES2015 using [Angular](https://angularjs.org/). We are using [Angular Material](https://material.angularjs.org/latest/) for our styles.   

## Installation
Docker is the preferred way to get an environment running. If you would like to not use Docker, please click [here](https://github.com/jakeharding/repo-health/blob/master/docs/Other%20Installation.md). Please note the Docker environment uses a development server and serves the backend application in a development state.  This is not safe for production use.

This was tested using v1.12.6 of [Docker](https://docs.docker.com/engine/installation/linux/ubuntu/) and v1.11.2 of [Docker Compose](https://docs.docker.com/compose/install/). Any version below these are untested.

Step 1: Clone `repo-health` onto your local machine. Run `git clone https://github.com/jakeharding/repo-health.git` to clone this repo.

Step 2: Make sure `mysql` is not running locally and that port 3306 and 8000 are free. If running on ubuntu, run `service mysql stop`.

Step 3: Go to the root folder of `repo-health` and run `docker-compose up`. This will run through all of our configurations. This process will take roughly 10 minutes.

Step 4: Once complete, a message will display saying that the server is listening to port 8000. You may now go to [localhost:8000](http://localhost:8000) to view this application.

## Development
To run UI tests:
```
cd repo_health/index/static
npm test
``` 
To run Backend tests:
```
python manage.py test
``` 

## Production setup
The app is not ready for production yet so this part is incomplete.

Assumptions made about production:
- Operating system: Ubuntu 12.04 or greater
- Application will be running in it's own isolated environment, and a virtualenv is not needed.
- Apache httpd server is used to serve app using mod_wsgi.
- All static files are served from Apache using a redirect from url `/static/` to a static documents folder. This folder is created using `python manage.py collectstatic`.  This is not necessary in development.

## License and Copyright
All source code is covered by the MIT license.  This license can be found [here](https://github.com/jakeharding/repo-health/blob/master/LICENSE.txt).

All other material, such as documentation, is covered by the Creative Commons - Attribution, or the CC BY license.

© 2017 Jake Harding and Benjamin Parish

## Contributing
External contributions are not being accepted at this time. For existing contributors, please use the following header documentation at the top of each file:

```
fileName.ext - (C) Copyright - 2017
This software is copyrighted to contributors listed in CONTRIBUTIONS.md.

SPDX-License-Identifier: MIT

Author(s) of this file:
  Your name or github username

Brief description of the file.
```
