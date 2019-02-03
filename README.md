# Person-Repository-Service
App backend to store user details based on flask app.

API Guide for APP :https://github.com/vinsan14249/Person-Repository-Service/wiki/Person-Repository-ServiceAPI-Guide 

Problem Statement

    Imagine you have to design a service which will help you to manage all the new and existing users 
    for a company. Let us call this Person Repository Service. It must be a REST-API based service with backend on python or java. It is expected to handle all exceptions, have proper test cases and handle  all edge cases. Also, Deploy the API’s on your personal AWS Account.

    The service needs to fulfil the following requirements. 

    A. Functional  Requirements
      1.  CRUD operations (Response should be in form of JSON format preferably for each of the operation) - 
         -   Create a new User and store it in a data store.
             You can take in First name, Last Name, Age and add a unique ID for any new user.
          -  Read an existing user from the data store.
           - Update the information of an existing user from the data store.
            - Delete any existing user from the data store.

        BONUS QUESTIONS (Optional)
        2. You should be able to search for all the persons based on first name, last name or both. 
        The response will be preferred in form of JSON format with all the details of each person matching 
        the criteria.
        3. You should be able to search for all the persons based on their age. The response will be preferred
         in form of JSON format with all the details of each person matching the criteria.

    B. Non-Functional Requirements (Optional)
        You must explain why and how will you make the service highly available and consistent.
        You must explain how can you reduce the search latency to view the results in real-time.
        Can you think how you can handle a heavy load of read operation for persons ?
*********************************************************************************************************************************


Features 
* Modular Structure App
* -> Each Api works on single task
* -> Each utility functions for a single task of its own 
        
        
Solution 

Entities :
```
user_id (Unique id):
- first_name
- last_name
- age
if no user-id :
    # Read all existing users
else :
     Read a specific existing user's details using  :
        - user_id
        - first name
        - last name
        - full name

```
 

## API’s Summary :
```
/user       POST    -   create_user()
/users  -   GET     -   get_all_users()
/searchbyid/<user_id>   -   GET     -   get_user_by_id
/search     -   POST    -   get_user_by_name
/update     -   POST    -   update_user_details
```
