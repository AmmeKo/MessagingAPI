# MessagingAPI
## Table of Contents
* Overview
* Technologies Used
* Setup
* Testing
* Additional Comments


## Overview
This code creates a basic API for users to send and receive messages. 

It allows for the following functions:
* Create user and edit user name. User_ID is automatically generated and unique.
* Send message from one user to another using the recipient's User_ID.
* Delete individual messages using the Message_ID.
* Delete individual users using the User_ID. Deleting a user will also remove all messages associated with them.

The program allows users to retrieve the following information:
* A list of users (/users)
* A list of a messages a user has sent (<user_id>/sent)
* A list of messages a user has received (<user_id>/received)
    * Only 100 most recent messages or those sent/received within the past 30 days from the request time are displayed.


## Technologies
The project was created with:
* Python 3.7
* SQLite3


## Setup
To run this API locally, set up a virtual environment using the requirements.txt included.
Run ````main.py```` from the command line.


## Testing
Be sure to run the provided test BEFORE utilizing the program to avoid any lost/altered data.

To test this API locally, go to the main project folder in the command line and activate the virtual environment.
Execute the ````pytest```` command.

If all tests are successful, the API is working!
The messagingAPI.db file will have been created but both the users and messages tables will be empty if the test is run prior to any other program usage.


## Additional Comments
There are a few things that I would add/edit to this project if I were to continue developing it:
* Add a foreign key restriction for the recipient in the messages table to ensure that the recipient is a current user in the database.
* Add the ability to delete multiple messages or users at once.
* Add additional criteria options for deleting messages (ex. recipient or date)
* Handle timezones in the datetime entries for messages
* Allow the ability to send messages to multiple recipients
* Expand on testing abilities in the test_api.py to better test content and avoid any potential data loss when run after program has already been utilized
