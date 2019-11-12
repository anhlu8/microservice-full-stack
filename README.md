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
Successfully ran from local Postgres database & inside a Docker container.

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

# Connect to Containerized Postgres:
Make sure local Postgres is stopped.
- Host name: 0.0.0.0
- Port: 5432
- Database: flask
- Username: postgres
- Password: example

# To push/update image to AWS ERC:
Run `aws ecr get-login --no-include-email`, then copy and paste token in Terminal
Run `./upload-to-ecr.sh`

# Continuous Improvements:
* Front-End: Create PWA, Deploy Build folder to S3, Refactor to use Hooks & TS.
* Back-End: Create Restful APIs (Right now, it's missing PUT & DELETE)
* DevOps: CI/CD