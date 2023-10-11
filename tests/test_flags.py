# encoding: utf-8
#
# main.py
import numpy as np
from pytest import mark

'''
from semaphore.flags import Flags


class TestFlags(object):

    @mark.parametrize(('N', ), [(i, ) for i in range(1, 100)])
    def test_flags(self, N, max_flag=10000):
        
        bits = np.unique(np.random.randint(1, max_flag, size=N))
        sorted_bits = np.sort(bits)
        unset_bits = tuple(set(range(1, max_flag)).difference(bits))

        # check type conversions                                
        
        #assert np.all(np.array(Flags(str(Flags(bits))).bits) == sorted_bits)
        #assert np.all(np.array(Flags(Flags(bits).data).bits) == sorted_bits)
        a = Flags()
        a.set_bits(*bits)
        assert np.all(np.array(a.bits) == sorted_bits)

        assert np.all(np.array(Flags.from_bits(a.bits).bits) == sorted_bits)
        assert np.all(np.array(Flags.from_hex(a.hex).bits) == sorted_bits)
        assert np.all(np.array(Flags.from_array(a.array).bits == sorted_bits))

        # TODO: not tested from_flags
        




        b = Flags()
        b.set_bits(*bits)

        assert np.all(np.array(b.bits) == sorted_bits)




        d = Flags()
        d.toggle_bits(*bits)
        assert np.all(np.array(d.bits) == sorted_bits)
        d.toggle_bits(*bits)
        assert len(d.bits) == 0

        
        e = Flags()
        e.toggle_bits(*bits)
        assert np.all(np.array(e.bits) == sorted_bits)
        e.toggle_bits(*bits)
        assert not e.are_any_bits_set(*range(1, max_flag))
        assert len(e.bits) == 0

        f = Flags()
        f.set_bits(*bits)
        assert f.are_all_bits_set(*bits)
        assert not f.are_any_bits_set(*unset_bits)

        g = Flags()
        g.set_bits(*bits)
        assert g.are_all_bits_set(*bits)
        g.clear_bits(*bits)
        assert not g.are_any_bits_set(*bits)




        g.__repr__()

''' 
