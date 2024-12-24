student_info = {
    "name": "John",
    "age": 20,
    "grade": "A",
    "class" : 12,
}

print(student_info["name"])
print(student_info["class"])


ec2_instance_info =  [
    {
    "id": "instance-01",
    "type": "t2.micro",
    "region": "us-west-1",
    },

    {
    "id": "instance-02",
    "type": "t2.nano",
    "region": "ap-south-1",
    },

    {
    "id": "instance-03",
    "type": "t2.medium",
    "region": "us-east-2",
    }
]

print(ec2_instance_info[0]["id"])
print(ec2_instance_info[1]["region"],ec2_instance_info[2]["type"])
print(ec2_instance_info[2]["type"], ec2_instance_info[2]["id"])