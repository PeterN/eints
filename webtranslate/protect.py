"""
Bottle authentication decorator.
"""
from webtranslate.bottle import request, abort, error, response
from webtranslate import users, rights

@error(401)
def handle401(error):
    response.set_header('WWW-Authenticate', 'Basic realm="Web translator"')
    return 'Access denied'

METHODS = {'GET': 'read', 'POST': 'add', 'PUT': 'set', 'DELETE': 'del'}

def protected(page_name):
    """
    Decorator for adding basic authentication protection to a route.

    @param page_name: Name of the page being protected. Some of the parts may be
                      a pattern that has to be replaced with a real part when the
                      query is performed.
    @type  page_name: C{list} of C{str}
    """
    def decorator(func):
        def wrapper(*a, **ka):
            if request.auth is None:
                user = 'unknown'
            else:
                user, password = request.auth
                if not users.authenticate(user, password): user = 'unknown'
            pname = [ka.get(p, p) for p in page_name] + [METHODS.get(request.method, "-")]
            if not rights.may_access(pname, user):
                abort(401, "Access denied")
            return func(user, *a, **ka)
        return wrapper
    return decorator
