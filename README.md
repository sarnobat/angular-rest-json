angular-rest-json
=================

Hello World Angular JS example that calls a minimal Python REST service (implemented with Bottle), returning JSON, with Cross Origin Resource Sharing (CORS) enabled  

Quick Start
-----------

1. Start the server

        sh server.sh

2. Deploy the client in your Apache instance

        cd htdocs
        ln -s angular-json-rest .
(note: all parent dirs of the physical target must have the right permissions)
        
3. Go to [http://localhost/angular-json-rest/index.html](http://localhost/angular-json-rest/index.html)

Errors, ambiguities, omissions?
-------------------------------

Please [create an issue](https://github.com/sarnobat/angular-rest-json/issues/new)