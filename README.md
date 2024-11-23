# Django To-Do List Project

## Description
This project is a simple web application for managing a to-do list, built with Django. Users can create new tasks, mark them as completed, or delete them. The project supports filtering tasks by their status (completed or incomplete).

## Project Structure
- `models.py` — defines the task model.
- `views.py` — logic for handling requests and displaying tasks.
- `urls.py` — routing for different functionalities (task list, task creation, status toggle, deletion).
- `templates/` — HTML templates for displaying the task list and the form for creating new tasks.

## Functionality
### task_list
- Displays a list of all tasks.
- Allows filtering by status:
  - `all` — all tasks.
  - `completed` — only completed tasks.
  - `incomplete` — only incomplete tasks.
  
### create_task
- Allows creating a new task by filling out a title and description.
- After a successful task creation, the user is redirected to the task list.

### toggle_task_status
- Toggles the task's status between completed and incomplete.
- After the status change, the user is redirected back to the task list.

### delete_task
- Allows deleting a task.
- After deletion, the user is redirected to the task list.

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```

2. Navigate to the project directory:
   ```bash
   cd <project-name>
   ```

3. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On MacOS/Linux:
     ```bash
     source venv/bin/activate
     ```

5. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

6. Run migrations:
   ```bash
   python manage.py migrate
   ```

7. Start the server:
   ```bash
   python manage.py runserver
   ```

8. Open your browser and go to `http://127.0.0.1:8000/` to view the project.

## Technologies
- Python 3.x
- Django 4.x
- PostgreSQL (if used for the database)
- HTML, CSS (for creating templates)

## Authors
- Bogdan - Developer
