---
title: ⚡ Serverless REST API on AWS with FastAPI ⚡
tags:
  - Python
  - AWS
canonicalUrl: >-
  https://medium.com/aws-tip/serverless-rest-api-on-aws-with-fastapi-bd9de11f925a
coverImage: >-
  https://github.com/DevWaveX/fastapi-aws-starter-kit/raw/main/article/cover.png
publications:
  - platform: devTo
    published: false
  - platform: hashnode
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
[{"filename": "../fastapi_aws_starter_kit/fastapi_app.py"}]: 🎨
<a href="https://github.com/DevWaveX/fastapi-aws-starter-kit/blob/main/fastapi_aws_starter_kit/fastapi_app.py" target="_blank">![🎨../fastapi_aws_starter_kit/fastapi_app.py](https://github.com/DevWaveX/fastapi-aws-starter-kit/raw/main/article/carbon/v6e5L5Y83opJr5DXMoVUci/fastapi_app.py.png)</a>

## Deploy FastAPI on AWS

To deploy our API in **AWS**, we will leverage **API Gateway** and **Lambda** services and use **Serverless** framework capabilities to easily create all resources we need.

### Lambda handler with Mangum

In order to build the handler for our Lambda which will be called by our API Gateway, we will use [**Mangum**](https://github.com/jordaneremieff/mangum) which is an ASGI adapter for API Gateway and Lambda (perfect for our FastAPI application 🍾)

Add **mangum** to your dependencies and build the handler as follow:
[{"filename": "../fastapi_aws_starter_kit/handler.py"}]: 🎨
<a href="https://github.com/DevWaveX/fastapi-aws-starter-kit/blob/main/fastapi_aws_starter_kit/handler.py" target="_blank">![🎨../fastapi_aws_starter_kit/handler.py](https://github.com/DevWaveX/fastapi-aws-starter-kit/raw/main/article/carbon/8Kub2wEE4v4GAPYnxzrktD/handler.py.png)</a>

### Configure serverless.yaml

Serverless configuration is pretty easy, here is what I did as a simple example:
[{"filename": "../serverless.yaml"}]: 🎨
<a href="https://github.com/DevWaveX/fastapi-aws-starter-kit/blob/main/serverless.yaml" target="_blank">![🎨../serverless.yaml](https://github.com/DevWaveX/fastapi-aws-starter-kit/raw/main/article/carbon/bEJmxXKPp5LvJcHwD5SCEQ/serverless.yaml.png)</a>

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
[{"filename": "../fastapi_aws_starter_kit/web_server.py"}]: 🎨
<a href="https://github.com/DevWaveX/fastapi-aws-starter-kit/blob/main/fastapi_aws_starter_kit/web_server.py" target="_blank">![🎨../fastapi_aws_starter_kit/web_server.py](https://github.com/DevWaveX/fastapi-aws-starter-kit/raw/main/article/carbon/vXkRQ52Xj9V7Vhij1LdQEA/web_server.py.png)</a>

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
       │   ANY | http://localhost:3000/dev/{proxy*}                            │
       │   POST | http://localhost:3000/2015-03-31/functions/app/invocations   │
       │                                                                       │
       └───────────────────────────────────────────────────────────────────────┘

    Server ready: http://localhost:3000
```

And that’s it ! 🚀

## FastAPI AWS Starter Kit

Here the the repository related to this article:
[**GitHub - Cox65/fastapi-aws-starter-kit: Starter kit to deploy FastAPI as an AWS serverless…**](https://github.com/Cox65/fastapi-aws-starter-kit)

I hope you enjoyed reading this article and that it will help you in your next projects ! 🤘

If you liked it, don’t forget to clap, share and subscribe 😉
