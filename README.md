# Data Engineer Applicant Exercise
To be considered for a Data Engineer position at **CoverWallet**, you must
successfully complete these steps.

## What is the exercise about?

1. First of all, fork this repository to your GitHub account and clone your own repo to your laptop.
  * If you are not familiar with GitHub, please check this
  [how to fork a repo](https://help.github.com/articles/fork-a-repo/) link.  
2. To initialize the workspace, please create a folder named `working_folder`
or execute the following command. **IMPORTANT: All exercise deliverables should
be in this folder before submitting the application.**
```
make init
```
3. Once in your **initilized** repository, in the `working_folder` directory and using **Python** as
programming language, create a script that collects the
`weather data` from the 3 different cities/regions of your election from
 [this](https://www.visualcrossing.com/) public API. Please, create a free account in order to use the service. 
   You can find the available endpoints [here](https://www.visualcrossing.com/resources/documentation/weather-api/weather-api-documentation/#timeline), collect the data and save it to a local file.
Feel free you select the endpoint you think is better to guarantee that the job is deterministic and runs on a time basis.
4. Again in your repository, in the `working_folder` directory, create a second script that uploads
previous CSV files to either a MongoDB or a PostgreSQL database.
  * You can use [mLab](https://mlab.com/plans/pricing/#plan-type=sandbox) to start
  a free MongoDB as a Service.
  * If you prefer a PostgreSQL database, you can use [ElephantSQL](https://www.elephantsql.com/plans.html)
  to start a free PostgreSQL server.
  * If you do not want to use any of this cloud provider you can start a Docker Container in your local host
  and insert the data there.
5. Once you load the data into the DB you choose, create a directory inside the working folder and name it `app`.
Inside the folder build an API to consume the data you just load into the db. Choose the framework, 
or programming language you want, there is no restriction. The API should have a persistence in a db.
6. In the `working_folder` create a directory call `querys`. You will find a csv file called `weather_forecasts_history.csv` with the following fields:
    * `City`: name of the city
    * `Created`: date when the forecast on the Applicable Date is made
    * `Applicable Date`: date when the forecast takes place
    * `Wind Speed`: measure of the speed of the wind
    * `Temperature`: measure of the temperature  
            
   Load this data into your db and create a file called `query.txt` in the `querys` directory with the query code to get a report of:
  * How accurate is `wind_speed` prediction with time.
  * Taking day X as a reference, which is the deviation from `wind_speed(X)` compared with previous predictions of the same day X.
7. [OPTIONAL] Following the Serverless approach, put this pipeline to automatically
run on a daily basis.
  * You can use Heroku, AWS Free Tier or Google Cloud.
  * You can use the Serverless Framework and just make the yaml config for the deploy.
  * You can create a Dockerfile with the environment and just write in a txt how you will set up a cron job.
  * Add another document in the `working_folder` explaining how you did it and
  some evidences.
8. [OPTIONAL] Try to explain how would you ingest data from the api using an event processing platform. You can choose the 
   event platform you want Kafka, RabbitMQ, Celery... etc. There is not need to create the full architecture code, but
   otherwise create a file called streaming_events.txt explaining us how will you build this architecture.
9. [OPTIONAL] Create the environment to deploy your API in to a production environment.
  * You can use a Docker Compose with the App.
  * You can follow a Serverless Approach and use the Serverless Framework.
  * You can use other architecture to deploy.
