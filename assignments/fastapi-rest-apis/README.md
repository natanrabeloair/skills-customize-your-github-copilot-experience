# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small REST API with FastAPI by creating endpoints that create, retrieve, update, and delete tasks. Students will practice defining request data, handling HTTP responses, and using the FastAPI framework.

## 📝 Tasks

### 🛠️ Create the FastAPI Application

#### Description
Create the FastAPI application and define a task data model that represents the information stored by the API.

#### Requirements
Completed program should:

- Import `FastAPI`, `HTTPException`, and `BaseModel`.
- Create an application instance with `FastAPI()`.
- Define a `Task` model with `id`, `title`, and `completed` fields.
- Store tasks in an in-memory list.

### 🛠️ Add Task API Endpoints

#### Description
Implement REST endpoints for creating, retrieving, updating, and deleting tasks.

#### Requirements
Completed program should:

- Add a `POST /tasks` endpoint that creates a task and returns a `201 Created` response.
- Add a `GET /tasks` endpoint that returns all tasks.
- Add a `GET /tasks/{task_id}` endpoint that returns one task.
- Add a `PUT /tasks/{task_id}` endpoint that updates a task.
- Add a `DELETE /tasks/{task_id}` endpoint that removes a task.
- Return appropriate status codes and clear error messages when a task does not exist.

### 🛠️ Run and Test the API

#### Description
Run the application and verify the API behavior with FastAPI's built-in documentation.

#### Requirements
Completed program should:

- Run the application with `uvicorn`.
- Use the FastAPI documentation to test at least one create request and one retrieve request.
- Confirm that the API responds with valid JSON.
- Include a `GET /` endpoint that returns a short welcome message.

```python
uvicorn starter_code:app --reload
```
