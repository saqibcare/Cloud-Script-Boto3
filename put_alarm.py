import boto3

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
    Statistic='Average',
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


# client2 = boto3.client2('autoscaling')
# response = client2.put_scaling_policy(
#     AutoScalingGroupName='auto-scaling-group',
#     PolicyName='greaterThan10 ',
#     PolicyType='SimpleScaling ',
#     # AdjustmentType='string',
#     # MinAdjustmentStep=123,
#     # MinAdjustmentMagnitude=123,
#     # ScalingAdjustment=123,
#     Cooldown=120,
#     MetricAggregationType='string',
#     StepAdjustments=[
#         {
#             'MetricIntervalLowerBound': 123.0,
#             'MetricIntervalUpperBound': 123.0,
#             'ScalingAdjustment': 123
#         },
#     ],
#     EstimatedInstanceWarmup=123,
#     TargetTrackingConfiguration={
#         'PredefinedMetricSpecification': {
#             'PredefinedMetricType': 'ASGAverageCPUUtilization'|'ASGAverageNetworkIn'|'ASGAverageNetworkOut'|'ALBRequestCountPerTarget',
#             'ResourceLabel': 'string'
#         },
#         'CustomizedMetricSpecification': {
#             'MetricName': 'string',
#             'Namespace': 'string',
#             'Dimensions': [
#                 {
#                     'Name': 'string',
#                     'Value': 'string'
#                 },
#             ],
#             'Statistic': 'Average'|'Minimum'|'Maximum'|'SampleCount'|'Sum',
#             'Unit': 'string'
#         },
#         'TargetValue': 123.0,
#         'DisableScaleIn': False
#     }
# )