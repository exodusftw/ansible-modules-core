#!/usr/bin/python
# -*- coding: utf-8 -*-

# (c) 2016, Jeremy Grant <jeremy.grant@outlook.com>
#
# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.

DOCUMENTATION = '''
---
module: validate
author: "Jeremy Grant (@exodusftw)"
version_added: 1.0
requirements: [ 're', 'yaml']
short_description: Methods for variable validation
description:
  - The M(validate) module provides a set of validation tools
    for variables. This is handled through a
    set of options to provide basic type enforcement,
    argument matching against a regular expression, integer range
    enforcement, and the ability to validate inputs
    against whitelist/blacklist entries.
options:
  blacklist:
    description:
      - List of user input values to reject
    required: false
    default: null
  input_type:
    description:
      - Required data type for input value - if passed, module will fail
        if data type provided by user does not match input_type passed
        to validate
    required: false
    choices: [ boolean, bool, str, string, array, list, hash, dict, int, long, float ]
    default: null
  matcher:
    description:
      - Regular expression to match against user input
        Expression should be passed as a string rather than I(/regex/)
    required: false
    default: null
  num_range:
    description:
      - Number Range to be used for validation
        against number vars - should be formatted as
        I(minimum-maximum) i.e. I(1-100)
    required: false
    default: null
  value:
    description:
      - User input variable to validate
    required: true
    default: null
  whitelist:
    description:
      - List of user input values to accept
    required: false
    default: null
'''

EXAMPLES = '''
# Basic input validation examples *assumes value field is user input var*

- name: validate boolean example with variable expansion
  validate:
  args:
    value: "{{ example_boolean_var }}"
    input_type: bool

- name: validate boolean stub variable
  validate:
  args:
    value: True
    input_type: bool

- name: validate stub integer variable range
  validate:
  args:
    value: 9
    num_range: '1-100'

- name: validate stub variable against regex
  validate:
  args:
    value: 'http://test.example.com/example/made-up-site'
    matcher: '^.*/example/.*$'

- name: validate stub variable against value whitelist
  validate:
  args:
    value: 'accepted_value1'
    whitelist:
      - 'accepted_value1'
      - 'accepted_value2'

- name: validate stub variable against value blacklist
  validate:
  args:
    value: 'rejected_value1'
    blacklist:
      - 'rejected_value1'
      - 'rejected_value2'
'''

RETURN = '''
---
pass:
  description: Returns a string containing the validation result
  returned: pass
  type: string
  sample: "PASS: Input value 'true' of type I(bool) matches validation requirement for value to be of type: I(bool)"
fail:
  description: Returns a string containing the validation result
  returned: fail
  type: string
  sample: "FAIL: Input value 'not_a_bool' of type I(str) does not match validation requirement for value to be of type: I(bool)"
'''
