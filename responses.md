
### (1). The readme doesn’t include instructions for running the web server itself. Do you have a way to run it on a single machine (not Heroku?)

Yes, definitely. Django is really easy with local testing.   
I updated the ReadMe for the step of establishing a local host

### (2). Your zip file included Python libraries. Can you clean up the code to not have the binaries included?


Thanks for pointing this out! Initially, i added them to .gitignore and was hoping you guys can directly clone them from Github. unfortunately, sendgrid suspend my account.   
__The updated zipfile should be clean__

### (3) We don’t see some of the management commands such as get_weather_data. Are some files missing?

It's located in the *_init_.py* for the commands module. The principle engineer of my previous team has a philosophy that we should localize the function as low-level as possible, i kind of followed his design philosophy  
However, after giving it a bit more thought, i think they should be decoupled from the commands module and relocated to the ```utils.py```. Although right now they only used for the django commands method, one can imagine it is useful
for the future API (such as API to retrieve weather data to display on a dashboard)

__I updated this in the zip as well__

### (4) Love the idea of the ‘demo’ mode but some of the code is duplicated there. How would you clean that up?

That's a really good point. Thanks for the advice
i added that the last minute for testing, it totally needs to be refactored. I updated the code
Here is the approach

  *  leave the sg_send_email as base-level abstraction to interact with API for sending email via sendgrid
  *  write newsletter_builder as one level abstraction to build parameter dictionary (via invoking various helper method) for sg_send_grid needed for sending user newsletter (admin and average user)
  *  write send_user_newsletter as one more level abstraction to control the invoking of (b) and (a) and handle exceptions


Inspired by your suggestion, i have also written one abstraction for sending user sign-up welcome email. It is clearer to write a separate function because the logic is much simpler than building a newsletter


### (5) What is the purpose of your sub_tuples and personalizations?

The html/css for emailing template, though i wrote them myself, is stored in send-grid.
Send-grid then allow you to specify a dictionary or map to substitute one string in the template for dynamic data via API
For example, in the template html
there is ```_temperature_``` I then can specify
```
{"_temperature_": CURRENT_TEMPERATURE}
```
it will substitute ```_temperature_``` with the value i specified.
### (6) How would you scale the app or personalization to send to perhaps 1m+ recipients daily?
Excellent question, i kind of touched that in the readme

Since the model is
1. run analysis for each user and generate customized newsletter (can takes long time)
2. send out email
It fits perfectly to a distributed task processing system

We can

1. (use multiple workers) produce the task of analyze and sending email to a queue
2. use multiple workers to consume the task in the queue

_one machine can host multiple workers/processes_

High-Level
_____
```
P - Producer
C - Consumer

  p                                                         C
---->                                                      --->
  p                                                         C
---->  (Exchange) -> RABBITMQ/SQS/Redis(whatever broker)   --->
  .                                                         .
  .                                                         .
  .                                                         .
```
_More proccesses does not mean better performance, that's where auto-scaling, load-balancing comes in_

Implementation
________________
One implementation for Django/python is to use
* Celery -- task queue package for python
* RabbitMQ -- as the broker service
* Flower -- for monitoring

So we
1.  host rabbitMQ on a EC2
2.  Use celery to define a task for the newsletter queue
    * define how it should be consumed (analyze + email)
    *  do this via override the run_inner method. something like this

    ```python
    class QueuedNewesLetterGenerator_Sender(Task):
    def run(self, some_requried_parameter):
        @some_decarator_to_prevent_deadlock
        @some_decarator_to_restrict_access_to_database_write_permission
        def run_inner():
            result = analyze(subscriber)
            send_mail(result)
        return run_inner()

    ```
3. multiple workers to produce to the queue, create task, we can enforce uniqueness of the task by maintain a ID table
    ```python
    QueuedNewesLetterSender.applyAsync(....)

    ```
4. multiple workers to consume the queue, extract info and generate html for email then call the send-grid to send it. Requeue it when fail
Notes: One needs to handle dead-lock when use multiple

5. Now what if we want to implement our own email server?
    ```
    Have two queues
    a. one for processing/generating html
    b. one for sending the generated html to subscriber
    each queue have its own producers and consumers hookedup
    ```


6. *Extra*  
  Similar approach can be implemented for the sign-up emailing process

### (7) How did you end up solving the SendGrid issue?
I simply signed up a new API key and recreated the template (i kept a local copy)   
One can simply use from django.core.mail import send_mail to do the same thing.   
That's how we built our emailing tool for SurveyMini. I just wanted to try something new
