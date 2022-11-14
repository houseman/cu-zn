def test_init(mocker):
    from cuzn.session import BrazeSession

    requests_session = mocker.Mock()

    session = BrazeSession(session=requests_session)

    assert session.__session__ is requests_session


def test_send(mocker):
    from cuzn import session as module
    from cuzn.request import BrazeRequest, RequestMethod
    from cuzn.session import BrazeSession

    request = BrazeRequest(
        method=RequestMethod.POST, path="/foo/bar", data={"foo": "bar"}
    )

    requests_response = mocker.Mock()
    requests_response.status_code = 201
    requests_response.text = "OK"

    requests_session = mocker.Mock()
    requests_session_send = mocker.patch.object(
        requests_session, "send", return_value=requests_response
    )
    prepared_request = mocker.Mock()

    requests_request = mocker.Mock()
    requests_request.prepare.return_value = prepared_request
    mocker.patch.object(module.requests, "Request", return_value=requests_request)

    session = BrazeSession(session=requests_session)
    response = session.send(request=request)

    requests_session_send.assert_called_with(request=prepared_request)

    assert response.code == 201
    assert response.content == "OK"
