# Hello World!
## Migrated from SQLite to MySQL db
>Database is now MySQL locally (when pulling from DockerHub, creates it's own table)

>Info does saving locally, you can read it, MySQL req.!

>Next stage is to push it in DockerHub and let someone to start it

### Use those commands to work with it:
`docker buildx build -t testingframework . `  ### to create an image

`docker run -p 8000:5000 testingframework `   ### to run a container

`docker run -p 8000:5000 --name testing-docker --mount type=bind,source="$(pwd)/instance",target=/app/instance testingframework `   
                                                                                                          ### to save docker container changes locally in db.sqlite
                                                                                                          (now it's in docker-compose.yml and MySQL, not SQLite)
```
#version: '3'
services:
  testing-docker:
    image: testingframework
    ports:
      - "8000:5000"
    volumes:
      - "./instance:/app/instance"
    container_name: testing-docker                                ### THE SAME AS PREVIOUS
```
`c:/Users/babiy/source/repos/Python/TestingFramework/.venv/Scripts/Activate.ps1 `             
                                                                        ### I dont remember exactly what this command did, but it's needed to run code in
                                                                                             Studio Code, and must be activeted when programm is about to work.       

```
 db:
    container_name: mydatabase
    image: mysql:latest
    volumes:
      - ./db:/var/lib/mysql                                        ###I'VE MIGRATED TO MYSQL SO THIS HOW TO VOLUME DB
    environment:
      - MYSQL_ROOT_PASSWORD=userer
      - MYSQL_PASSWORD=userer
      - MYSQL_DATABASE=dbfile
      - MYSQL_USER=userer
    ports:
      - "3306:3306"
```
Run with `docker-compose up --build`

Now this branch __cleanup__ is over, and i'm not about to use it anymore. It's just a **checkpoint.**
After ending editing this file I'll change last commit and repush it.

# See Ya!
