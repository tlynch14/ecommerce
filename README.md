# YT_Django_Project_Ecommerce_v1_Part1
 
## Setting up Virtual Environment
1. Head to requirements.txt - observe required dependencies & align where necessary
2. cd to venv 
2. run `source venv/bin/activate`

## Running Project 
1. Within Ecommerce folder `python manage.py runserver`

## Admin Area 

## Testing 
1. `coverage run --omit='*/venv/*' manage.py test` Omitting the virutal environment folder. (Ensure you have coverage installed - if not `pip install coverage`)
2. Recommend `coverage html`

## Code Quality
1. Run `flake8` to observe inconsistencies with PEP8 code standards. See `setup.cfg` for flake8 config.
2. Run `isort .` to sort imports in all python files

--> Package this up into one script to flake8 && isort . && flake8 


## Cool Commands
1. `pip freeze > requirements.txt`
