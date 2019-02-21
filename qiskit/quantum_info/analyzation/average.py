# -*- coding: utf-8 -*-

# Copyright 2018, IBM.
#
# This source code is licensed under the Apache License, Version 2.0 found in
# the LICENSE.txt file in the root directory of this source tree.

"""A collection of useful functions for post processing results."""

import numpy as np


def average_data(counts, observable):
    """Compute the mean value of an diagonal observable.

    Takes in an observable in dictionary format and then
    calculates the sum_i value(i) P(i) where value(i) is the value of
    the observable for state i.

    TODO: make the observable also include a matrix

    Args:
        counts (dict): a dict of outcomes from an experiment
        observable (dict): The observable to be averaged over. As an example
        ZZ on qubits equals {"00": 1, "11": 1, "01": -1, "10": -1}

    Returns:
        Double: Average of the observable
    """
    temp = 0
    tot = sum(counts.values())
    counted_states = sorted(counts.keys())
    # Convert a matrix to dictionary
    if not isinstance(observable, dict):
        new_observable = {}
        observable = np.array(observable)
        # Create 1D array from diagonal if passed a matrix
        if observable.ndim == 2:
            observable = np.diagonal(observable)
        for state in counted_states:
            state_index = int(state, 2)
            new_observable[state] = observable[state_index]
        observable = new_observable
    # Perform summation
    for state in counted_states:
        temp += counts[state] * observable[state] / tot
    return temp
