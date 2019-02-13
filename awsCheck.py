import boto3 
import pandas as pd
from io import StringIO  


s3 = boto3.client('s3')

response = s3.list_buckets()

bucks = [bucket['Name'] for bucket in response['Buckets']]

file_nM = "/home/adithya/DAQ-Sensor/DataStored/measurement0025"

bucket_nM = bucks[0]

#s3.upload_file(file_nM+".csv", bucket_nM, "Measurements")

readCSV = pd.read_csv(file_nM+".csv")

csv_buffer = StringIO()

readCSV.to_csv(csv_buffer)

#error
s3_resource = boto3.resource('s3')
 
s3_resource.Object(bucket_nM, 'df.csv').put(Body=csv_buffer.getvalue())

#s3.upload_file(csv_buffer.getvalue(), bucket_nM, "Measurements")

#print (readCSV.head)

print("done")
