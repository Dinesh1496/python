import requests
import boto3


response=requests.get("https://api.github.com/repos/iam-veeramalla/python-for-devops/pulls")


complete_detail = response.json()


print (complete_detail[0]["id"])
print(response.status_code)

#go to the above url using browser and code it

print(complete_detail[0]["user"]["login"])

for i in range(len(complete_detail)):
    print(complete_detail[i]["user"]["login"])
    print(complete_detail[i]["id"])

