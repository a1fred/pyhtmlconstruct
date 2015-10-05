from core import Element

class form(Element):
    name = 'form'

class input(Element):
    allow_content = False
    self_closing = True
    ending_slash = True
    name = 'input'

class select(Element):
    name = 'select'

    allowed_childs = [
        'option'
    ]

class option(Element):
    name = 'option'

    allowed_childs = [
        'value'
    ]
