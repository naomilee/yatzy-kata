
# This directory contains a refactorization of the Python Yatzy Kata

The refactorization is based on python language conventions, readability, maintainability, accurate Yatzy scoring, and PEP-8 styling 

### To run the unit tests from inside a Docker container:

1. Navigate to this directory (yatzy-kata/python)
1. Execute:
    1. docker build -t yatzy-kata .
    1. docker run yatzy-kata
1. The output of the unit tests will be printed to stdout
1. Any other Yatzy-related program can be run (instead OR in addition), by simply placing it in this directory (yatzy-kata/python) and 
   modifying the last line of the Dockerfile