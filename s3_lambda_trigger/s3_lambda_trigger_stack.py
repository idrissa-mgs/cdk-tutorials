from aws_cdk import (
    core as cdk,
    aws_lambda as _lambda,
    aws_iam  as _iam, 
    aws_s3 as _s3,
    aws_s3_notifications as _s3_notifications

)

# For consistency with other languages, `cdk` is the preferred import name for
# the CDK's core module.  The following line also imports it as `core` for use
# with examples from the CDK Developer's Guide, which are in the process of
# being updated to use `cdk`.  You may delete this import if you don't need it.
from aws_cdk import core


class S3LambdaTriggerStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)



        # The code that defines your stack goes here

        #IAM USER
        #user = _iam.User(self, "VSUser")

        #S3BUCKET and grant 
        bucket = _s3.Bucket(self, 'vs-bucket')
        #bucket.grant_read_write(user)

        #LAMBDA FUNCTION
        my_function = _lambda.Function(self, "ma_funct_lambda", 
        runtime=_lambda.Runtime.PYTHON_3_7,
        code=_lambda.Code.from_asset('lambda_'),
        handler="main.handler", 
        environment={'BUCKET_NAME':bucket.bucket_name}
        )

        #S3 NOTIFICATION
        notification = _s3_notifications.LambdaDestination(my_function)
        notification.bind(self, bucket)

        #add object creation notificaton

        bucket.add_object_created_notification(notification)
