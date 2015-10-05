import unittest
from core import ElementNotAllowed
import html

class HtmlTests(unittest.TestCase):
    def test_a(self):
        self.assertEqual(html.text.a(attrs={"href": "#"}).render(), "<a href=\"#\"></a>")
        self.assertEqual(html.text.a(attrs={"href": "#"}, childs=None).render(), "<a href=\"#\"></a>")
        self.assertEqual(html.text.a(attrs={"href": "#"}, childs=["Hello", ]).render(), "<a href=\"#\">Hello</a>")
        self.assertEqual(html.text.a(attrs={"href": "#"}, childs="Hello").render(), "<a href=\"#\">Hello</a>")

        self.assertEqual(
            html.text.a(attrs={"href": "#"}, childs=[
                html.text.p(["HelloWorld", ])
            ]).render(),
            "<a href=\"#\"><p>HelloWorld</p></a>"
        )

    def test_br(self):
        self.assertEqual(html.text.br().render(), "<br>")
        self.assertRaises(ElementNotAllowed, lambda: html.text.br("asd"))

    def test_input(self):
        self.assertEqual(html.form.input().render(), "<input />")
        self.assertRaises(ElementNotAllowed, lambda: html.form.input("asd"))

