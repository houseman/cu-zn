def test_configure():
    import cuzn

    braze_endpoint = "https://abc.xyz"
    braze_api_key = "foobar"

    client = cuzn.configure(braze_endpoint=braze_endpoint, braze_api_key=braze_api_key)

    assert client._endpoint == braze_endpoint
    assert client._api_key == braze_api_key
