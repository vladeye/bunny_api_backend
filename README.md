SETUP

The project is in python with the framework django

The virtualenviroment is venvbunny

To access the backend is in this url:
https://pure-hamlet-43893.herokuapp.com/ 

The app inside the project is called api

-In the file utils.py there are the classes that communicates with bunny api
-In test.py there are the unit test
Although the whole CRUD is working because the RetrieveUpdateDestroyAPIView API I only made unit test for:
	-Create Readings
	-Consult all the Readings
	-Consult one Reading


The application use database sqllite to save the status of the projects
It could be more than one project, these projects can be created through Postman you can use this json object:
{
	"title":"My Test Project 48",
	"script":"Mandarina",
	"test":1
}

Its important to be aware that when you create the object, the script attribute is just a key to the api that gets the text bring the actual script.
It uses the wiki api, so after the search of that key the results will be saved in the database.

To keep checking if the readings are already produced I used celery and I created a task tha is in the file tasks.py

Importat:
To create the project in bunnyinc I created a signal post_save in the models.py file.

