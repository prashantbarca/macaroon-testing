#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 prashant <prashant@prashant-Geekpad>
#
# Distributed under terms of the MIT license.

"""

"""

import time
from Crypto.Cipher import AES
from macaroon import Macaroon
from macaroon import Caveat
import random


start_time = time.time()

r = random.SystemRandom()
key = r.getrandbits(32)
m = Macaroon(1,key)
cav = Caveat("Issuer = Utility")
m.add_cav(cav)
cav = Caveat("Recipient = Smart Meter")
m.add_cav(cav)
cav = Caveat("Valid till : Feb 1 2017")
m.add_cav(cav)
end_time = time.time()
print end_time-start_time

start_time = time.time()
m.verify(key)
print time.time()-start_time

