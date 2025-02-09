# Flask Hello World API
 
This project demonstrates the basics of building a simple API using Flask. It includes endpoints that return a static "Hello, World!" message as well as personalized greetings, along with automated testing using `pytest`.
 
## Key Features
 
- **Static Greeting**: A simple "Hello, World!" message.
- **Dynamic Greeting**: Personalized greetings with user input (e.g., `/hello/John` returns "Hello, John!").
- **Automated Testing**: Tests for verifying endpoint functionality using `pytest`.
 
## Requirements
 
- **Python**: Version 3.6 or higher
- **Flask**: Version 2.0 or higher
- **pytest**: Version 6.0 or higher
 
## Installation
 
1. **Clone the repository**:
   ```bash
   git clone https://github.com/manjyyot/flask-hello-world-api.git
   cd flask-hello-world-api
## Installation
 
2. **Set up a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # macOS/Linux
   .\venv\Scripts\activate  # Windows
 
## Install dependencies:
  ```bash
  pip install -r requirements.txt

## Running the Application:

## Start the Flask server:

  ```bash
  flask run
  Visit http://127.0.0.1:5000/ to see the API in action.
 
## API Endpoints
  GET /:
  Returns "Hello, World!"
 
  GET /hello:
  Returns "Hello!"
 
  GET /hello/{name}:
  Returns a personalized greeting.
 
## Running Tests:

To run tests, use:

```bash
pytest
Deployment
AWS EC2
Follow the steps to deploy on AWS EC2 by setting up an instance, installing dependencies, and running the app.
 
Docker
Build and run the Docker container with:
 
```bash
docker build -t flask-hello-world-api .
docker run -p 5000:5000 flask-hello-world-api

Contributing:
Fork the repository, create a new branch, make changes, and submit a pull request.
 
License
MIT License.
