#!/usr/bin/env python
#
# Copyright 2014 Quantopian, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Dual Moving Average Crossover algorithm.

This algorithm buys apple once its short moving average crosses
its long moving average (indicating upwards momentum) and sells
its shares once the averages cross again (indicating downwards
momentum).
"""

from zipline.api import order_target, record, symbol
from collections import OrderedDict

def initialize(context):
    context.sym = symbol('F')
    context.i = 0
    context.dict = OrderedDict()
    context.els = list()


def handle_data(context, data):

    # Compute averages
    # history() has to be called with the same params
    # from above and returns a pandas dataframe.
        context.i+=1
        short_mavg = data.history(context.sym, 'price', 100, '1d').mean()
        long_mavg= data.history(context.sym, 'price', 300, '1d').mean()
        d = data.current(context.sym,'last_traded')
        context.els = list()
        context.els.append(d)
        if short_mavg > long_mavg:
            context.dict[d]="BUY"
            #print('BUY',d)
        elif short_mavg < long_mavg:
            context.dict[d]="SELL"
            #print('SELL',d)
        context.els.append(context.dict[d])

def analyze(context=None, results=None):
            print(context.els[0],context.els[1])
