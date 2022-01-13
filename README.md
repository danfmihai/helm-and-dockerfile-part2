# helm-and-dockerfile-part2

- The current repo has the helm chart for the app that returns the objects of a provided aws s3 bucket.
- In order to install the chart a `values.yaml` file is provided, in which you need to provide your required environment variables.

- Don't forget to change the values in exports-var.txt file and export the environment variables with:
```
source exports-var.txt
```

To test the docker image created with Dockerfile use command:
```
docker run -d --rm -p 5000:5000 -e AWS_ACCESS_KEY_ID -e AWS_SECRET_ACCESS_KEY -e TF_VAR_bucket_name -e AWS_DEFAULT_REGION misu3108/s3bucket:latest
```

To install the chart you can fill the env variables in the values.yaml and run the command:
```
helm install test-chart /. or

helm install test-chart /. --values myvalues.yaml # if you create your own myvalues.yaml file
```

- Also in this repo is the Dockerfile for the image that is used in the helm chart.