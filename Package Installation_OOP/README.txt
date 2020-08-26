Detailed Package explaination
- distributions, which contains the code for the distributions package including Gaussiandistribution.py and Generaldistribution.py code.
- setup.py a file needed for building python packages with pip
- test.py unit tests to help you debug your code
- numbers.txt are data files used as part of the unit tests

How To Run
- Download the folder
- Go to the path folder that contains set.py and distribution
- Open the terminal and run "pip install ." . It will look for a package and install it locally
- Notice inside distributions folder, __init__.py indicates this is a package
- The dot in front of Generaldistribution is required in python 3 when installing packages.
- Here is the explaination for a signle dot, 2 dots, three dots: https://realpython.com/lessons/relative-imports-python/
- Note that if you change the code in the distributions folder after pip installing the package, Python will not know about the changes. You'll need to run `pip install --upgrade .` when you make changes to the package files.

Example:
- Open terminal, type 'python'
- import distributions
distributions.__file__ (to see the package installation location)

- from distributions import Gaussian
- gaussian_1 = Gaussian (10, 5)
- gaussian_1.mean
