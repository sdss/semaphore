# encoding: utf-8
#
# main.py
import numpy as np
from pytest import mark

from semaphore.flags import Flags, FlagsArray


class TestFlags(object):

    @mark.parameterize(('N', ), map(list, range(1, 1000)))
    def test_flag_data(self, N):

        bits = np.unique(np.random.randint(1, 10000, size=N))
        sorted_bits = np.sort(bits)
        a = Flags(bits)
        
        # Check that both are equal:
        assert np.all(np.array(a.bits) == sorted_bits)

        b = Flags()
        for bit in bits:
            b.set(bit)
        
        assert np.all(np.array(b.bits) == sorted_bits)




        
