# Data Engineer Applicant Exercise
To be considered for a Data Engineer position at **CoverWallet**, you must
successfully complete these steps.

## What is the exercise about?

1. First of all, clone this repository to your local computer. If you are not familiar with GitHub, please check this
  [how to clone a repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) link.
2. Please, create a folder named `working_folder` and using **Python** as
programming language, create a script that collects the
`weather data` from the 3 different cities/regions of your election from
 [this](https://www.visualcrossing.com/) public API. Please, create a free account in order to use the service. 
   You can find the available endpoints [here](https://www.visualcrossing.com/resources/documentation/weather-api/weather-api-documentation/#timeline), collect the data and save it to a local file.
Feel free you select the endpoint you think is better to guarantee that the job is deterministic and runs on a time basis.
3. Again in your repository, in the `working_folder` directory, create a second script that uploads
previous CSV files to either a MongoDB or a PostgreSQL database.
  * You can use [mLab](https://mlab.com/plans/pricing/#plan-type=sandbox) to start
  a free MongoDB as a Service.
  * If you prefer a PostgreSQL database, you can use [ElephantSQL](https://www.elephantsql.com/plans.html)
  to start a free PostgreSQL server.
  * If you do not want to use any of this cloud provider you can start a Docker Container in your local host
  and insert the data there.
4. Once you load the data into the DB you choose, create a directory inside the working folder and name it `app`.
Inside the folder build an API to consume the data you just load into the db. Choose the framework, 
or programming language you want, there is no restriction. The API should have a persistence in a db.
5. In the `working_folder` create a directory call `queries`. You will find a csv file called `weather_forecasts_history.csv` with the following fields:
    * `City`: name of the city
    * `Created`: date when the forecast for the Applicable Date is made
    * `Applicable Date`: date the forecast applies to
    * `Wind Speed`: measure of the speed of the wind
    * `Temperature`: measure of the temperature  
            
   Load this data into your db and create a file called `queries.txt` in the `queries` directory with the SQL query code to get a report of:
  * How accurate is `wind_speed` prediction with time.
  * Taking day X as a reference, which is the deviation from `wind_speed(X)` compared with previous predictions of the same day X.
6. [OPTIONAL] Following the Serverless approach, put this pipeline to automatically
run on a daily basis.
  * You can use Heroku, AWS Free Tier or Google Cloud.
  * You can use the Serverless Framework and just make the yaml config for the deploy.
  * You can create a Dockerfile with the environment and just write in a txt how you will set up a cron job.
  * Add another document in the `working_folder` explaining how you did it and
  some evidences.
7. [OPTIONAL] Try to explain how would you ingest data from the api using an event processing platform. You can choose the 
   event platform you want Kafka, RabbitMQ, Celery... etc. There is not need to create the full architecture code, but
   otherwise create a file called streaming_events.txt explaining us how will you build this architecture.
8. [OPTIONAL] Create the deployment of your API.
  * You can use a Docker Compose with the App.
  * You can follow a Serverless Approach and use the Serverless Framework.
  * You can use other architecture to deploy.
