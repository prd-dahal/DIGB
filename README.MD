### Run Backend Project
Install the following prerequisities:
- Docker: [Install Docker](https://docs.docker.com/get-docker/) (**version 24.0.6**)
- Docker Compose: [Install Docker Compose](https://docs.docker.com/compose/install/) (**verson 1.29.2**) 

*PS: Docker Compose V2 might not work properly*

#### Steps to run the project

1. Clone the repository:
   ```bash
   git clone https://github.com/prd-dahal/DIGB.git
 2. Go to digb_backend
    ``` bash 
    cd digb_backend
3. Run docker compose 
    ```
    sudo docker-compose -f production.yml up -d --build --force-recreate
4. The project will be hosted in http://localhost:1257
5. Admin login url
    ```
    http://localhost:1257/digb_admin
6. Default login credentials
    ```
    Username : ordermanagement
    Password : @ordermanagement321
    
    
### Run Front-End Project

Install following prerequisities. 

- Node: [Install Node](https://nodejs.org/en) (**version >= 18.17.0**)

*PS: Recommended version is **18.17.0***

#### Steps to run the project
1. Clone the repository:
   ```bash
   git clone https://github.com/prd-dahal/DIGB.git
 2. Go to digb_fe
    ``` bash 
    cd digb_fe
3. Install yarn (**version 1.22.19**)
    ```
    npm install --global yarn 
4. Install all the dependencies 
    ```
    yarn
5. Run the project 
    ``` 
    yarn dev
6. The project will be hosted in http://localhost:3000
