# EZ-file-sharing-system-py-flask
A simple file-sharing system built with Flask, SQLite, and JWT-based authentication.  
app deployed at : https://ez-file-sharing-system-py-flask.onrender.com

Learning from this project:  
Learned to Create Flask app    
Handeling API requests GET POST  
debugging  
Deploying to RENDER
Working with Sqlite and Flask CRUD operations and etc


postman collection: postman dump/EZ File Sharing System.postman_collection.json

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
{      
    "Content-Type": "application/json"      
}      

Request Body:         
{      
    "username": "example_user",      
    "email": "user@example.com",      
    "password": "password123",      
    "is_operation_user": true      
}      

Response (Success):         
{      
    "msg": "User registered successfully"      
}  

Response (Error - Missing parameters):        
{        
    "msg": "Missing required parameters: username, email, and password are required."      
}     

Response (Error - Username already exists):          
{      
    "msg": "Username already exists"      
}      

Response (Error - Email already exists):        
{      
    "msg": "Email already exists"    
}      

2. User Login      
URL: /login      
Method: POST      
Description: Allows a user to log in using their username and password. Upon successful login, a JWT token is returned.        
      
Request Headers:                   
{            
    "Content-Type": "application/json"            
}                 

Request Body:              
{            
    "username": "example_user",      
    "password": "password123"      
}            

Response (Success):      
{          
    "msg": "Login successful",      
    "access_token": "your_jwt_token_here"      
}      

Response (Error - Invalid username or password):            
{      
    "msg": "Invalid username or password"      
}    

Response (Error - Missing parameters):           
{      
    "msg": "Missing required parameters: username and password are required."      
}      

                                                                                   
$.Upload File (/upload)         
Method: POST         
Description: Allows operation users to upload files.     

Headers:         
Authorization: Bearer <your_jwt_token>      

Request Body:         
file: The file you want to upload.    

Success Response:                           
{                                                               
  "msg": "File <filename> uploaded successfully"                           
}     

Error Responses:                                                                                          
{                                                      
  "msg": "Missing Authorization Header"                           
}                                             
                  
{                                                      
  "msg": "token must be a Bearer token"                                    
}                                                      
                          
{                                                                                                                                                                                         
  "msg": "You are not authorized to upload files. Only operation users can upload."                  
}                                    
                          
{                                                      
  "msg": "No selected file"                                    
}                                                      
                          
{                                                                                 
  "msg": "Invalid file type. Only .pptx, .docx, and .xlsx are allowed."                           
}                                                          

5. Generate Download URL (/generate_download_url/<filename>)                           
Method: GET                                                               
Description: Generates a secure download URL for a file.
                                 
Headers:                                                      
Authorization: Bearer <your_jwt_token>                

URL Parameter:                                    
filename: The name of the file.       

Success Response:                                                                                        
{                                                                                          
  "download_url": "http://localhost:5000/download_file/<download_token>",                           
  "message": "Success"                                             
}    

Error Responses:                                                                                                                              
{
  "msg": "Missing Authorization Header"                                             
}                                                                       
                                  
{                                                               
  "msg": "token must be a Bearer token"                           
}                                                         
                                    
{                                                      
  "msg": "File not found"                                    
}                                                                                
                          
{                                                      
  "msg": "only client user can download the file"                                    
}

7. Download File (/download_file/<download_token>)                                    
Method: GET                                                                        
Description: Allows a user to download a file using a secure token.
                              
URL Parameter:                                                                        
download_token: The secure token generated by /generate_download_url.       

Success Response:                                    
The file will be downloaded.                           

Error Responses:                                                                                                         
{                                                      
  "msg": "Invalid or expired token"                           
}         
                  
