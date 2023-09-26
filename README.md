Serverless REST API on AWS with FastAPI
==================

![Banner](Banner.png)

![Deployment](https://github.com/Cox65/fastapi-aws-starter-kit/actions/workflows/main.yaml/badge.svg)

This starter kit shows how to deploy a serverless REST API on AWS using:
* Python
* Poetry
* FastAPI
* Serverless framework

### Installation
### Local development

```bash
make serve
```
### Deployment
#### 1. Deploy locally
##### a. Pre-deployment
- If you have a Serverless account

```bash
npx serverless login
```

Then you will be able to login using your browsers.

![](https://i.imgur.com/KDpIpco.png)

If you havent created an app before, please go to your Serverless dashboard and create a new project, it must have same name as your app name (on the `serverless.yaml` file):

![](https://i.imgur.com/cuulyzZ.png)

In this example:

![](https://i.imgur.com/zMLe2mm.png)

![](https://i.imgur.com/BD6lkVA.png)

- If you do not have Serverless account: go to the Deployment step

##### b. Deployment
Run the following command to deploy
```bash
make deploy
```
![](https://i.imgur.com/re6ApDp.png)
Note the endpoint so it can be used later.

##### c. Post-Deployment
Run the following command to test your endpoint:
```bash
curl your-serverless-endpoint
```
Here `your-serverless-endpoint` is the endpoint that you can get from the **Deployment** step above.
![](https://i.imgur.com/R366e1s.png)

### Remove app:
If you want to remove your app, run the following command:
```bash
make remove
```
