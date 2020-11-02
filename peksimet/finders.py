import logging
import re
try:
    import regex
except ImportError:
    regex = re

PERCENTAGE = regex.compile(r'''(?:\s|\||\s\(|:\s|}})\s?(?:-?|\+?|<?|>?|~?|±?|–?|∓?|≈?|≤?|≥?)\s?
(([0-9]+)(\.?|,?)([0-9]*)( ?\%| ?‰)|(\% ?|(?:Y|y)üzde ?|‰ ?|(?:B|b)inde ?)([0-9]+)(\.?|,?)([0-9]*))
(?:\s|\||\)|:|,|'|’|}}|\s?-\s?)'''.replace('\n', ''))
