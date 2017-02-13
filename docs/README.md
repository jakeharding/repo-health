#REST API README    

##Purpose
GitHub maintains a REST API so why do we need another? 
 - The reason to host and supply the data independentluy of GitHub enables us to structure the data in a fashion suitable for our purpose.

This presents a challenge in updating our database to stay current.  We recognize the need for data synchronization as an external entity of our system and outside the scope of our purpose. The documentation here provides structure and details for the repo_health REST API, which works with the msr14 database downloaded from GhTorrent [here](http://ghtorrent.org/msr14.html). This database is a subset of data and appears to be outdated.  This means many structure changes have likely occurred and will need to be accounted for when updating the database.

The repo_health REST API accepts and returns JSON.

Thank you to GhTorrent for providing the needed data and structure to get us started.