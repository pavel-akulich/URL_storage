# API application for storing user links

[Russian](../README.md) | **English**

## Description of the project
User link storage application is a backend part of an application created in Python programming language using Django REST framework.
The application allows users to save their links, as well as view, edit and delete them. When saving a link, the user passes only the link, all other
information about it is filled in automatically. Users can also create collections for their links and segregate them as they see fit.  

## Components of the project

The project consists of the following components:

1. **Users:**
    - User can register (email, password)   
    - User can change password   
    - User can reset password   
    - User can authenticate   
    - User can manage their links
    - User can manage their collections

2. **Links:**
   - Contains the page title (links)
   - Contains a short description of the page
   - Contains a link to the page
   - Contains a preview of the page
   - Contains the type of link (website, book, article, music, video)
   - Contains date and time of creation
   - Contains date and time of last update

3. **Collections:**
   - Contains the name of the collection
   - Contains a description of the collection
   - Contains links belonging to the collection
   - Contains the date and time of creation
   - Contains the date and time of the last update
   
## Technology
   - The project is developed in `Python` programming language using `Django REST framework`
   - A third-party library `psycopg2-binary` is used to work with `PostgreSQL` database
   - Swagger documentation is connected in the project using `drf-yasg` library
   - The `pillow` library is used to work with images
   - The `beautifulsoup4` and `requests` libraries are used to get information about the page
   - The `poetry` tool is used to control the virtual environment
   - The `python-dotenv` library is used to interact with environment variables
   - Containerization technology is used for easier and simpler project deployment using `Docker`

## Start a project using Docker
   - Clone the repository https://github.com/pavel-akulich/URL_storage
   - In the root directory of the project, create a `.env` file and copy the contents of the `.env.sample` file into it, specifying the necessary values (database, email server).
   - Use the `docker compose up --build` command to build and start all services
   - The database will be created automatically, after which the migrations will be applied and the database will be populated with test data from `testdata_for_db.json`.
   - After successful completion of the previous step, the application will be available at http://localhost:8000/

## API documentation
After successful launch of the server, Swagger documentation will be available at the following addresses: http://localhost:8000/ or http://localhost:8000/docs/

## Notes
   - The project can be modified and extended for wider use
   - Email server is used in the project to implement resetting of user password
   - Environment variables required for the project can be viewed in `.env.sample` file
   - All necessary dependencies are located in `pyproject.toml` and `poetry.lock` files
