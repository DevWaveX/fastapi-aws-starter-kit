Serverless REST API on AWS with FastAPI
==================

![Banner](Banner.png)

![Deployment](https://github.com/Cox65/fastapi-aws-starter-kit/actions/workflows/main.yaml/badge.svg)

This starter kit shows how to deploy a serverless REST API on AWS using:
* Python
* Poetry
* FastAPI
* Serverless framework

### A. Installation
All the following installation steps for the first time only

#### 1. Install Make
- Make sure to setup `make` on your OS, if you are not able to setup `make`, please use command on the `Makefile`

#### 2. Install Nodejs and projects node_modules
- If you havent install Nodejs before please install it.
- It is recommended to install LTS versions.
- Note: the project is using Nodejs v16.20.2 but any Nodejs newer versions should be fine.

When you have Nodejs installed, let install the `node_modules`:
```bash
npm i
```
Or if you have `make`:
```bash
make install-serverless
```

#### 3. Install Python and packages
- If you havent install Python before please install it.
- Note: the project is using Python3.9 but any Python3 newer versions should be fine.

#### 4. Install Miniconda

- If you are using Linux:

```bash
curl -sL \
  "https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh" > \
  "Miniconda3.sh"
bash Miniconda3.sh
```

- If you are using MacOS:

```bash
curl -sL \
  "https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh" > \
  "Miniconda3.sh"
bash Miniconda3.sh
```

- If you are using Windows:

Go to this page: https://repo.anaconda.com/miniconda/ and download and install the latest `.exe` package

Note: when install `miniconda`, please read carefully its instruction, it is pretty straight forward

#### 5. Install new conda environment
```bash
conda env create -f environment.yml
```

#### 6. Activate the new conda environment
```bash
conda activate serverless_env
```

#### 6. Install Python packages
```bash
poetry install
```

or if you have `make`:
```bash
make install-python-requirements
```

Now its time to go to the next steps!

### B. Local development
1. If you havent activated your `conda` environment, let's activate it:
```bash
conda activate serverless_env
```

2. Run the following command to start local server
```bash
npx sls offline
```
or if you have `make`:
```
make serve
```

3. Testing:
```bash
curl localhost:3000/dev/health
```
Or you can visit this link using your browser.

It should return:
```
{"status":"OK"}
```
![](https://i.imgur.com/fH0Y2dx.png)


### C. Deployment
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

Note: Read more about Setup an Serverless account here [](https://www.devops.ci/setup-your-serverless-account/)

- If you do not have Serverless account: go to the Deployment step

##### b. Deployment
Run the following command to deploy
```bash
make deploy
```
![](https://i.imgur.com/re6ApDp.png)
Note the endpoint so it can be used later.

##### c. Post-Deployment
Run the following command to test your endpoint (the default path is `health`):
```bash
curl your-serverless-endpoint
```
Here `your-serverless-endpoint` is the endpoint that you can get from the **Deployment** step above.
![](https://i.imgur.com/R366e1s.png)

### D. Remove app:
If you want to remove your app, run the following command:
```
npx sls remove
```
Or if you have `make`:
```bash
make remove
```
