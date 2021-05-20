import os
from app.schemes import spec
from app.functions.example.app import path
from app.schemes.example import ExampleSchema

spec.tag("Example")
spec.path(**path)
spec.components.schema("Example", schema=ExampleSchema)


if __name__ == "__main__":
    with open(f"{os.getcwd()}/openapi.yaml", mode='w') as f:
        f.write(spec.to_yaml())
