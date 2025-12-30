import requests
import os
from dotenv import load_dotenv

load_dotenv()

AUTH_CREDENTIALS = (os.getenv("N8N_WORKFLOW_USERNAME"), os.getenv("N8N_WORKFLOW_PWD"))

URL = "http://localhost:5678/webhook/a40acb26-d510-4664-98f4-ea535b0e5244"


#body  = {"data":"What is the monthly cost of the Fiber 500 plan?"}
#body  = {"data":"Wht are some residential home internet installation pre-requisites?"}
body = {"data":"Can you explain notice period for price increases?"}



print(requests.post(URL, body, auth = AUTH_CREDENTIALS).json())