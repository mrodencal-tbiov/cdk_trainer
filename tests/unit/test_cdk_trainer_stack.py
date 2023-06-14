import aws_cdk as core
import aws_cdk.assertions as assertions

from cdk_trainer.cdk_trainer_stack import CdkTrainerStack

# example tests. To run these tests, uncomment this file along with the example
# resource in cdk_trainer/cdk_trainer_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CdkTrainerStack(app, "cdk-trainer")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
