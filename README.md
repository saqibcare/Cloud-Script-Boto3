# 


Requirements:-
  -Python
  -boto3
  -awscli

# Cloud-Script-Boto3 with AWS services

In this Tutorial we are going to intereact with some AWS services Script without moving towards the GUI.

## Getting Started
Follow the following steps in order to fullfill the respective tasks


### Prerequisites

First of all you need to install following libraries into your computer in order to interact with AWS services
  * Python
  * boto3
  * awscli
  * AWS Account

### Working with awscli

After installing the given libraries open **cmd** and type

```
aws configure
```

it will ask you to provide the following credentials 

```
AWS Access Key ID: [Provide KEY ID of your AWS account here]
AWS Secret Access Key: [Provide SECRET KEY of your AWS account here]
```
then you need to enter the region id here, where you wana connect.
```
Default region name [us-west-2]:
```
Default region is us-west-2, just press enter if you don't want to change.
```
Default output format [text]:
```
just press enter on the output as well to leave it text.

Now we are up to connection, Never hard code your security keys in the script of never upload them to any online repository.


