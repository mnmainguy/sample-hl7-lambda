import json
from hl7apy.parser import parse_message


def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """
    
    # Parse inbound payload using hl7apy library (http://crs4.github.io/hl7apy/api_docs/parser.html)
    hl7_message = parse_message(event["body"].replace('\n', '\r').replace('^^','^""^'))
    print(f"Received HL7 {hl7_message} with {hl7_message.children}")
    
    # Build response payload with expected fields parsed from HL7 (e.g. firstname, lastname, etc)
    response_payload = {}
    
    return {
        "statusCode": 200,
        "body": json.dumps(response_payload),
    }
