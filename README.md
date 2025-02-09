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

3. Install dependencies:
  
   ```bash
   pip install -r requirements.txt

## Running the Application:

4. **Start the Flask server**:

    ```sh
    flask run
    Visit [http://127.0.0.1:5000/](http://127.0.0.1:5000/) to see the API in action.

5. ## **API Endpoints**:

- **GET /**  
  Returns `"Hello, World!"`

- **GET /hello**  
  Returns `"Hello!"`

- **GET /hello/{name}**  
  Returns a personalized greeting.


## **Running Tests**:

5. To run tests, use:
    ```bash
    pytest

## **Deployment** (v1.0.0)

### AWS EC2  
Follow the steps to deploy on **AWS EC2**:  
1. Set up an EC2 instance.  
2. Install necessary dependencies.  
3. Run the Flask app.

### Docker  
Build and run the Docker container with:

  ```bash
  docker build -t flask-hello-world-api .
  docker run -p 5000:5000 flask-hello-world-api

