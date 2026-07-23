import functions_framework


@functions_framework.http
def hello_http(request):
    return {
        "status": "success",
        "message": "Cloud Native File Processing Platform is running!"
    }