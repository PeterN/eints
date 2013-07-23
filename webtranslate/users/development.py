"""
User administration system to use during development.

In particular the user management is very poor.
"""
from webtranslate import rights
from webtranslate.users import silly

def init():
    """
    Initialize the user admin system.
    """
    silly.init()
    rights.init_page_access()
    rights.init_projects()

def may_access(user, pwd, pname, prjname, lngname):
    """
    May a user access a page?

    @param user: Name of the user, if provided (external data).
    @type  user: C{str} or C{None}

    @param pwd: Password of the user, if provided (external data).
    @type  pwd: C{str} or C{None}

    @param pname: Page name being accessed.
    @type  pname: C{list} of C{str}

    @param prjname: Project name of the page, if any.
    @type  prjname: C{str} or C{None}

    @param lngname: Language name of the page, if any.
    @type  lngname: C{str} or C{None}

    @return: Whether the user may access the page.
    @rtype:  C{bool}
    """
    if user is None or pwd is None or not silly.authenticate(user, pwd):
        user = "unknown"

    return rights.may_access(pname, prjname, lngname, user)