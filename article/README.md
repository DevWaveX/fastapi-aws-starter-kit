---
title: ⚡ Serverless REST API on AWS with FastAPI ⚡
tags:
  - Python
  - AWS
  - Serverless
  - FastAPI
canonicalUrl: >-
  https://medium.com/aws-tip/serverless-rest-api-on-aws-with-fastapi-bd9de11f925a
coverImage: https://github.com/DevWaveX/fastapi-aws-starter-kit/raw/main/article/cover.png
publications:
  - id: 1655339
    url: https://dev.to/coxhawk/serverless-rest-api-on-aws-with-fastapi-1e6a
    platform: devTo
    published: true
  - id: 6544258d544bd9c69327cdff
    url: TBD
    platform: hashnode
    publicationId: 62019a434efba97010a97bb9
---


# ⚡ Serverless REST API on AWS with FastAPI ⚡

Hi there! 👊

In this article, I will explain you how to deploy, in minutes, **FastAPI** on **AWS** using **Serverless**.

As usual in all my articles, you will find at the end a link to a working example on my Github.

## Pre-requisites

I assume you have at least **Python 3.7+** and **npm** installed.

### Install and configure AWS CLI

You need to install the **AWS CLI** and configure your credentials. You can follow this [link](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html) for instructions.

### Install Serverless Framework

Then you will have to install the **Serverless** framework via npm. See instructions [here](https://www.serverless.com/framework/docs/getting-started#via-npm).

## FastAPI Application

### Build the application

First of all, we will build our FastAPI application. Add **fastapi** dependency in your requirements.txt and install it.
Then you can create your FastAPI application:

<!-- CODE:START file=../fastapi_aws_starter_kit/fastapi_app.py -->
``` Python
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from fastapi_aws_starter_kit.routers.health_check_api import router as hc_router
from fastapi_aws_starter_kit.config import PROJECT_NAME, API_VERSION

# Declare the application
app = FastAPI(title=PROJECT_NAME, debug=False, version=API_VERSION)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get(path="/health", description="Health check")
def health_check():
    return {"status": "OK"}


app.include_router(hc_router)

```
<!-- CODE:END -->

## Deploy FastAPI on AWS

To deploy our API in **AWS**, we will leverage **API Gateway** and **Lambda** services and use **Serverless** framework capabilities to easily create all resources we need.

### Lambda handler with Mangum

In order to build the handler for our Lambda which will be called by our API Gateway, we will use [**Mangum**](https://github.com/jordaneremieff/mangum) which is an ASGI adapter for API Gateway and Lambda (perfect for our FastAPI application 🍾)

Add **mangum** to your dependencies and build the handler as follow:

<!-- CODE:START file=../fastapi_aws_starter_kit/handler.py -->
``` Python
from mangum import Mangum
from fastapi_aws_starter_kit.fastapi_app import app

handler = Mangum(app=app)

```
<!-- CODE:END -->

### Configure serverless.yaml

Serverless configuration is pretty easy, here is what I did as a simple example:

<!-- CODE:START file=../serverless.yaml -->
``` MiniYAML
org: cox65
app: fastapi-aws-starter-kit
service: fastapi-aws-starter-kit
package:
  individually: true
provider:
  name: aws
  runtime: python3.12
  region: eu-west-1
  httpApi:
    cors: true
  timeout: 10
  memorySize: 128
plugins:
  - serverless-python-requirements
  - serverless-offline
functions:
  app:
    package:
      patterns:
        - "fastapi_aws_starter_kit/**"
    handler: fastapi_aws_starter_kit.handler.handler
    events:
      - http:
          method: any
          path: /{proxy+}
          cors: true
custom:
  pythonRequirements:
    dockerizePip: true

```
<!-- CODE:END -->

As you can see I’m using 2 plugins:

- **serverless-python-requirements:** It will bundle your python dependencies specified in your requirements.txt

- **serverless-offline:** It will allow to run our infrastructure locally by running **sls offline** command.

### Deploy your API

To deploy your API on AWS, you just need to perform:

```sh
sls deploy
```

## Run your API in local

If you want to run your API in local, you have two options.
Either you can run an [**uvicorn**](https://www.uvicorn.org/) web server like this:

<!-- CODE:START file=../fastapi_aws_starter_kit/web_server.py -->
``` Python
import os
import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        "fastapi_app:app",
        host="127.0.0.1",
        port=5000,
        reload=True,
    )

```
<!-- CODE:END -->

Either, and this what I recommend as we are using Serverless, you can use **serverless-offline** plugin I just mentionned before.

```sh
    ➜ sls offline
    Running "serverless" from node_modules
    Using local credentials. Add provider credentials via dashboard: https://app.serverless.com//providers

    Starting Offline at stage dev (eu-west-1)

    Offline [http for lambda] listening on http://localhost:3002
    Function names exposed for local invocation by aws-sdk:
               * app: fastapi-aws-starter-kit-dev-app
    
       ┌───────────────────────────────────────────────────────────────────────┐
       │                                                                       │
       │   ANY | http://localhost:3000/{proxy*}                                │
       │   POST | http://localhost:3000/2015-03-31/functions/app/invocations   │
       │                                                                       │
       └───────────────────────────────────────────────────────────────────────┘
    
    Server ready: http://localhost:3000 🚀

```

And that’s it ! 🚀

## FastAPI AWS Starter Kit

Here the the repository related to this article:
[**GitHub - DevWaveX/fastapi-aws-starter-kit: Starter kit to deploy FastAPI as an AWS serverless…**](https://github.com/DevWaveX/fastapi-aws-starter-kit)

I hope you enjoyed reading this article and that it will help you in your next projects ! 🤘

If you liked it, don’t forget to clap, share and subscribe 😉
