********************************* eSaumudaay Demo ********************************* 

# Overview :-
This is a simple demo project. It is an application server with a single API. The API takes as input items ordered, delivery distance, and offer applied. The response is the total order value.


## INSTALLATION :-
1. Clone the repo in your local system.

2. Create a virtual environment.
    - MAC users :-
        Refer to :- https://gist.github.com/pandafulmanda/730a9355e088a9970b18275cb9eadef3

    - Windows and Linux users :-
        Refer to :- https://www.geeksforgeeks.org/creating-python-virtual-environment-windows-linux/

3. Install Requirements
    Change directory to the root folder and run
    
    `pip install -r requirements.txt` 

4. Make migrations and migrate.
    Run these commands

    `pip manage.py makemigrations` and `pip manage.py migrate`

5. Start the server.

    `pip manage.py runserver`

6. You are good to go. Happy hacking !


## Important Technical Decision :-
1. Creating separate utility functions so that all the *Computations* are carried out at a single place.

2. Having a separate *Const.py* file to store all the constants used in each app.

3. Using and `OrderedDict()` to store the range for calculating delivery_fee. This was done to have a *configurable slab*.


## Note :- 
1. Added a *Order* Model to keep track of all the requests made to our server.

2. Added `postman_collection.json` file, the test cases can be found there

3. Added postman_samples folder for postman screenshots.