# Flask Blog Application

This is a Flask web application for a simple blogging platform where users can sign up, log in, create blog posts, view their profile, and log out. The project includes user authentication and uses MongoDB for storing user data and blog posts.

## Table of Contents

- [Project Setup](#project-setup)
- [Running the Application](#running-the-application)
- [Project Structure](#project-structure)
- [Routes](#routes)
- [Templates](#templates)
- [License](#license)

## Project Setup

### Prerequisites

- Python 3.x
- MongoDB

### Installation

1. **Clone the repository:**
    ```sh
    git clone https://github.com/yourusername/flask-blog.git
    cd flask-blog
    ```

2. **Create and activate a virtual environment:**
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**
    ```sh
    pip install -r requirements.txt
    ```

4. **Start MongoDB:**
    Ensure that MongoDB is running on your machine. The default connection is `localhost:27017`.

## Running the Application

1. **Start the Flask application:**
    ```sh
    python app.py
    ```

2. **Access the application:**
    Open your web browser and go to `http://localhost:5000`.

## Project Structure

flask-blog/
│
├── templates/
│ ├── dashboard.html
│ ├── make_post.html
│ ├── profile.html
│ ├── registiration.html
│ └── view.html
│
├── user/
│ ├── init.py
│ ├── models.py
│ ├── routes.py
│ └── db.py
│
├── app.py
├── requirements.txt
└── README.md

## Routes

- **Home Page** (`/`): The main landing page of the application.
- **Sign Up** (`/user/signup`): Route to handle user registration.
- **Log In** (`/user/login`): Route to handle user login.
- **Log Out** (`/user/signout`): Route to handle user logout.
- **Dashboard** (`/dashboard/`): The main dashboard where users can see all blog posts.
- **Make a Post** (`/user/make_post`): Page to create a new blog post.
- **Create Post** (`/user/create_post`): Route to handle creating a new blog post.
- **View Profile** (`/user/profile`): Page to view user profile information.

## Templates

- **dashboard.html**: Displays the list of blog posts and user actions (create post, view profile, log out).
- **make_post.html**: Form to create a new blog post.
- **profile.html**: Displays user profile information.
- **registiration.html**: User registration form.
- **view.html**: Main landing page.
Note:
Ensure that your MongoDB instance is running on the default port (27017) and is properly configured in user/db.py:
