import unittest
from html5writer.html5writer import SemanticHTML5Writer
from docutils.core import publish_parts

def text_to_rst(text):
    parts = publish_parts(writer=SemanticHTML5Writer(), source=text)
    return parts['fragment'].strip()

class TestNoDivSection(unittest.TestCase):
    def test_div(self):
        in_text = """Lorem ipsem dolor sit amet"""
        out_text = u"""<p>Lorem ipsem dolor sit amet</p>"""
        self.assertEqual(text_to_rst(in_text), out_text)


class TestCodeElements(unittest.TestCase):
    def test_inline_code(self):
        in_text = """``code here``"""
        out_text = u"""<p><code>code here</code></p>"""
        self.assertEqual(text_to_rst(in_text), out_text)


class TestCustomInlineElements(unittest.TestCase):
    def test_kbd_element(self):
        in_text = """:kbd:`sudo`"""
        out_text = u"""<p><kbd>sudo</kbd></p>"""
        self.assertEqual(text_to_rst(in_text), out_text)

    def test_abbr_element(self):
        in_text = """:abbr:`lol (laugh out loud)`"""
        out_text = u"""<p><abbr title="laugh out loud">lol</abbr></p>"""
        self.assertEqual(text_to_rst(in_text), out_text)


class TestLinkElements(unittest.TestCase):
    def test_external_link(self):
        in_text = """A link `goes here`__

__ http://google.com"""
        out_text = u"""<p>A link <a href="http://google.com" rel="external">goes here</a></p>"""
        self.assertEqual(text_to_rst(in_text), out_text)

    def test_internal_link(self):
        in_text = """A link `goes here`__

__ /something"""
        out_text = u"""<p>A link <a href="/something">goes here</a></p>"""
        self.assertEqual(text_to_rst(in_text), out_text)

if __name__ == '__main__':
    unittest.main()
