from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin


spec = APISpec(
    title="SAM apispec",
    version="0.0.1",
    openapi_version="3.0.3",
    plugins=[MarshmallowPlugin()],
)
