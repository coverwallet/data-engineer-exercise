# Data Engineer Applicant Exercise
To be considered for a Data Engineer position at coverwallet, you must
successfully complete these steps.

1. Fork this Repository
2. In the simple_challenge directory, using the programming language/tool of your
preference, create a script that collects the `consolidated_weather` from the
3 different cities/regions of your election from [here](https://www.metaweather.com/api/)
and saves it to a local file.
3. In the simple_challenge directory, using the programming language/tool of your
preference, create a second script that uploads previous CSV files to either a MongoDB
or a PostgreSQL.
  * You can use [mLab](https://mlab.com/plans/pricing/#plan-type=sandbox) to start
  a free MongoDB as a Service.
  * If you prefer a PostgreSQL database, you can use [ElephantSQL](https://www.elephantsql.com/plans.html)
  to start a free PostgreSQL server.
4. [OPTIONAL] In the same directory, create a text file called `query.txt` with the
query code to get a report of how accurate is `wind_speed` prediction with time.
  * Taking day X as a reference, which is the deviation from `wind_speed(X)` compared
 with previous predictions of the same day X.
5. [OPTIONAL] Following the Serverless approach, put this pipeline to automatically
run on a daily basis.
  * You can use Heroku, AWS Free Tier or Google Cloud.
6. Commit and Push your code to your fork.
6. Send a pull request to our repository, we will review your exercise and get
back to you. If your GitHub profile does not include your name, please include
your name in the pull request.
