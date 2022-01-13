import os
import json
import boto3
from flask import request
from flask import render_template
from flask import Flask

env_var = ["AWS_ACCESS_KEY_ID","AWS_SECRET_ACCESS_KEY","TF_VAR_bucket_name"]

access_key_id = os.getenv(env_var[0])
secret_key = os.environ.get(env_var[1])
bucket_name = os.environ.get(env_var[2])

def get_env_vars():
  access_key_id = os.getenv(env_var[0])
  secret_key = os.environ.get(env_var[1])
  bucket_name = os.environ.get(env_var[2])


# current module (__name__) as argument.
app = Flask(__name__)

# check if variables are set
def check():
    get_env_vars()
    if access_key_id is not None or secret_key is not None or bucket_name is not None:
        print('Variables defined')
        return True
    else:
        print('Please export variables!')
        return False
    

session = boto3.Session( 
         aws_access_key_id = str(access_key_id), 
         aws_secret_access_key = str(secret_key)
)

#Then use the session to get the resource
s3 = session.resource('s3')
my_bucket = s3.Bucket(str(bucket_name))

@app.route("/health")
def health():
    return "Pass"

@app.route('/')
# ‘/’ URL is bound with the listS3 function.
def lists3():
    get_env_vars()
    if check() is False:
        return render_template("index.html", check=env_var , obj="not",bucket_err=" bucket found!", bucket_name=my_bucket.name,err="!! PLEASE SET THE ENVIRONMENT VARIABILES FOR AWS AND BUCKET NAME !!")
    else:
        if my_bucket.name != '' :
            list = []
            for my_bucket_object in my_bucket.objects.all():
                list.append(my_bucket_object.key)
                
            json_str = json.dumps(list, indent=2, separators=(',', ':'))
            print(json_str)
            return render_template("index.html", data=json_str, bucket_name=my_bucket.name)
        else:
            return render_template("index.html",bucket_name=my_bucket.name, bucket_err=" bucket found!") 

# main driver function
if __name__ == '__main__':
	app.run()