# FastAPI SageMaker Endpoint Template

FYI: [機械学習の推論用REST APIサーバーをAmazon SageMakerで構築するまでに考えたこと](https://techblog.raksul.com/entry/2023/08/17/122804)

This is a template for deploying a FastAPI endpoint on AWS SageMaker. 

This is mainly based on [Seamless Integration: Deploying FastAPI ML Inference Code with SageMaker BYOC + Nginx](https://medium.com/@imrannaz326/seamless-integration-deploying-fastapi-ml-inference-code-with-sagemaker-byoc-nginx-6802103f7a2c).

### Why use Nginx

Nginx serves as a high-performance reverse proxy, forwarding client requests to the appropriate backend server, such as FastAPI, enabling load balancing and distribution. 

This setup enhances the ability to handle a large number of simultaneous connections efficiently. 

Utilizing an asynchronous event-driven architecture, Nginx can process more requests quickly compared to FastAPI alone. 

This leads to an overall improvement in performance and responsiveness.

### Why use Gunicorn
By combining Gunicorn and Uvicorn, applications can be parallelized, leveraging multi-core CPUs to handle more requests. 

Gunicorn, a WSGI application server, isn't directly compatible with FastAPI. 

However, it functions as a process manager using Uvicorn's Gunicorn-compatible worker class. 

Gunicorn listens on specified ports and IPs, forwarding communications to Uvicorn worker processes.

FYI: [Server Workers - Gunicorn with Uvicorn](https://fastapi.tiangolo.com/deployment/server-workers/)

## Prerequisites

- Tool to run Docker like Docker Desktop
  - I highly recommend to use [OrbStack](https://github.com/orbstack/orbstack)

## Apply template to your project
```
git clone https://github.com/tamtam-fitness/python-template-based-on-docker.git <new-project>

cd <new-project>

rm -rf .git
```

## Setup Model

This template uses [the model for word2vec](https://drive.google.com/file/d/0ByFQ96A4DgSPUm9wVWRLdm5qbmc/view?resourcekey=0-of5Ks1fuoKNh1pEYE8uSFQ) created by [Hironsan](https://github.com/Hironsan).

You can download and unzip the model from the above link ,then put it in the following directory.


```
mkdir -p opt/ml/model/

mv ~/Downloads/vector_neologd.zip opt/ml/model/

unzip opt/ml/model/vector_neologd.zip -d opt/ml/model/
```

The model file(`opt/ml/model/model.vec`) is supposed to be located in the directory.

## Run Container

To start development, you are supposed to run the following command:
```bash 
make setup   
```

## Development Commands

### Enter into container
```bash
make enter_container
```

### Lint

```bash 
make lint
```
### Format

```bash 
make format
```

### Test

If you want to run all tests, you can run the following command:
```bash 
make test
```

If you want to run the specific test, you can run the following command:
```bash
make enter_container

poetry shell

poe test tests/{file or directory you want to test}
```


## Testing Locally
After serving the endpoint locally by `make setup`, you can run a couple tests.

- For viewing the swagger api, enter http://0.0.0.0:8080/docs into your search bar.

- For testing the /ping endpoint, enter curl http://0.0.0.0:8080/ping into the console.

- For testing the /invocations endpoint, enter curl http://0.0.0.0:8080/invocations into the console.
  ```bash
  # Here is an example for testing the /invocations
  curl -X 'POST' \
    'http://localhost:8080/invocations' \
    -H 'accept: application/json' \
    -H 'Content-Type: application/json' \
    -d '{"word": "Python"}'
  ```

## Testing Production Image Locally

※ You are supposed to [setup model](#setup-model) in advance .

```
sh serve_local.sh
```


## Deploying to AWS SageMaker

If you want to deploy a model file to AWS SageMaker, you need to compress the model as tar.gz and upload it to S3.

```
opt/ml/model/model.tar.gz
```

Plus, you need to add ENV variables when Model creation.

```bash
# you have to set prod.yml in opt/program/common/yaml_configs if you want to deploy it as a WebAPI
ENV=prod 
```

Besides, if you want to publish it as a WebAPI, you may want to read [Creating a machine learning-powered REST API with Amazon API Gateway mapping templates and Amazon SageMaker](https://aws.amazon.com/blogs/machine-learning/creating-a-machine-learning-powered-rest-api-with-amazon-api-gateway-mapping-templates-and-amazon-sagemaker/).

## References
- [Use Your Own Inference Code with Hosting Services](https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms-inference-code.html)
- [amazon-sagemaker-examples/advanced_functionality/scikit_bring_your_own
/container/](https://github.com/aws/amazon-sagemaker-examples/tree/main/advanced_functionality/scikit_bring_your_own/container)
- [Seamless Integration: Deploying FastAPI ML Inference Code with SageMaker BYOC + Nginx](https://medium.com/@imrannaz326/seamless-integration-deploying-fastapi-ml-inference-code-with-sagemaker-byoc-nginx-6802103f7a2c)
- [Deploying custom models on AWS Sagemaker using FastAPI](https://sii.pl/blog/en/deploying-custom-models-on-aws-sagemaker-using-fastapi/?category=hard-development&tag=aws-sagemaker,fastapi,docker-2)
