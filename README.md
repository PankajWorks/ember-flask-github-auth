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


### Prerequisites

You will need the following things properly installed on your computer.

* [Git](https://git-scm.com/)
* [Node.js](https://nodejs.org/) (with NPM)
* [Ember CLI](https://ember-cli.com/)
* [PhantomJS](http://phantomjs.org/)

### Installation

* `git clone <repository-url>` this repository
* `cd ember-flask-github-auth`
* `npm install`

### Running / Development
* add the github client id for the value forapiKey variable in file config/environment.js
* `ember s` or `ember serve`
* Visit your app at [http://localhost:4200](http://localhost:4200).

### Code Generators

Make use of the many generators for code, try `ember help generate` for more details

### Running Tests

* `ember test`
* `ember test --server`

### Building

* `ember build` (development)
* `ember build --environment production` (production)

### Deploying

Specify what it takes to deploy your app.

## Further Reading / Useful Links

* [ember.js](http://emberjs.com/)
* [ember-cli](https://ember-cli.com/)
* Development Browser Extensions
  * [ember inspector for chrome](https://chrome.google.com/webstore/detail/ember-inspector/bmdblncegkenkacieihfhpjfppoconhi)
  * [ember inspector for firefox](https://addons.mozilla.org/en-US/firefox/addon/ember-inspector/)



## STEP4
* open http://localhost:4200 in your browser




