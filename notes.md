What is an API?
- API are mechanism that enable two software components-such as the frontend and backend of an application - to communicate with each other using a defined set of rules , protocols , and data formats.It is nothing but a connector.

Why API?
- If i have only one applcation but i want to make for android , ihpone , web then all these application uses different language or different architechture so , if we use API then API -> backend -> database is enough for all the application . If we want a frontend then frontend will interact with API and then from that API it interact with backend and database rather then using application independently.

ML Perspective of API.
- In the case of software the common is database but in the case of ML the common is ML/DL model. Same nai ho but instead of database there is model where backend interact with model and api interact with API and services is given by API.

FastAPI - modern . high-performace web framework for buidling APIs with Python using two lirabary - Starlette (manages how your API reviceve req and send response) and Pydantic(it is data validation libarary airako kura chai correct format ma xa ki nai herxa elle).

How it woks?
- API for machine learning model xa re ani /predict bhanera endpoint xa re hami sangaa then , API code and Webserver hunxa hami sanga. Webserver ma basically there is HTTP request listen kei bhako xa ki xaina herne anid API code bhaneko the API code bhaihalyo. Browser le first ma HTTP request set garxa POST eta uti haru then it is send to Webserver and generate the prediction value and the request is HTTP but our API code is in python and python dont understand HTTP so the client sent http request then it is send to SGI and it convert it into python understandable code and send it to API. ani response garne bela ni SGI auxa python output lai http ma convert garxa and then send it to webserver. SGI (server gateway interface) is the bridge between python and http. Webserver ma request auxa ani tyo SGI ma janxa ja python understandable code ma janxa ani API ma janxa ani tya bata predict call hunxa.

Why fastAPI is fast to code ?
- Automatic input validation 
- Auto-generated Interactive Documentation
- Seamless integration with Modern Ecosystem (ML/DL library , OAuth , JWT , SQL Alchemy , Docker , Kubernetes ,etc).



