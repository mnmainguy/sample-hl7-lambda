import json

import pytest

from hl7_receiver import app


@pytest.fixture()
def apigw_event():
    """ Generates API GW Event"""

    return {
        "body": 'MSH|^~\\&|ADTOUT|TESTSYSTEM|TWISTLE|TWISTLE|20220902090245||ADT^A03|Q11887566466T11159470345X24062|P|2.3||||||8859/1\nPID|1||222222^^^Good MRN^MRN^~1111111^^^Bad MRN^MRN^||DUCK^DONALD^^^^^Current||19900101|M|^Don^^^^^Preferred|U|111^DUCK ST^^FOWL^CA^999990000^US^home||(999)999-9999^Home^TEL~(500)999-9999^Mobile/Telecommunications||EN|U|UNK|0010001^^^FIN Number^FIN NBR|999999999|||U|||0\nPV1|1|O|BPMCCNC^^^BPMCCNC^^Ambulatory(s)^BPMCCNC|3|||1949375608^DISNEY^WALT^D^^MD^^^National Provider ID^Personnel^^^National Provider Identifier|||CVM||||2|||1949375608^DISNEY^WALT^D^^MD^^^National Provider ID^Personnel^^^National Provider Identifier|O||P|Ou|||||||||||||||01|||BP||DIS|||20220901085700|20220902090200',
        "resource": "/{proxy+}",
        "requestContext": {
            "resourceId": "123456",
            "apiId": "1234567890",
            "resourcePath": "/{proxy+}",
            "httpMethod": "POST",
            "requestId": "c6af9ac6-7b61-11e6-9a41-93e8deadbeef",
            "accountId": "123456789012",
            "identity": {
                "apiKey": "",
                "userArn": "",
                "cognitoAuthenticationType": "",
                "caller": "",
                "userAgent": "Custom User Agent String",
                "user": "",
                "cognitoIdentityPoolId": "",
                "cognitoIdentityId": "",
                "cognitoAuthenticationProvider": "",
                "sourceIp": "127.0.0.1",
                "accountId": "",
            },
            "stage": "prod",
        },
        "queryStringParameters": {"foo": "bar"},
        "headers": {
            "Via": "1.1 08f323deadbeefa7af34d5feb414ce27.cloudfront.net (CloudFront)",
            "Accept-Language": "en-US,en;q=0.8",
            "CloudFront-Is-Desktop-Viewer": "true",
            "CloudFront-Is-SmartTV-Viewer": "false",
            "CloudFront-Is-Mobile-Viewer": "false",
            "X-Forwarded-For": "127.0.0.1, 127.0.0.2",
            "CloudFront-Viewer-Country": "US",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Upgrade-Insecure-Requests": "1",
            "X-Forwarded-Port": "443",
            "Host": "1234567890.execute-api.us-east-1.amazonaws.com",
            "X-Forwarded-Proto": "https",
            "X-Amz-Cf-Id": "aaaaaaaaaae3VYQb9jd-nvCd-de396Uhbp027Y2JvkCPNLmGJHqlaA==",
            "CloudFront-Is-Tablet-Viewer": "false",
            "Cache-Control": "max-age=0",
            "User-Agent": "Custom User Agent String",
            "CloudFront-Forwarded-Proto": "https",
            "Accept-Encoding": "gzip, deflate, sdch",
        },
        "pathParameters": {"proxy": "/examplepath"},
        "httpMethod": "POST",
        "stageVariables": {"baz": "qux"},
        "path": "/examplepath",
    }


def test_lambda_handler(apigw_event, mocker):

    ret = app.lambda_handler(apigw_event, "")
    data = json.loads(ret["body"])

    assert ret["statusCode"] == 200
    assert data["firstname"] == "Donald"
    assert data["lastname"] == "Duck"
    assert data["external_id"] == "222222"
    assert data["phone"] == "5009999999"
    assert data["dob"] == "01/01/1990"
    assert data["gender"] == "M"
    assert data["discharge_date"] == "2022-09-02T09:02:00"