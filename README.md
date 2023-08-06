# FastAPI SageMaker Endpoint Template

This is a template for deploying a FastAPI endpoint on AWS SageMaker. 

This is mainly based on [Seamless Integration: Deploying FastAPI ML Inference Code with SageMaker BYOC + Nginx](https://medium.com/@imrannaz326/seamless-integration-deploying-fastapi-ml-inference-code-with-sagemaker-byoc-nginx-6802103f7a2c).

This template uses [the model for word2vec](https://drive.google.com/file/d/0ByFQ96A4DgSPUm9wVWRLdm5qbmc/view?resourcekey=0-of5Ks1fuoKNh1pEYE8uSFQ) created by [Hironsan](https://github.com/Hironsan).

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

FYI: [Server Workers - Gunicorn with Uvicorn](Server Workers - Gunicorn with Uvicorn)

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

```
tar -xzvf opt/ml/model/model.tar.gz
```


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

For viewing the swagger api, enter http://0.0.0.0:8080/docs into your search bar.

For testing the /ping endpoint, enter curl http://0.0.0.0:8080/ping into the console.

For testing the /invocations endpoint, enter curl http://0.0.0.0:8080/invocations into the console.

## References
- 
- [Use Your Own Inference Code with Hosting Services](https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms-inference-code.html)
- [amazon-sagemaker-examples/advanced_functionality/scikit_bring_your_own
/container/](https://github.com/aws/amazon-sagemaker-examples/tree/main/advanced_functionality/scikit_bring_your_own/container)
- [Seamless Integration: Deploying FastAPI ML Inference Code with SageMaker BYOC + Nginx](https://medium.com/@imrannaz326/seamless-integration-deploying-fastapi-ml-inference-code-with-sagemaker-byoc-nginx-6802103f7a2c)
- [Deploying custom models on AWS Sagemaker using FastAPI](https://sii.pl/blog/en/deploying-custom-models-on-aws-sagemaker-using-fastapi/?category=hard-development&tag=aws-sagemaker,fastapi,docker-2)