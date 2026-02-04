Installation
============

Requirements
------------

jmaplib requires Python 3.9 or later.

Installing from PyPI
---------------------

The easiest way to install jmaplib is from PyPI using pip:

.. code-block:: console

   pip install jmaplib

This will install jmaplib and all its required dependencies.

Installing from Source
----------------------

If you want to install from source (for development or to get the latest unreleased features):

.. code-block:: console

   git clone https://github.com/smkent/jmaplib.git
   cd jmaplib
   pip install .

Development Installation
------------------------

For development, it's recommended to use Poetry:

.. code-block:: console

   git clone https://github.com/smkent/jmaplib.git
   cd jmaplib
   poetry install

This will install jmaplib in development mode along with all development dependencies.

Verification
------------

To verify that the installation was successful, you can run:

.. code-block:: python

   import jmaplib
   print(jmaplib.__version__)

This should print the version number of jmaplib without any errors.
