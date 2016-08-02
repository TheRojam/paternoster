# -*- coding: utf-8 -*-

import pytest


@pytest.mark.parametrize("value,valid", [
    ("uberspace.de", True),
    ("foo.google", True),
    (u"foobär.com", True),
    ("uberspace.deee", False),
    ("-bla.com", False),
    ("a42'.com", False),
    ("a" * 65 + ".com", False),
    (("a" * 40 + '.') * 8 + "com", False),
])
def test_type_domain(value, valid):
  from ..types import domain

  if not valid:
    with pytest.raises(ValueError):
      domain(value)
  else:
    domain(value)


@pytest.mark.parametrize("param,value,valid", [
    ("a-z", "aaaaaabb", True),
    ("a-z", "aaaaaabb2", False),
    ("b", "bbbb", True),
    ("b", "a", False),
    ("a-z0-9", "aaaaaabb2", True),
])
def test_type_restricted_str(param, value, valid):
  from ..types import restricted_str

  check = restricted_str(param)

  if not valid:
    with pytest.raises(ValueError):
      check(value)
  else:
    check(value)