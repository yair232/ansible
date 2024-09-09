import boto3
    # create a new EC2 client
ec2 = boto3.resource('ec2')
response = ec2.create_instances(
    ImageId= 'ami-0e86e20dae9224db8',
    InstanceType= 't2.medium',
    MinCount=1,
    MaxCount=1,
    KeyName= "yairg",
    SecurityGroupIds= ['sg-0cb8272bc259f528d'],
    SubnetId='subnet-05aef944f475b371d',
    TagSpecifications=[{'ResourceType': 'instance', 'Tags': [{'Key': 'Name','Value': 'yair-new'}]}],
)[0]
#wait for the instance upload and print when finish
response.wait_until_running()
response.reload()
print(response.public_ip_address)
