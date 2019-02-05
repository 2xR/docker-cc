=================================
docker-cc: docker-compose-compose
=================================

A tool to aid in development of projects involving multiple docker-compose files.

Sample docker-cc.yml file
=========================

.. code-block:: bash

    docker-cc create foo '/some/dir/docker-compose*.yml'
    docker-cc use foo  # or docker-cc use ~/projects/foo/docker-cc.foo.yml
    docker-cc update  # (or refresh?) re-read input files and reload containers
    docker-cc up  # any docker-compose commands, really


.. code-block:: yaml

    name: foo
    includes:
    - /some/dir/docker-compose*.yml


Compatibility
=============

Developed and tested in Python 3.7+.


Installation
============

From the github repo:

.. code-block:: bash

    pip install git+https://github.com/2xR/docker-cc.git


License
=======

This library is released as open source under the MIT License.

Copyright (c) 2019 Rui Rei
