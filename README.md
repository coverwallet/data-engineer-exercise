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
3. Once in your **initilized** repository, in the `working_folder` directory and using the
programming language/tool of your preference, create a script that collects the
`consolidated_weather` from the 3 different cities/regions of your election from
 [this](https://www.metaweather.com/api/) public API, and save it to a local file.
3. Again in your repository, in the `working_folder` directory and using the
programming language/tool of your preference, create a second script that uploads
previous CSV files to either a MongoDB or a PostgreSQL database.
  * You can use [mLab](https://mlab.com/plans/pricing/#plan-type=sandbox) to start
  a free MongoDB as a Service.
  * If you prefer a PostgreSQL database, you can use [ElephantSQL](https://www.elephantsql.com/plans.html)
  to start a free PostgreSQL server.
  * If you do not want to use any of this cloud provider you can start a Docker Container in your local host
  and insert the data there.
4. Once you load the data into the DB you choose, create a directory inside the working folder and name it `app`.
Inside the folder build an API to consume the data you just load into the db. Choose the framework, 
or programming language you want there is no restriction. The API should have a persistence in a db.
5. [OPTIONAL] In the `working_folder` create a directory call `querys` and create a text file called `query.txt` with the
query code to get a report of how accurate is `wind_speed` prediction with time.
  * Taking day X as a reference, which is the deviation from `wind_speed(X)` compared
 with previous predictions of the same day X.
6. [OPTIONAL] Following the Serverless approach, put this pipeline to automatically
run on a daily basis.
  * You can use Heroku, AWS Free Tier or Google Cloud.
  * You can use the Serverless Framework and just make the yaml config for the deploy.
  * You can create a Dockerfile with the enviroment and just write in a txt how you will set up a cron job.
  * Add another document in the `working_folder` explaining how you did it and
  some evidences.
7. [OPTIONAL] Try yo load the CSV files donwload from the api using an event processing platform. You can choose the 
   event platform you want Kafka, RabbitMQ, Celery... etc. There is not need to create the full architecture code, but
   otherwise create a file called streaming_events.txt explaining us how will you build this architecture.
8. [OPTIONAL] Create the enviroment to deploy your API in to a production enviroment.
  * You can use a Docker Compose with the App.
  * You can follow a Serverless Approach and use the Serverless Framework.
  * You can use other architecture to deploy.

## How to submit your exercise?
The submitting process consist on _encrypting your files with our public
[GPG](https://gnupg.org/) key_ and creating a Pull Request towards our repo.
In order to do it, please follow the following steps:

1. In order to import and use our public key, you need to install GPG.
   * Linux: `sudo apt-get install gnupg2`
   * Mac: `brew install GPG`
2. To import our public key to your key ring, use the following command (Linux/Mac)
from the repository folder For other OS, please refer to the [documentation](https://www.gnupg.org/documentation/).
 ```
 make import
 ```
3. To encrypt your files and prepare the encrypted deliverable use the following
command. It will create a new GPG file in `publish_folder` with the content of
`working_folder` directory.
```
 make encrypt
```
4. Commit and Push your code to your fork.
5. Send a pull request to our repository, we will review your exercise and get
back to you. If your GitHub profile does not include your name, please include
your name in the pull request.

** If you find any issues during the exercise, please send an email to [jobs@coverwallet.com](mailto:jobs@coverwallet.com)
