# Berry Locator

## Setup and Installation
1. Set environment variables or create `.env` file in project root. 
In case of postgres container only variables starting with `POSTGRES_` are required.
   ```dotenv
   DEBUG=True
   SECRET_KEY=abc123
   EMAIL_HOST=mailhog
   EMAIL_PORT=1025
   
   POSTGRES_HOST=postgres
   POSTGRES_PORT=5432
   POSTGRES_DB=berry_locator
   POSTGRES_USER=postgres
   POSTGRES_PASSWORD=postgres
    ```
2. Build and start app:
   - with `make`:
      ```
      make build
      make up
      ```
   - without `make`:
      ```
      docker-compose build
      docker-compose up
      ```
Django: [http://127.0.0.1:8000](http://127.0.0.1:8000)   
MailHog: [http://127.0.0.1:8025](http://127.0.0.1:8025)
