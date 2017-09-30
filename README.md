# ember-flask-github-auth
Github authentication using ember based app as UI and flask for rest layer

## Learning OAUTH - 
This repo conatins an ember app and shows how it can be used to authenticate with github.

## STEP1 
* Open Github.com -> settings create a OAUTH app
* put application name as flask or some other name
* Authorization callback URL to http://localhost:4200 or some other url which you want to be redirected
* notedown Client ID,Client Secret and application name
## STEP2 - API 
The folder api contains very simple api to exchange token
To run the flask app run the follwing command
* cd api
* virtualenv venv
* add the following lines in venv/bin/activate
  * export GITHUB_CLIENT_ID="<client id>"
  * export GITHUB_CLIENT_SECRET="<github client secret>"
  * export SESSION_SECRET_KEY="first_github_app"
  * export USER_AGENT="<application name>"
  * export TOKEN_URL="https://github.com/login/oauth/access_token"
* pip install -r requirements.txt
* source venv/bin/activate

## STEP3 - UI
The run the flask app run the following commands
* add the github client id for the value forapiKey variable in file config/environment.js
* npm install
* ember s

## STEP4
* open http://localhost:4200 in your browser




