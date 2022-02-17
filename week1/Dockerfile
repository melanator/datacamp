services:
  postgres:
    image: postgres:13
    environment:
      POSTGRES_USER: airflow
      POSTGRES_PASSWORD: airflow
      POSTGRES_DB: airflow
    volumes:
      - postgres-db-volume:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD", "pg_isready", "-U", "airflow"]
      interval: 5s
      retries: 5
    restart: always

sudo docker run -it \
-e POSTGRES_USER="root" \
-e POSTGRES_PASSWORD="root" \
-e POSTGRES_DB="ny_taxi" \
-v "/mnt/d/dev/data_eng/data_zoomcamp/week1/ny_taxi_postgres_data":/var/lib/postgresql/data \
-p 5431:5432 \
postgres:13

sudo docker run -it \
-e POSTGRES_USER="root" \
-e POSTGRES_PASSWORD="root" \
-e POSTGRES_DB="ny_taxi" \
-v d:/dev/data_eng/data_zoomcamp/week1/ny_taxi_postgres_data:/var/lib/postgresql/data \
-p 5432:5432 \
postgres:13

sudo docker run -it \
-e POSTGRES_USER="root" \
-e POSTGRES_PASSWORD="root" \
-e POSTGRES_DB="ny_taxi" \
-v /home/anton/datacamp/week1/ny_taxi_postgres_data:/var/lib/postgresql/data \
-p 5431:5432 \
--network=pg-network \
--name pg-database \
postgres:13

sudo docker run -it \
-e POSTGRES_USER="root" \
-e POSTGRES_PASSWORD="root" \
-e POSTGRES_DB="livetracker" \
-v /home/anton/livetracker/db/:/var/lib/postgresql/data \
-p 5432:5432 \
--network=pg-network \
--name pg-database \
postgres:13

sudo docker run -it \
-e POSTGRES_USER="root" \
-e POSTGRES_PASSWORD="root" \
-e POSTGRES_DB="ny_taxi" \
-p 5431:5432 \
postgres:13

https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page

docker run -it -e PGADMIN_DEFAULT_EMAIL="admin@admin.com" -e PGADMIN_DEFAULT_PASSWORD="root" -p 8080:80 --network=pg-network --name pg-admin dpage/pgadmin4