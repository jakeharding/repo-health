# Milestone 3    

## System Description

The system is a web based user interface and retrieves data about a GitHub repository using a URL specified by the user. The source code for the system is hosted on GitHub at: https://github.com/jakeharding/repo-health.

The intent is to provide the user with usable information about a GitHub repository so the user can make an informed decision about the health and sustainability of the repository and the community supporting it.

The system has many parts.  The backend provides a connection to the database, serialization of the data, and serving the data to the client in JSON format. The web client uses the JSON data to render the visualization of the data.  Both parts are included in the source code repository for convenience, but the system is built so the separation of the frontend and backend can be easily achieved.

The current state of the system is in a proof of concept and is not ready for a production environment.  The proof of concept supplies basic statistics about a repository and leaves out complex data manipulation.

Rendering of charts has been left out in this milestone but the data is still present in the user interface as a list of numbers.

## Development Environment
Our development operating system is a Linux/Unix (Mac) environment and our database management system is MySQL. 

Our server is running on Python 3.5+ and is using the Django web framework and dev server. Python’s `virtualenv` is used to keep every developers python environment the same.

Our front end is using the node package manager (npm) to manage and keep our dependencies in sync.

Docker is used to create an instance of the system as fast as possible.

## Posted Repository Issues
Jake - 
Benji - https://github.com/Dreizan/Repos-Health-Study

## Walk-through of system
Our system consists of an API and a UI that work together. After deploying our software, when you go to the website, you should be asked to enter a github url (name/repo). After entering a url,
if it exists you will be presented with a new page. If it doesn't work, then you will see an error. After it was successful, you will see the details of the repository. You can then
select issues or pull requests to see those statistics.

## Data Flow Diagram
Our Data Flow Diagram can be found [here](https://github.com/jakeharding/repo-health/blob/master/docs/Data%20Flow%20Diagram.pdf).

## Database Schema
We are using ghtorrent's schema. It can be found [here](http://ghtorrent.org/files/schema.pdf).

## Copyright and License
Licenses used for this project cover two areas: documentation and software.  The software is covered under the MIT license and the documentation is covered under CC BY.

Each file has the following documentation: 

```
fileName.ext - (C) Copyright - 2017
This software is copyrighted to contributors listed in CONTRIBUTIONS.md.

SPDX-License-Identifier: MIT

Author(s) of this file:
  Your name or github username

Brief description of the file.
```

## Contributions
##### Jake:
Jake is responsible for implementation of connecting to the database, the web server for the REST API, and all related documentation. 

##### Benji:
Benji is responsible for the frontend implementation. This includes UI/UX Design and the display of information from the server on the UI. All documentation for the frontend will be written by Benji.
