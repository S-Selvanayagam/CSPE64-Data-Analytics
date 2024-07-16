My progress 


Week 1

Monday and Tuesday - Orientation 
Wednesday - develop you courses
Thursday - develop you courses + project meet + started reading springboot 
Friday - Learnt about TLC project, raised Iam requests, ms server SQL connection 

Week 2

Monday -
Introduction to chaos engineering project, setup tlc project db and api calls 

Tuesday-
Intro to PCC project + learnt what's chaos engineering - assaults+ watchers, chaos monkey 

Wednesday-
Learnt and execution of resiliency patterns - using resiliency4j
Started to develop scenarios 

Thursday-
Developed scenarios based on high level architecture 
Set up 2 projects - resiliency4j and another spring gradle repo for familiarity

Friday-
Got pagewise PCC update, hence defined scenarios with page wise dependency on services, raised IAM for PCC repos and applications for local setup of PCC.

3rd week

Monday -
Started local setup of PCC using script.
Cloned all repos but running had gradle building issues, debugging it.

Tuesday -
Was able to get the PCC local setup working 
Fixed npm config issues and gradle building issues
Started to configure chaosmonkey in a service 

Wednesday-
Developed some scenarios for the service
Chaosmonkey config had too many issues, 
Fixed jre issue, got maven repo to get the access thru artifactory for the setup, fixed varying jdk issues.

Thursday 
Finally configured chaos monkey in the project.
Prepared a postman collection for all routes in the service and the chaos assaults routes.

Friday- 
Started performing assaults using Chaos Monkey and started to note observations.
Performed latency test on routes under QueryEvents.

4th Week.

Monday

Started out with scenarios in QueryEvents service wise.
Implemented running tests method wise using custom watchers.
Tested out Redis, Mongo, Hume and Epods services and in controller layer.

Tuesday
Integrate Chaos Monkey into all the repositories - 5 (queryEvents, queryTransanctions, Authenticate, App content, Data export.)
Started with finding payloads for all routes inside queryTransanctions.

Wednesday 
Started with exception assaults, triggered runtime exception in different services within queryEvents.
Implemented exception assualts method wise 
Finished with all payloads of queryTransanctions and Data export microservices.

Thursday 
Done with all payloads for all routes and created collections to perform assaults.
Done with documenting all observations for latency and exception tests for QueryEvents.

Friday
Created a branch called chaos-develop in all the the 5 repos.
Pushed changes of chaos monkey setup.
Created observations on queryTransanctions and half-way completed with the assault executions.

5th Week:

Monday 
Completed Latency and Exception assaults on queryTransanctions.
Documented the observations and made some changes as suggested by PCC Team.
Started with Data export microservices, with services and scenarios.

Tuesday 
Completed the assaults on Data export microservices and documented the observations.
Started with Authenticate microservices.
Asked to prepare presentation of demo for progress

Wednesday 
Created presentation with assaults  demo and displayed to Manager and Principal engineer.
Completed with Assault and observations in Authenticate microservices.
Started reading about TestNG implementation.

Thursday 
Implemented 
