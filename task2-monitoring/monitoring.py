# Task 2 - Cloud Monitoring and Alerts
import boto3

cloudwatch = boto3.client("cloudwatch", region_name="us-east-1")

INSTANCE_ID = "i-01b2b0e22aa4aa7e1"
SNS_ARN = "arn:aws:sns:us-east-1:350475136594:codtech-alerts"

# Create CPU alarm
def create_cpu_alarm():
    cloudwatch.put_metric_alarm(
        AlarmName="HighCPUAlarm",
        MetricName="CPUUtilization",
        Namespace="AWS/EC2",
        Statistic="Average",
        Period=300,
        Threshold=70,
        ComparisonOperator="GreaterThanThreshold",
        Dimensions=[{"Name": "InstanceId", "Value": INSTANCE_ID}],
        EvaluationPeriods=2,
        AlarmActions=[SNS_ARN]
    )
    print("CPU Alarm created")

# List alarms
def list_alarms():
    response = cloudwatch.describe_alarms()
    for alarm in response["MetricAlarms"]:
        print(f"{alarm["AlarmName"]}: {alarm["StateValue"]}")

if __name__ == "__main__":
    list_alarms()
