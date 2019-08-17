# MNIST

# Introduction 
The goal of this project is to predict the numbers in the corresponding images uploaded by users of the program. Also, to make sure of the efficiency of transferring and storing data, the virtual container Docker is included in this project. 
Specifically, Convolutional Neural Network(CNN), a trained model of which is deployed into Docker, is used to predict the handwriting numbers. The results of predictions are given to two locations at the same time. First, by RESTful API, results can be transferred to the website that this project established earlier, users can see the results predicted on the website directly. Second, the predictions of the results are recorded in the phpMyAdmin databases, including both the numbers and the time used to make those predictions correspondingly.

# How to use?
Open the html. Click "Choose File", and upload images. Click "predict", and then you will get the results.

# Preparations
Due to the problem of the directory in this project, users should do several things before running it.

First, create an empty file named "model".

Second, create an empty file named "package", and put file "pycache", "init1.py", "MNIST_data", "MNIST.py", "model", "output.py", "process_image.py", "templates" into "package".

Third, create an empty file named "mnist", and put "package" and "requirements.txt" into "mnist".

Forth, create an empty file named "docker_mnist", and put "mnist" and "Dockerfile" into "docker_mnist".

Before other operations, users should run "MNIST.py", the trained model of which will be sotred in "model".



# Operations
The last work is Docker Construction. Users are suggested to follow the instructions to make sure the process goes well.

1) Download phpMyAdmin and MySQL from Docker registry:

docker pull phpmyadmin/phpmyadmin

docker pull mysql:5.6

2) We need two Docker containers, which are the container runs the main service and records data in database, and the container implements the database and receives the data.

Start the two Docker containers :

docker run --name test-mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=root -d mysql:5.6

docker run --name test-phpmyadmin -p 8080:80 --link test-mysql:db -d phpmyadmin/phpmyadmin:latest

In this case, two containers expose phpMyAdmin and MySQL to port 8080 and port 3306.

3) Go to the website by typing “the default IP of Docker machine” + “:8080”, and then sign in to phpMyAdmin with “username” and “password” (both of them are root).

4) Create “database mnist”, and create table “picture_information”.

5) Use the following SQL query to create table image_information ： CREATE TABLE test.image_information ( name VARCHAR(50) NOT NULL , timeDATETIME NOT NULL , output INT NOT NULL )
