#!/usr/bin/env python


import boto3


#LoadBalancer


client = boto3.client('elb')
response = client.create_load_balancer(
    LoadBalancerName='testloadbalancer',
    Listeners=[
        {
            'Protocol': 'HTTP',
            'LoadBalancerPort': 80,
            'InstanceProtocol': 'HTTP',
            'InstancePort': 80,
            # 'SSLCertificateId': 'string'
        },
    ],
    # AvailabilityZones=[
    #     'us-west-2c',
    #     # 'us-west-2a',
    #     # 'us-west-2b',
    # ],
    Subnets=[
        'subnet-0cd1fc56',
        # 'subnet-0cd1fc56',
        # 'subnet-0cd1fc56',
    ],
    SecurityGroups=[
        'sg-8eed3cfc',
    ],
    Scheme='internet-facing',
    # Tags=[
    #     {
    #         'Key': 'string',
    #         'Value': 'string'
    #     },
    # ],
)
response = client.configure_health_check(
    LoadBalancerName='testloadbalancer',
    HealthCheck={
        'Target': 'HTTP:80/',
        'Interval': 30,
        'Timeout': 5,
        'UnhealthyThreshold': 2,
        'HealthyThreshold': 10
    }
)

response = client.modify_load_balancer_attributes(
    LoadBalancerName='testloadbalancer',
    LoadBalancerAttributes={
        'CrossZoneLoadBalancing': {
            'Enabled': True
        },
        # 'AccessLog': {
        #     'Enabled': True|False,
        #     'S3BucketName': 'string',
        #     'EmitInterval': 123,
        #     'S3BucketPrefix': 'string'
        # },
        'ConnectionDraining': {
            'Enabled': True,
            'Timeout': 300
        },
        # 'ConnectionSettings': {
        #     'IdleTimeout': 123
        # },
        # 'AdditionalAttributes': [
        #     {
        #         'Key': 'string',
        #         'Value': 'string'
        #     },
        # ]
    }
)



##################################################################################################################3

# #Launch Configuration



# test1 = 'user_data\nset -e -x\nsudo yum update -y\nsudo yum install -y httpd24 php72 php72-mysqlnd\n',
# test2 = 'sudo service httpd start\ncd /var/www/html\nsudo git clone https://github.com/ChristianHMeier/cc-images',
# client2 = boto3.client('autoscaling')
# response = client2.create_launch_configuration(
#     LaunchConfigurationName='autoscaling-launchconfiguration',
#     ImageId='ami-a0cfeed8',
#     KeyName='saqib1-key',
#     SecurityGroups=[
#         'sg-8eed3cfc',
#     ],
#     # ClassicLinkVPCId='string',
#     # ClassicLinkVPCSecurityGroups=[
#     #     'string',
#     # ],
#
#     UserData='',
#         # '#!/bin/bash',
#         # 'set -e -x',
#         # 'sudo yum update -y',
#         # 'sudo yum install -y httpd24 php72 php72-mysqlnd',
#         # 'sudo service httpd start',
#         # 'sudo yum install git -y',
#         # 'cd /var/www/html',
#         # 'sudo git clone https://github.com/ChristianHMeier/cc-images',
#
#     # InstanceId='string',
#     InstanceType='t2.micro',
#     KernelId='Use default',
#     RamdiskId='Use default',
#     BlockDeviceMappings=[
#         {
#
#             # 'VirtualName': 'string',
#             'DeviceName': '/dev/xvda',
#             'Ebs': {
#                 'SnapshotId': 'snap-0b9ac5da0147e5eb2',
#                 'VolumeSize': 8,
#                 'VolumeType': 'standard',
#                 'DeleteOnTermination': True,
#                 # 'Iops': 100 / 3000,
#                 'Encrypted': False
#             },
#             # 'NoDevice': False
#         },
#     ],
#     InstanceMonitoring={
#         'Enabled': False
#     },
#     # SpotPrice='string',
#     IamInstanceProfile='S3-Role',
#     EbsOptimized=False,
#     AssociatePublicIpAddress=True,
#     PlacementTenancy='default'
# )

##########################################################################################

#Creating Auto Scaling Group

client3 = boto3.client('autoscaling')
response = client3.create_auto_scaling_group(
    AutoScalingGroupName='auto-scaling-group',
    # LaunchConfigurationName='autoscaling-launchconfiguration',
    # LaunchTemplate={
    #     'LaunchTemplateId': 'string',
    #     'LaunchTemplateName': 'string',
    #     'Version': 'string'
    # },
    InstanceId='i-01557ffa4959b3cfd',
    MinSize=1,
    MaxSize=5,
    DesiredCapacity=1,
    DefaultCooldown=200,
    # AvailabilityZones=[
    #     'us-west-2',
    # ],
    LoadBalancerNames=[
        'testloadbalancer',
    ],
    # TargetGroupARNs=[
    #     'string',
    # ],
    HealthCheckType='EC2',
    HealthCheckGracePeriod=300,
    # PlacementGroup='string',
    VPCZoneIdentifier='subnet-0cd1fc56',
    # TerminationPolicies=[
    #     'string',
    # ],
    NewInstancesProtectedFromScaleIn=False,
    # LifecycleHookSpecificationList=[
    #     {
    #         'LifecycleHookName': 'string',
    #         'LifecycleTransition': 'string',
    #         'NotificationMetadata': 'string',
    #         'HeartbeatTimeout': 123,
    #         'DefaultResult': 'string',
    #         'NotificationTargetARN': 'string',
    #         'RoleARN': 'string'
    #     },
    # ],
    Tags=[
        {
            # 'ResourceId': 'string',
            # 'ResourceType': 'string',
            'Key': 'Name',
            'Value': 'autoscaling',
            # 'PropagateAtLaunch': True|False
        },
    ],
    # ServiceLinkedRoleARN='string'
)


###########################################################################333

alarm = boto3.client('cloudwatch')
response = alarm.put_metric_alarm(
    AlarmName='greaterThan10',
    AlarmDescription='string',
    ActionsEnabled=False,
    # OKActions=[
    #     'string',
    # ],
    # AlarmActions=[
    #     'string',
    # ],
    # InsufficientDataActions=[
    #     'string',
    # ],
    MetricName='RequestCount',
    Namespace='AWS/ELB',
    Statistic='Sum',
    # ExtendedStatistic='p90',
    Dimensions=[
        {
            'Name': 'Service',
            'Value': 'ELB'
        },
    ],
    Period=60,
    # Unit='Seconds'|'Microseconds'|'Milliseconds'|'Bytes'|'Kilobytes'|'Megabytes'|'Gigabytes'|'Terabytes'|'Bits'|'Kilobits'|'Megabits'|'Gigabits'|'Terabits'|'Percent'|'Count'|'Bytes/Second'|'Kilobytes/Second'|'Megabytes/Second'|'Gigabytes/Second'|'Terabytes/Second'|'Bits/Second'|'Kilobits/Second'|'Megabits/Second'|'Gigabits/Second'|'Terabits/Second'|'Count/Second'|'None',
    EvaluationPeriods=1,
    DatapointsToAlarm=1,
    Threshold=10.0,
    ComparisonOperator='GreaterThanThreshold',
    # TreatMissingData='string',
    # EvaluateLowSampleCountPercentile='string'
)