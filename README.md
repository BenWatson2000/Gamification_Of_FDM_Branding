# Project: Gamification of FDM Branding
###### Created by: Ben Thompson-Watson, Dimitrios Tsatsoulas, Iga Koryciarz, Lakshman Santhanam and Megan Stone

---
This document contains a description of the project and credentials to the admin and helper pages along with 
instructions for developers on how to run the system locally.

##Introduction

The product developed is a web application which greets the user with a homepage showing three 
different career streams, Software Testing, Business Intelligence and Technical Operations. 

The user can select these streams manually or be offered a suggestion from a personality test. 
* The personality test consists of a set of 5 questions with a selection of answers for each. Answers 
are all correct however each one provides a different insight on which stream the user may best fit into.
  The results will provide a pie chart showing a clear indication of what stream the users responses have converged
  towards.

For each of the streams there will be 3 different games to play, all tailored to the selected stream.
* i.e. If you selected a game on the software testing stream, you will expect questions about software testing.

**Games Available:**

* Cable Game - The user must connect questions to answers using cables. The game will finish when
  all the cables are connected correctly, completing the circuit or if the time runs out. To control the cable, the 
  user just needs to click on the cable end on the left and to connect it to the answer you click on the cable end on 
  the right.
  <br><br>
* Pipe Game - The user directs the flow from a question pipe to a receiving pipe showing the correct answer. This
  will involve clicking on different pipes on the grid, rotating them and altering the flow path to ensure it goes to 
  the correct answer. There are 3 answers displayed, and the correct answer location is always random. To win you
  must direct the flow to the correct answer before the time runs out. 
  <br><br>
* Memory Game - The user must match up pairs of hidden icons on a grid by clicking on them and learning the location
of these icons. When a match is found, the pair is shown and coloured green on the grid, when a match is incorrect then
  the two icons selected flash red to indicate they are incorrect. The user must find all the matching pairs before the
  time runs out.
  
**Administration:**

There are two forms of admin pages on our application.
* Django's built in admin page where a 'superuser' can have complete access to all the tables in the database and modify 
  the data.
* Our FDM helper page where a 'helper' can add new questions to the database, look at the existing questions and query
the high scores for each game type.<br><br>
  
  Credentials:
  
  | Username        | Password           | Access to|Accessed via  | 
  | ------------- |:-------------:| -----:| -----:|
  | team4admin      | our3ChipDoor | Django Admin Page |'home-url/admin' | 
  | team4helper      | SAqYgYhaPD      | FDM Helper Page|   Helper page button in footer |


  *note that both accounts can access the helper page however only the superuser can access the django admin page.
  <br><br>Superuser are statically created and helper accounts can be registered on the app and then approved by a 
  super user. This prevents anyone from making a helper account and then adding their own questions to the games.
  <br><br>


  We have also created a team Gmail account to be able to send real password reset emails to our helper users. <br>
  The credentials for this account are as follows:

  * Email address: team4helper@gmail.com <br>
  * App password generated by Gmail: ppvjxlyqglrpzuvm<br>
    *required by Django to control the emails being sent from Gmail account
  
##Instructions to run system locally

###Required software:

 | Software        | Version           | 
  | ------------- |:-------------:| 
  | Pycharm Professional (JetBrains)      | 2020.3 or later |#
| Python      | 3.9 |

*note there are other dependencies in a requirements.txt file and a Pipfile. Please install these into either a 
virtualenv environment or pipenv environment. I have provided both just in case you had a preference. 

If there is an
issue installing mysqlclient try running ```pip install libmysqlclient-dev```.

###How to run:

1. Unzip project folder and open in pycharm.
2. Setup interpreter on python 3.9 and install dependencies from either the pipfile or requirements.txt.
3. Run the command ```python manage.py runserver``` and click the link that will look like 
 ```http://127.0.0.1:8000/```.
4. This should greet you with our homepage in your preferred browser. We have tested our application in Chrome, Firefox,
Safari and Microsoft Edge, so we recommend you use one of these.
   
Along with this local instance of the web app, we also have hosted an instance on the web at the domain 
https://mycareerpath.co.uk/.