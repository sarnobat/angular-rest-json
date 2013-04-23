angular-rest-json
=================

This is a Hello World Angular JS example page that calls a minimal Python REST service (implemented with Bottle), returning JSON, with Cross Origin Resource Sharing (CORS) enabled.

Quick Start
-----------

1. Start the server

        sh server.sh

2. Deploy the client in your Apache instance

        cd $APACHE_HOME/htdocs
        ln -s angular-json-rest .
(note: all parent dirs of the physical angular-json-rest directory must have the right permissions)
        
3. Go to [http://localhost/angular-json-rest/index.html](http://localhost/angular-json-rest/index.html)

Errors, ambiguities, omissions?
-------------------------------

Please [create an issue](https://github.com/sarnobat/angular-rest-json/issues/new)

Requirements
------------
* Python
Everything else should be included in the repository.
