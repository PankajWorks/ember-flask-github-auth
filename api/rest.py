
from flask_cors import cross_origin
from flask import  Flask,jsonify, request

import logbook
import os
import requests


logger = logbook.Logger(__name__)

GITHUB_CLIENT_ID = os.environ['GITHUB_CLIENT_ID']
GITHUB_CLIENT_SECRET = os.environ['GITHUB_CLIENT_SECRET']
USER_AGENT = os.environ['USER_AGENT']
TOKEN_URL = os.environ['TOKEN_URL']

app = Flask(__name__)
app.secret_key = os.environ['SESSION_SECRET_KEY']


@app.route('/')
def hello():
    return "Hello from GITHUB AUTH API SYSTEM!"

@app.route('/v1/token',methods=['POST'])
@cross_origin(methods=['POST'])
def get_token():
    token = None
    auth_code = (request.json or {}).get('authorizationCode')
    logger.info(auth_code)
    if auth_code:
        client_id = GITHUB_CLIENT_ID
        client_secret = GITHUB_CLIENT_SECRET
        user_agent = USER_AGENT
        token_url = TOKEN_URL

        if not client_id:
            logger.error('No OAuth2 client id configured')
            error(404,'No OAuth2 client id configured')

        if not client_secret:
            logger.error('No OAuth2 client secret configured')
            error(404,'No OAuth2 client secret configured')
        
        payload = {
            'client_id': client_id,
            'client_secret': client_secret,
            'code': auth_code
        }
        headers = {'Accept': 'application/json', 'User-Agent': user_agent}
        logger.info(headers)
        r = requests.post(token_url, params=payload, headers=headers)
        response = r.json()
        # get access_token from response and store in session
        if 'access_token' in response:
            token = response['access_token']
        else:
            error(400,'github didn\'t return an access token, oh dear')
        return jsonify(access_token = token)
    return error(404,'Authorization Code not found')

def error(status_code, message):
    resp = jsonify(message=message, status_code=status_code)
    resp.status_code = status_code
    return resp

if __name__ == '__main__':
    app.run(debug=True)

"""
 How to run 
 Register a new application in Github
 The callback url should be http://localhost:5000/callback/github

PUT CONFIG FILE

open github-oauth/.env and put the following 
GITHUB_CLIENT_ID=(Your app's client ID)
GITHUB_CLIENT_SECRET=(Your apps' client secret)
SESSION_SECRET_KEY=(Random string)

If you are using virtualenv then export the variables in  bin/activate file.

"""
