# Project URLs

## Backend
**URL**: [Backend URL](https://digb_be.dahalpradeep.com.np/digb_admin/)  
**Username**: ordermanagement  
**Password**: @ordermanagement321

## Frontend
**URL**: [Frontend URL](https://digb_fe.dahalpradeep.com.np/)

## Run Backend Project

### Prerequisites
- Docker: [Install Docker](https://docs.docker.com/get-docker/) (**version 24.0.6**)
- Docker Compose: [Install Docker Compose](https://docs.docker.com/compose/install/) (**version 1.29.2**)

*Note: Docker Compose V2 might not work properly.*

### Steps to Run the Backend Project

1. Clone the repository:
    ```bash
    git clone https://github.com/prd-dahal/DIGB.git
    ```

2. Navigate to `digb_backend`:
    ```bash
    cd digb_backend
    ```

3. Run Docker Compose:
    ```bash
    sudo docker-compose -f production.yml up -d --build --force-recreate
    ```

4. The project will be hosted at [http://localhost:1257](http://localhost:1257).

5. Admin login URL:
    [http://localhost:1257/digb_admin](http://localhost:1257/digb_admin)

6. Default login credentials:
    - **Username**: ordermanagement
    - **Password**: @ordermanagement321

## Run Frontend Project

### Prerequisites
- Node: [Install Node](https://nodejs.org/en) (**version >= 18.17.0**)

*Note: Recommended version is **18.17.0**.*

### Steps to Run the Frontend Project

1. Clone the repository:
    ```bash
    git clone https://github.com/prd-dahal/DIGB.git
    ```

2. Navigate to `digb_fe`:
    ```bash
    cd digb_fe
    ```

3. Install Yarn (**version 1.22.19**):
    ```bash
    npm install --global yarn
    ```

4. Install all dependencies:
    ```bash
    yarn
    ```

5. Run the project:
    ```bash
    yarn dev
    ```

6. The project will be hosted at [http://localhost:3000](http://localhost:3000).

