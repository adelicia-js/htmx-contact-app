**UPDATE:** The app is no longer hosted, as my free trial for Google Cloud reached its end.

**Note:** The following steps were carried out on an Ubuntu machine.

## Setup

### To clone this app
Type this into your terminal

    git clone https://github.com/adelicia-js/htmx-contact-app.git

### Run the app

#### Open app
    cd htmx-contact-app 
    
    code .

#### Set up venv 

    python3-m venv venv

    source venv/bin/activate

(Remember to do the activation step every time)

#### Install requirements

    pip install -r requirements.txt

#### Run app

    flask run

Navigate to http://127.0.0.1:5000/contacts :D

## Deployment/Production

### Using Gunicorn

#### Install gunicorn 

    pip install gunicorn

#### Create a config file

    cat > gunicorn_config.py

        workers = 4  
        bind = '0.0.0.0:8000'  
        accesslog = '-' 
        errorlog = '-'

Ctrl + C to exit editor  mode

#### Run app

    gunicorn -c gunicorn_config.py app:app

Navigate to http://0.0.0.0:8000 :D

Relevant references:
- https://gunicorn.org/
- https://flask.palletsprojects.com/en/3.0.x/deploying/gunicorn/

### Using Google App Engine

Read through these docs before anything: 

- https://cloud.google.com/appengine/docs/standard/python3/building-app

- https://cloud.google.com/appengine/docs/standard/python3/building-app/creating-gcp-project

Installation link for gcloud CLI:
- https://cloud.google.com/sdk/docs/install

In the project folder, create a file called `app.yaml`

    cat > app.yaml

        runtime: python
        env: flex
        entrypoint: gunicorn -b :$PORT app:app

        runtime_config:
            operating_system: "ubuntu22"

Ctrl + C to exit editor mode

#### Initialize console

(Assuming you've installed the SDK already)

Navigate to project location

    gcloud init

Select app to be deployed/set up

#### Check permissions

Navigate to Console > Navigation Menu > IAM & Admin > IAM

Add following roles for your gmail account & the [project_name]@appspot.gserviceaccount.com:
- App Engine Deployer (most relevant role)
- App Engine Viewer
- App Engine Code Viewer

#### Deploy app

Go back to project location

    gcloud app deploy

Now, you wait. :)

#### Troubleshooting

In case `gcloud app deploy` still throws an error

Retry using
    
    gcloud auth login

    gcloud app deploy

Reference for help just in case: https://stackoverflow.com/questions/56126481/gcloud-error-gcloud-app-deploy-permissions-error-fetching-application
