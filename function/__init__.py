import azure.functions as func
from ..app import app

def main(req: func.HttpRequest, context: func.Context) -> func.HttpResponse:
    """
    Each request is redirected to the WSGI handler.
    """
    func.__name__ = "Homepage"
    return func.WsgiMiddleware(app.wsgi_app).handle(req, context)