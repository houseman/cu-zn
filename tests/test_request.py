def test_init(mocker):
    from cuzn.request import BrazeRequest

    method = mocker.Mock()
    path = mocker.Mock()
    data = mocker.Mock()

    request = BrazeRequest(method=method, path=path, data=data)

    assert request.__method__ is method
    assert request.__path__ is path
    assert request.__data__ is data
