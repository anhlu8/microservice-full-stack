# Goals:

- Must-haves: 
    * Learn/Implement microservices & distributed development systems in DevOps.
    * Create a CI system  
- Should-haves: Restful APIs server & full CRUD operations client

### I. Client (React):
Successfully make AJAX calls to Flask server.
* `React.js` (JavaScript)
* `Material-UI`
* `Axios`


### II. Server (Flask):
Successfully run on local & inside Docker container. Succesffuly add volumne (mounting). Successfully add/query data to local Postgres database

* `Flask` (Python)
* `flask_cors`

### III. Database (Postgres):
Successfully ran from local Postgres database

* Local database config: server/db/config/postgreSQL.ini
* Models: Right now only takes first_name, last_name
* ORM: `flask_sqlalchemy`
* Serializer/Deserializer: `marshmallow_sqlalchemy`

# Usage:
### To run locally, and use local database:
- In `server.py`, uncomment line 12 and comment out line 13
- Create virtual environment and activate it
- Install requirements
- Run `python server.py`

### To run in containers (web app container & postgres database container):
- In `server.py`, uncomment line 13 and comment out line 12
- Run `docker-compose up -d` at the root
- Check logs: `docker-compose logs -f`
- Kill containers: `docker-compose down -d`


# Continuous Improvements:
* Front-End: Include client in container, PWA, Deploy Build folder to S3, Refactor to use Hooks & TS.
* DevOps: CI/CD


