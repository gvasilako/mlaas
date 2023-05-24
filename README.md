# mlaas

Machine Learning as a Service dummy project. 

1. The Backend service (WebApi) is a Flask RestApi. It contains pretained models for the classification task of the [iris dataset](https://en.wikipedia.org/wiki/Iris_flower_data_set).
2. The Backend service (WebApi) exposes the endpoint http://localhost:port/prediction where a user can make a post request with the following parameters: 
<p style="text-align: center;">{'sl':'<Sepal Length>' , 'sw':'<Sepal Width>' , 'pl':'<Petal Length>', 'pw':'<Petal Width>'}</p>
3. The FrontEnd service is an Angular application where the user can provide the above parameters to a user interface. Then the WebApi is being called which return the flower prediction.  
  
Both services can also be containerized according to the provided Dockerfiles.
