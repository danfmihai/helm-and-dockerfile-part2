# helm-and-dockerfile-part2

- The current repo has the helm chart for the app that returns the objects of a provided aws s3 bucket.
- In order to install the chart a `values.yaml` file is provided, in which you need to provide your required environment variables.

To install the chart you can fill the env variables in the values.yaml and run the command:
```
helm install test-chart /. or

helm install test-chart /. --values myvalues.yaml # if you create your own myvalues.yaml file
```

- Also in this repo is the Dockerfile for the image that is used in the helm chart.