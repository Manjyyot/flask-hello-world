Flask Hello World API
This project is a simple Flask-based API that returns a "Hello, World!" message and allows for dynamic greetings using user input. It's an ideal starting point for developers learning Flask.

Key Features
Hello World Endpoint: Returns a static "Hello, World!" message.
Dynamic Greeting: Responds with personalized greetings based on user input (e.g., /hello/John returns "Hello, John!").
Automated Testing: Includes tests using pytest to ensure endpoint functionality.
Requirements
Python 3.6+
Flask 2.0+
pytest 6.0+
Installation
Clone the repository:
bash
Copy
Edit
git clone https://github.com/yourusername/flask-hello-world-api.git
cd flask-hello-world-api
Set up a virtual environment:
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # macOS/Linux
.\venv\Scripts\activate  # Windows
Install dependencies:
nginx
Copy
Edit
pip install -r requirements.txt
Running the Application
Start the Flask server:

arduino
Copy
Edit
flask run
Visit http://127.0.0.1:5000/ to see the API in action.

API Endpoints
GET /: Returns "Hello, World!"
GET /hello: Returns "Hello!"
GET /hello/{name}: Returns a personalized greeting.
Running Tests
To run tests, use:

nginx
Copy
Edit
pytest
Deployment
AWS EC2
Follow the steps to deploy on AWS EC2 by setting up an instance, installing dependencies, and running the app.

Docker
Build and run the Docker container with:

arduino
Copy
Edit
docker build -t flask-hello-world-api .
docker run -p 5000:5000 flask-hello-world-api
Contributing
Fork the repository, create a new branch, make changes, and submit a pull request.

License
MIT License.
