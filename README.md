# EZ-file-sharing-system-py-flask
A simple file-sharing system built with Flask, SQLite, and JWT-based authentication.  
app deployed at : https://ez-file-sharing-system-py-flask.onrender.com

Learning from this project:  
Learned to Create Flask app    
Handeling API requests GET POST  
debugging  
Deploying to RENDER
Working with Sqlite and Flask CRUD operations and etc


postman collection: https://api.postman.com/collections/22131487-f0e1f47e-efdd-45f3-8108-a5481dfb0401?access_key=PMAT-01JD02ZMC7BCBRWZ33G86K06BA     

Requirements    
Python 3.x      
Flask: Lightweight Python web framework.  
Flask-JWT-Extended: JWT authentication for Flask.  
SQLAlchemy: ORM for interacting with the SQLite database.    
Werkzeug: Password hashing utilities.  
SQLite: Lightweight database (used in development).    
         

Create with a virtual environment and activate it:    
.venv\Scripts\activate  # Windows             

Running the Flask application:        
bash             
# For local development (Flask server)    
python app.py    

# For production (using Gunicorn)    
gunicorn app:app          

API Endpoints            
1. User Registration
URL: /register      
Method: POST      
Description: Allows a new user to register. The user must provide a username, email, and password. Optionally, the user can set the is_operation_user flag.      

Request Headers:        

json      
{      
    "Content-Type": "application/json"      
}      
Request Body:      

json      
{      
    "username": "example_user",      
    "email": "user@example.com",      
    "password": "password123",      
    "is_operation_user": true      
}      
Response (Success):      

json      
{      
    "msg": "User registered successfully"      
}      
Response (Error - Missing parameters):      
    
json    
{        
    "msg": "Missing required parameters: username, email, and password are required."      
}      
Response (Error - Username already exists):      

json    
{      
    "msg": "Username already exists"      
}      
Response (Error - Email already exists):    

json    

{      
    "msg": "Email already exists"    
}      

2. User Login      
URL: /login      
Method: POST      
Description: Allows a user to log in using their username and password. Upon successful login, a JWT token is returned.        
      
Request Headers:      
            
json             
{            
    "Content-Type": "application/json"            
}                                                          
Request Body:        
                
json      
{            
    "username": "example_user",      
    "password": "password123"      
}            
Response (Success):      
                          
json
{          
    "msg": "Login successful",      
    "access_token": "your_jwt_token_here"      
}      
Response (Error - Invalid username or password):      
        
json      
{      
    "msg": "Invalid username or password"      
}      
Response (Error - Missing parameters):      

json     
{      
    "msg": "Missing required parameters: username and password are required."      
}      

                                                                                   
                                

Future Enhancements                                                      
Implement file upload functionality for ops users only.                        
Allow client users to download files they uploaded.                                    
Add email confirmation functionality.                                
Improve error handling and validation.                
