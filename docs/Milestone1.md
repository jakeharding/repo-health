#Milestone 1    

##System Description
The information system being built provides an unbiased evaluation of a GitHub repository using data collected by the GHTorrent project.  The system is a web based interface and retrieves data about a GitHub repository using a URL specified by the user.  The intent is to provide the user with usable information about a GitHub repository so the user can make an informed decision about the health and sustainability of the repository and the community supporting it.  The system is not meant to provide any value to the statistics.  

The system has many parts.  The backend server serves data to the web client using a REST API in the JSON format.  The web client uses the JSON data to render the visualization of the data.  

The current state of the system is in a proof of concept and not ready for a production environment.  The proof of concept supplies basic statistics about a repository and leaves out complex manipulation.  

##Development Environment
Our development environment consists of several different tools. Our development operating system is a Linux/Unix (Mac) environment. Our database management system is MySQL. Our server is running on Python 3.5+ and is using the Django web framework and dev server. We is using Python’s `virtualenv` to keep every developers python environment the same. Our front end is using the node package manager (npm) to manage and keep our dependencies in sync.


##Data Flow Diagram
Our Data Flow Diagram can be found [here](https://github.com/jakeharding/repo-health/blob/master/docs/Data%20Flow%20Diagram.pdf).

##Database Schema
We are using ghtorrent's schema. It can be found [here](http://ghtorrent.org/files/schema.pdf).

##Copyright and License
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

##Contributions
#####Jake:
- Backend implementation
- Documentation
####Benji:
- Frontend  implementation
- Documentation
