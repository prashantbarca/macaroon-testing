#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 prashant <prashant@prashant-Geekpad>
#
# Distributed under terms of the MIT license.

"""

"""

class AttrCert:
    def __init__(self,v,h,i,s,sno,valid,attr,sign):
        self.version = v
        self.holder = h
        self.issuer = i
        self.signalg = s
        self.sno = sno
        self.validity = valid
        self.attr = attr
        self.signature = sign
        

from Crypto.PublicKey import RSA

key = RSA.generate(2048)
print key.publickey

print key.encrypt("Meh",None)
