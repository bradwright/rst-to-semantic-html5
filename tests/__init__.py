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

if __name__ == '__main__':
    unittest.main()
