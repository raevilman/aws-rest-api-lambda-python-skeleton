### Skeleton project for AWS Lambda - Python

**NOTE:**   
[1] _boto3 related functionality isn't tested, as I was exporting the zip only._  
[2] _Change the lib folder path in manage.py. Currently set to venv folder of pycharm_

| File name | Purpose |
| :---     |  :---
| lambda_function.py | Entry point for the lambda |  
| env.json | Environment variable of lambda when deployed  
| manage.py | Includes functions to package, create, deploy the lambda  
| app | Main source folder for the app. Logic should go in function.py -> run method or make changes accordingly.

