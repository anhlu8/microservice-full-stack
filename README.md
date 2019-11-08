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

##

# Continuous Improvements:
* Front-End: PWA, Containerize it for local development, Deploy Build folder to S3, Refactor to use Hooks & TS.
* DevOps: create Makefile, create docker-compose.yml to run Flask/Postgres in containters


## Commands:
docker-compose ps
docker-compose build
docker-compose up -d
docker-compose down
docker-compose logs -f
docker-compose stop
docker-compose start
docker-compose restart
docker-compose exec web (this runs command line in that container)
docker-compose run (start another same container for you to try out commands again that container)

