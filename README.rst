==============================
  RST to semantic HTML5 Writer
==============================

Originally written to power `my blog`__, this project grew out of my
tiredness with the crappy HTML produced by `reStructuredText`__'s
default writers.

__ https://github.com/bradleywright/intranation.com
__ http://docutils.sourceforge.net/rst.html

Basically I didn't want to see HTML like:

::

  <div class="section" id="my-section-name">...</div>

when HTML5 has perfectly good semantics for that:

::

  <section id="my-section-name">..</section>

as a basic example.
