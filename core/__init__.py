from core.exceptions import ElementNotAllowed


class Element:
    name = None
    self_closing = False # Allow element to self-close ( <element/> )
    allow_content = True # Allow inner text in element
    ending_slash = False # /> or >

    allowed_attrs = []
    allowed_childs = []

    def _get_allowed_attrs(self):
        default_attrs = [
            "class",
        ]

        return default_attrs + self.allowed_attrs

    def _get_allowed_childs(self):
        return self.allowed_childs

    def check_allowed_attrs(self):
        allowed = self._get_allowed_attrs()
        for attr in self.attrs.keys():
            if attr not in allowed:
                raise AttributeError("Attribute '%s' not allowed to use in element '%s'" %(attr, self.name))

    def check_allowed_childs(self):
        allowed = self._get_allowed_childs()
        for child in self.childs:
            if isinstance(child, Element):
                if child.name not in allowed:
                    raise ElementNotAllowed("Element '%s' not allowed in '%s'" % (child.name, self.name))

    def __init__(self, childs=None, attrs=None, ):
        if not self.allow_content and childs:
            raise ElementNotAllowed("Childs in element '%s' is not allowed." % self.name)

        self.attrs = attrs or {}

        if not hasattr(childs, "__iter__"):
            if childs:
                self.childs = [childs, ]
            else:
                self.childs = []
        else:
            self.childs = childs

        self.check_allowed_attrs()
        self.check_allowed_childs()

    def _get_attrs_string(self):
        return " ".join([ "%s=\"%s\"" % (k,str(v).replace('"', "'")) for k,v in self.attrs.items() ])

    def _open(self):
        attrs = self._get_attrs_string()
        return "<"+ " ".join([self.name, attrs]).strip() + ">"

    def _content(self):
        res = ""
        for element in self.childs:
            res += element.render() if isinstance(element, Element) else str(element)
        return res

    def _end(self):
        return "</{name}>".format(name=self.name)


    def render(self):
        content = self._content()

        if self.self_closing:
            if not content:
                attrs = self._get_attrs_string()
                return "<"+ " ".join([self.name, attrs]).strip() + (" />" if self.ending_slash else ">")

        return "{start}{el_el}{end}".format(
            start= self._open(),
            el_el= self._content(),
            end= self._end(),
        )
