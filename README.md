# cu-zn
A Python client for the Braze Customer Engagement Platform REST API

# Getting started
```python
import cuzn

client = cuzn.configure(braze_endpoint="https://abc.xyz", braze_api_key="foobar")

# Or, if environment variables are set, you can just do
client = cuzn.configure()
```

> **Info**
> If `None` values (default) are passed as arguments to the `configure` function, the
> environment variables `CUZN_BRAZE_ENDPOINT` and `CUZN_BRAZE_API_KEY` will be used, if
> set (`.env` file configuration is supported). A `ConfigurationError` exception will
> raise if nether of these options are defined.
