from core import Element

class a(Element):
    name = "a"

    allowed_attrs = [
        'href',
        'hreflang',
        'rel',
        'charset',
        'type',
        'name',
        'rel',
        'rev',
        'shape',
        'coords',
        'rect',
    ]

    allowed_childs = [
        "p"
    ]

class abbr(Element):
    name = 'abbr'

    allowed_attrs = [
        'title'
    ]

class acronym(Element):
    name = 'acronym'

    allowed_attrs = [
        'title'
    ]


class address(Element):
    name = 'acronym'

    allowed_childs = [
        'p'
    ]

class p(Element):
    name = "p"

class br(Element):
    self_closing = True
    allow_content = False
    name = "br"
