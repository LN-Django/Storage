# Storage
Storage service to store storage-related information. 

## Running the App Locally
To run the dev server please run the following command.
```
 python ./boilerplate/manage.py runserver
```

## Docker config
### What is Docker?
> Docker is a "container" to package applications into standardized units for development and deployment ([Source](https://www.docker.com/resources/what-container))

### Prerequisites
- Docker is installed and accessible via terminal
- Docker is running (try running `docker ps` to see if Docker is running on your machine)

How to use Docker to serve the application locally

Build the docker image
```
docker build -t web:latest .
```

Run the container with the name of `boilerplate` using the image built on the last step
```
docker run -d --name boilerplate -e "PORT=8765" -e "DEBUG=1" -p 8000:8765 web:latest
```

Check on `http://localhost:8000` to see if the app is running.

Stop the docker container
```
docker stop boilerplate
```

Remove the container
```
docker rm boilerplate
```

## Docker Config with Heroku
### What is Heroku?
Heroku is a cloud platform (PaaS) to build and deploy the application ([Heroku documentation site](https://devcenter.heroku.com/categories/reference)). 

Building the image
```
docker build -t registry.heroku.com/peaceful-wave-28166/web .
```

Push the Docker container
```
docker push registry.heroku.com/peaceful-wave-28166/web 
```

Release the image
```
heroku container:release -a peaceful-wave-28166 web
```

## Demo

**Staging**: https://peaceful-wave-28166.herokuapp.com/api/v1/swagger

~~**Production**: https://enigmatic-dusk-38395.herokuapp.com/api/v1/swagger~~
**Note: We discontinued the production environment**

## CI/CD Pipeline
For this project, CI/CD is also implemented using [Github Actions](https://github.com/features/actions). Please take a look into the diagram below to see more about the CI/CD pipeline.
![CI/CD Diagram](https://github.com/LN-Django/boilerplate/blob/main/docs/CI_CD_KBE.drawio.png?raw=true)
