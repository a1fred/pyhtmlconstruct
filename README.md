# pyhtmlconstruct
Set of object to easy generate valid html.

# Example

```python
    from pyhtmlconstruct import html

    >>> print html.text.a("Hello World", attrs={"href": "#"},)
    <a href="#">Hello World</a>
```

# TODO
Add html elements with validation rules.
Using
[this](http://www.standardista.com/html5/xhtml-elements-their-parent-children-attributes-and-default-browser-presentation/)
as handbook.
