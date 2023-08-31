# encoding: utf-8
#
# main.py
import numpy as np
from pytest import mark

from semaphore.flags import Flags, FlagsArray


class TestFlags(object):

    @mark.parametrize(('N', ), [(i, ) for i in range(1, 100)])
    def test_flags(self, N, max_flag=10000):
        
        bits = np.unique(np.random.randint(1, max_flag, size=N))
        sorted_bits = np.sort(bits)
        unset_bits = tuple(set(range(1, max_flag)).difference(bits))

        a = Flags(bits)
        
        # Check that both are equal:
        assert np.all(np.array(a.bits) == sorted_bits)

        b = Flags()
        for bit in bits:
            b.set_bit(bit)

            assert b.is_set(bit)            
        
        assert np.all(np.array(b.bits) == sorted_bits)


        c = Flags()
        c.set_bits(*bits)
        assert np.all(np.array(c.bits) == sorted_bits)


        d = Flags()
        for bit in bits:
            d.set_bit(bit)
            assert d.is_set(bit)

            d.clear_bit(bit)
            assert not d.is_set(bit)

            d.toggle_bit(bit)
            assert d.is_set(bit)
            d.toggle_bit(bit)
            assert not d.is_set(bit)

        
        e = Flags()
        e.toggle_bits(*bits)
        assert np.all(np.array(e.bits) == sorted_bits)
        e.toggle_bits(*bits)
        assert not e.are_any_set(*range(1, max_flag))
        assert len(e.bits) == 0

        f = Flags(bits)
        assert f.are_all_set(*bits)
        assert not f.are_any_set(*unset_bits)

        g = Flags(bits)
        g.set_bits(*bits)
        assert g.are_all_set(*bits)
        g.clear_bits(*bits)
        assert not g.are_any_set(*bits)


        # check type conversions                                
        assert np.all(np.array(Flags(str(Flags(bits))).bits) == sorted_bits)
        assert np.all(np.array(Flags(Flags(bits).data).bits) == sorted_bits)