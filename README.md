# Project Title

## Description
A brief description of what this project does and who it's for.

## Installation
Instructions on how to install and set up the project.

```sh
# Clone the repository
git clone https://github.com/RajThak-998/Course_Review.git

# Navigate to the project directory
cd Course_Review

# Install dependencies
pip install -r requirements.txt
```


## How to Run

1. **Clone the repository:**
    ```bash
    git clone https://github.com/RajThak-998/course_review.git
    cd course_review
   
    ```

2. **Create a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate # for fedora workstation
    ```

3. **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Apply the migrations:**
    ```bash
    python manage.py migrate
    ```

5. **Run the development server:**
    ```bash
    python manage.py runserver
    ```

6. **Open your browser and navigate to:**
    ```
    http://127.0.0.1:8000/
    ```

7. **Usage:**
    ```bash
    #Load initial data
    python manage.py load_assignment

    #Run the server
    python manage.py runserver
    ```


## Tech Stack
- **Backend:** Django

- **Frontend:** HTML, CSS, JavaScript
- **Database:** SQLite (default), can be configured to use PostgreSQL or MySQL
- **Version Control:** Git
- **Deployment:** Heroku, AWS, or any other cloud service
