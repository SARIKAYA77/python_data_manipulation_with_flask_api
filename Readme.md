● Developing an API with Python, taking the given input and output data as JSON and sending it to the person who made the request.
readable return.
● Performing manipulation operations

app.py --> It contains a flask endpoint and displays the incoming json data.Provides the manipulations needed to convert to the desired format.

api.py--> reads the json data and makes a request to the flask endpoint,prints the returned answer to the terminal

test.py --> Includes test operation on flask endpoint, tests the state of the response with assertEqual

data.json --> contains the relevant json data

how to run this project 
********************************
First step, install the requirements, see the requirements.txt file.
The app.py file should be run,
and flask server must be started,
for example: python3 app.py then;
the api.py file should be run.

notes
*********************************
By making a request in another way (like curl), via the terminal or from another code file, you can still get the same response while the flask server is running.