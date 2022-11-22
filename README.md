# Ebook

This is a Machine Test Task to create a small ebook management REST API with Django and SQLite to show CRUD operations.

API TESTING with CRUD Operations:
There we can add the inputs with the HTTP parameter as : POST with the URL : http://localhost:8000/ebook/ in the request part and view the output from response part.

We can see all the datas given with the HTTP parameters as : GET with the URL : http://127.0.0.1:8000/ebook/ in the request part and view the output from response part. Here you can also call the n^th input by specifying the position_number in the position of n in the URL as : http://127.0.0.1:8000/ebook/n/

We can also update the data in the database by using the HTTP paramenter as : PATCH with the URL : http://127.0.0.1:8000/update/n/ in which we have to mention the position_number in the place of 'n' in the URL from the request part of the the data in which we are going to make the updations and view the change from the response part.

We can delete the data from the database by using the HTTP paramenter as : DELETE with the URL : http://127.0.0.1:8000/ebook/n/
