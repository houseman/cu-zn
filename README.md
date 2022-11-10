# cu-zn
A Python client for the Braze Customer Engagement Platform REST API

## Getting started
```python
import cuzn

client = cuzn.configure(braze_endpoint="https://abc.xyz", braze_api_key="foobar")

# Or, if environment variables are set, you can just do
client = cuzn.configure()
```

> **Note**
> If `None` values (default) are passed as arguments to the `configure` function, the
> environment variables `CUZN_BRAZE_ENDPOINT` and `CUZN_BRAZE_API_KEY` will be used, if
> set (`.env` file configuration is supported). A `ConfigurationError` exception will
> raise if nether of these options are defined.

## Response
Client request methods will return an `ApiResponse` object instance. This provides some useful methods.
```python
from cuzn.response import ApiResponse

success = ApiResponse(200, '{"foo": "bar"}')
success.is_success()  # True, response code is 200
success.is_error()  # False, ditto
success.payload().get("foo")  # "bar"
success.payload().get("snafu")  # None
success.payload().get("snafu", "bar")  # "bar"
```

## Dev Tools
This project uses pip-tools to maintain dependency versions.

> **Note**
> Do _not_ edit `*.requirements.txt` files directly. Requirements are defined in the `pyproject.toml` file.

The `Makefile` defines the following targets
### Update dependency versions

> **Note**
> This will also run `make pip-sync`

```shell
make pip-compile
```

### Install dependencies
```shell
make pip-sync
```

### Run unit tests in local virtual environment
```shell
make test
```

### Run linting in local virtual environment
```shell
make lint
```

### Run nox tests

> Runs tests and linters for Python versions `>= 3.7, <= 3.11`

```shell
make run-nox
```
