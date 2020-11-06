# -*- coding: utf-8 -*-
"""
Custom functions to find numerical expressions
"""

#peksimet (c) by evolutionoftheuniverse
#
#peksimet is licensed under a
#Creative Commons Attribution-NonCommercial 4.0 International License.
#
#You should have received a copy of the license along with this
#work. If not, see <http://creativecommons.org/licenses/by-nc/4.0/>.

import logging
import re
try:
    import regex
except ImportError:
    regex = re

LOGGER = logging.getLogger(__name__)

PERCENTAGE = regex.compile(r'''(?:\s|\||\s\(|:\s|}})\s?(?:-?|\+?|<?|>?|~?|±?|–?|∓?|≈?|≤?|≥?)\s?
(([0-9]+)(\.?|,?)([0-9]*)( ?\%| ?‰)|(\% ?|(?:Y|y)üzde ?|‰ ?|(?:B|b)inde ?)([0-9]+)(\.?|,?)([0-9]*))
(?:\s|\||\)|:|,|'|’|}}|\s?-\s?)'''.replace('\n', ''))
    
def find_percentage(text):
    """Find percentages in text."""
    match = PERCENTAGE.finditer(text)
    result = ()
    for i in match:
        try:
            LOGGER.debug('Percentage %s have found between %d:%d', i.group(), i.start(), i.end())
            result += (i.groups() + (i.group(), ) + (i.start(), ) + (i.end(), ), )
        except ValueError:
            LOGGER.debug('Value error in percentage: %s', i.group())
    if result != ():
        return result
    return None
