from core import Element

class html(Element):
    name = 'html'

    allowed_attrs = [
        'xmlns'
    ]

    allowed_childs = [
        'head',
        'body',
    ]

class head(Element):
    name = 'head'

    allowed_attrs = [
        'profile',
        'id',
        'dir',
        'lang',
    ]

    allowed_childs = [
        'base',
        'link',
        'meta',
        'style',
        'script',
        'title',
    ]

class body(Element):
    name = 'body'

    allowed_childs = [
        'script'
    ]

class base(Element):
    name = "base"

    allowed_attrs = [
        'href'
    ]

class link(Element):
    name='link'

    allowed_attrs = [
        'href',
        'charset',
        'hreflang',
        'type',
        'rel',
        'rev',
        'media',
    ]

class meta(Element):
    name='meta'

    allowed_attrs = [
        'content',
        'name',
        'http-equiv',
        'scheme',
    ]

class style(Element):
    name = 'style'

    allowed_attrs = [
        'type',
        'media'
    ]

class script(Element):
    name = 'script'

    allowed_attrs = [
        'src',
        'charset',
        'async',
        'defer',
        'type'
    ]

class title(Element):
    name = 'title'

    allowed_attrs = [
        'id',
        'dir',
        'lang',
    ]