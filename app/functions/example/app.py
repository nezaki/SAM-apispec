import json

path = {
    "path": "/examples",
    "operations": dict(
        get=dict(
            tags=["Example"],
            responses={"200": {"content": {"application/json": {"schema": "Example"}}}})),
}


def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps({
            "id": 1234,
            "content": "content"
        }),
    }
