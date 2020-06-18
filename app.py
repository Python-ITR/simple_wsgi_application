from views import index_view, about_view


def application(headers, start_response):
    response = None
    PATH_INFO = headers.get("PATH_INFO")
    if PATH_INFO == "/":
        response = index_view()
    if PATH_INFO == "/about":
        response = about_view()
    if response is None:
        start_response("404 NOT_FOUND", [("Content-Type", "text/plain")])
        return [b"NOT_FOUND"]
    start_response("200 OK", [("Content-Type", "text/plain")])
    return [response.encode()]
