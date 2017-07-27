# Repository Health Project for CSCI 4900

[![Build Status](https://travis-ci.org/jakeharding/repo-health.svg?branch=travis)](https://travis-ci.org/jakeharding/repo-health)
[![Coverage Status](https://coveralls.io/repos/github/jakeharding/repo-health/badge.svg?branch=travis)](https://coveralls.io/github/jakeharding/repo-health?branch=travis)

This repository holds the proof of concept for the repository health and sustainability project for CSCI 4900 at the University of Nebraska at Omaha.  This repository will hold the backend and frontend source code to extract data from Github and ghtorrent and provide statistics about a selected repository.  Description of the backend and frontend source are provided.

Please be aware this project is not ready for production use.

## Installation
Docker is the preferred way to get an environment running. If you would like to not use Docker, please click [here](https://github.com/jakeharding/repo-health/blob/master/docs/Other%20Installation.md). Please note the Docker environment uses a development server and serves the backend application in a development state.  This is not safe for production use.

This was tested using v1.12.6 of [Docker](https://docs.docker.com/engine/installation/linux/ubuntu/) and v1.11.2 of [Docker Compose](https://docs.docker.com/compose/install/). Any version below these are untested.

Step 1: Clone `repo-health` onto your local machine. Run `git clone https://github.com/jakeharding/repo-health.git` to clone this repo.

Step 2: Make sure `mysql` is not running locally and that port 3306 and 8000 are free. If running on ubuntu, run `service mysql stop`.

Step 3: Go to the root folder of `repo-health` and run `docker-compose up`. This will run through all of our configurations. This process will take roughly 10 minutes.

Step 4: Once complete, a message will display saying that the server is listening to port 8000. You may now go to [localhost:8000](http://localhost:8000) to view this application.

## Usage
Once the app is installed and running, visit the localhost link above to enter a Github repository URL such as: https://github.com/cakephp/cakephp.

You may also enter only the owner and repo name portion of the URL such as: cakephp/cakephp and acheive the same result.

Please be aware the data set currently used is outdated and does not contain all the repositories on Github today.

## Technologies
#### Backend
The [Django web framework](https://www.djangoproject.com/) is used in the project to leverage quick development and the third party packages available.

#### Frontend
The frontend source is written in ES2015 using [Angular](https://angularjs.org/). We are using [Angular Material](https://material.angularjs.org/latest/) for our styles. 

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

## License and Copyright
All source code is covered by the MIT license.  This license can be found [here](https://github.com/jakeharding/repo-health/blob/master/LICENSE.txt).

All other material, such as documentation, is covered by the Creative Commons - Attribution, or the CC BY license.

© 2017 Jake Harding and Benjamin Parish

## Contributing
Please visit the [contributing documentation](https://github.com/jakeharding/repo-health/blob/master/CONTRIBUTING.md) for information on contributing to this project.
