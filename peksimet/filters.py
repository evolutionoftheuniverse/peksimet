# -*- coding: utf-8 -*-
"""
Custom filter functions to avoid unhappy inappropriateness
"""

#peksimet (c) by evolutionoftheuniverse
#
#peksimet is licensed under a
#Creative Commons Attribution-NonCommercial 4.0 International License.
#
#You should have received a copy of the license along with this
#work. If not, see <http://creativecommons.org/licenses/by-nc/4.0/>.

import logging
import warnings
import re
try:
    import regex
except ImportError:
    regex = re

LOGGER = logging.getLogger(__name__)

TAG_REF = regex.compile(r'(<ref[^>]*>|<\/ref>)')

def filter_ref(text, expr_start, expr_end):
    """Expression check between ref tags."""
    if expr_end < expr_start:
        raise ValueError('expr_end must be bigger than expr_start')
    match = TAG_REF.finditer(text)
    start = None
    end = None
    count = 0
    for i in match:
        try:
            LOGGER.debug('Ref tag %s found between %d:%d', i.group(1), i.start(), i.end())
            if i.group(1).endswith('/>'):
                continue
            if count % 2 == 0:
                start = i.end() if i.group(1).startswith('<ref') and i.group(1).endswith('>') else None
            elif count % 2 != 0:
                end = i.start() if i.group(1) == '</ref>' else None
            if not start or not end:
                LOGGER.debug('Problematic ref tag on text near %s %d:%d, continued', i.group(1), i.start(), i.end())
                warnings.warn(format('Problematic ref tag on text near {g} {s}:{e}, continued', g=i.group(1), s=i.start(), e=i.end()), SyntaxWarning)
                continue
            elif start and end and expr_start >= start and expr_end <= end:
                LOGGER.debug('A ref tag match found between %d:%d', start, end)
                return True
            elif start and end and expr_end >= end:
                LOGGER.debug('No ref tag match found between %d:%d, out of range', expr_start, expr_end)
                return False
        except ValueError:
            LOGGER.debug('Value error in ref tag: %s', i.group(1))
        count += 1
    LOGGER.debug('No ref tag found' if count == 0 else 'No ref tag match found between %d:%d', expr_start, expr_end)
    return False
