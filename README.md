# pre-interview-task-incling

## Python - Django project.
Hosted API [link](https://pre-interview.onrender.com)
### Tech used:
- Python
- Django 4.1 (did not downgrade to 3.1)
- PostgreSQL
- Render (database hosting)

### Summary
Three folders are available:
- pre_task = Django project folder
- task = task app with task and type models
- tile = tile app with tile and status models

### Notes
Task and Type models are connected as 1-1 relationship, as well as Tile and Status models. Tile and Task models are connected as many-to-many relationship. (Tried many to one but did not seem to work smoothly, may have to look more into that.)
