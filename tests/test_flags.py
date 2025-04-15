# encoding: utf-8
#
# main.py
import numpy as np
from pytest import mark, raises
from unittest import mock
from pathlib import Path
import contextlib
import os
import sys
from astropy.table import Table


from sdss_semaphore.targeting import TargetingFlags
from sdss_semaphore import BaseFlags, cached_class_property
from sdss_semaphore.targeting import BaseTargetingFlags


class TestFlags(object):

    @mark.parametrize(('N', ), [(i, ) for i in range(1, 100)])
    def test_flags(self, N, max_flag=10000):
        
        bits = np.unique(np.random.randint(1, max_flag, size=N))
        sorted_bits = np.sort(bits)
        unset_bits = tuple(set(range(1, max_flag)).difference(bits))

        # check type conversions                                
        
        #assert np.all(np.array(Flags(str(Flags(bits))).bits) == sorted_bits)
        #assert np.all(np.array(Flags(Flags(bits).data).bits) == sorted_bits)
        a = TargetingFlags()
        for bit in bits:
            a.set_bit(0,bit)

        assert np.all(np.where(a.as_boolean_array())[1] == sorted_bits)
        assert(np.all(np.where(TargetingFlags(a.array).as_boolean_array()[0]) == sorted_bits))
        


        b = TargetingFlags()
        for bit in bits:
            b.toggle_bit(0,bit)
        assert np.all(np.where(b.as_boolean_array()[0])[0] == sorted_bits)
        for bit in bits:
            b.toggle_bit(0,bit)
        b.as_boolean_array()[0]
        np.where(b.as_boolean_array())[0]
        assert not b.are_any_bits_set(0)


        c = TargetingFlags()
        for bit in bits:
            c.toggle_bit(0,bit)
        assert c.are_all_bits_set(*bits)
        assert not c.are_any_bits_set(*unset_bits)

        d = TargetingFlags()
        for bit in bits:
            d.set_bit(0,bit)

        for bit in bits:
            d.clear_bit(0, bit)
        assert not d.are_any_bits_set(*bits)

        e = TargetingFlags()
        mapping = Table.read(os.path.join(e.MAPPING_PATH,e.MAPPING_BASENAME))
        random_row = mapping[np.random.randint(len(mapping))]
        random_pk = random_row['carton_pk']
        e.set_bit_by_carton_pk(0,random_pk)
        assert np.all(e.are_all_bits_set(mapping[mapping['carton_pk'] == random_pk]['bit'].data))
        assert np.all(e.in_carton_label(mapping[mapping['carton_pk'] == random_pk]['label'].data))
        assert np.all(e.in_carton_name(mapping[mapping['carton_pk'] == random_pk]['name'].data))
        assert np.all(e.in_alt_name(mapping[mapping['carton_pk'] == random_pk]['alt_name'].data))
        assert np.all(e.in_carton_pk(mapping[mapping['carton_pk'] == random_pk]['carton_pk'].data))
        assert np.all(e.in_mapper(mapping[mapping['carton_pk'] == random_pk]['mapper'].data))
        assert np.all(e.in_program(mapping[mapping['carton_pk'] == random_pk]['program'].data))
        assert np.all(e.in_alt_program(mapping[mapping['carton_pk'] == random_pk]['alt_program'].data))

        assert set(e.get_carton_pk()[0]) == set(np.atleast_1d(random_row['carton_pk']))
        assert set(e.get_carton_label()[0]) == set(np.atleast_1d(random_row['label']))
        assert set(e.get_carton_name()[0]) == set(np.atleast_1d(random_row['name']))
        assert set(e.get_alt_name()[0]) == set(np.atleast_1d(random_row['alt_name']))
        assert set(e.get_mapper()[0]) == set(np.atleast_1d(random_row['mapper']))
        assert set(e.get_program()[0]) == set(np.atleast_1d(random_row['program']))
        assert set(e.get_alt_program()[0]) == set(np.atleast_1d(random_row['alt_program']))

        assert set(e.all_mappers) == set(mapping['mapper'].data)
        assert set(e.all_programs) == set(mapping['program'].data)
        assert set(e.all_alt_programs) == set(mapping['alt_program'].data)
        assert set(e.all_carton_names) == set(mapping['name'].data)
        assert set(e.all_alt_carton_names) == set(mapping['alt_name'].data)

        counts = e.count(skip_empty=True)
        assert isinstance(counts, dict)

        for label in np.atleast_1d(random_row['label']):
            assert label in counts
            assert counts[label] == 1

        counts = e.count()
        for label in np.atleast_1d(mapping['label'].data):
            assert label in counts
            if label in np.atleast_1d(random_row['label']):
                assert counts[label] == 1      
            else:
                assert counts[label] == 0    


        f = TargetingFlags(sdssc2bv=-1)


class TestMapping(BaseTargetingFlags):
    pass
def test_base_mapping_basename_raises():
    with raises(NotImplementedError, match="`_MAPPING_BASENAME` must be defined in subclass"):
        #del TestMapping._MAPPING_BASENAME
        _ = TestMapping._MAPPING_BASENAME
    with raises(NotImplementedError, match="`version` must be defined in subclass"):
        #del TestMapping.version
        _ = TestMapping.version
    with raises(NotImplementedError, match="`ver_name` must be defined in subclass"):
        #del TestMapping._ver_name
        _ = TestMapping._ver_name



@mark.parametrize("python_version, files_function", [
    ('3.7', 'side_effect'),  # Simulate older Python versions where files() fails
    ('3.8', 'side_effect'),
    ('3.9', 'normal')        # Simulate working files() in Python 3.9+
])
def test_get_mapping_path(python_version, files_function):
    mock_file = "/mocked/fallback/path/sdss5_target_1_with_groups.csv"

    with contextlib.ExitStack() as stack:
        # Conditionally patch `importlib.resources.files` if it exists
        if hasattr(sys.modules['importlib.resources'], 'files'):
            if files_function == 'side_effect':
                stack.enter_context(
                    mock.patch("importlib.resources.files", side_effect=AttributeError)
                )
            else:
                mock_files = mock.MagicMock()
                mock_files.joinpath.return_value = Path(mock_file)
                stack.enter_context(
                    mock.patch("importlib.resources.files", return_value=mock_files)
                )

        # Always patch `resources.path`
        mock_path = stack.enter_context(
            mock.patch("importlib.resources.path")
        )

        # Mock the context manager returned by path()
        mock_ctx = mock.MagicMock()
        mock_ctx.__enter__.return_value = mock_file
        mock_path.return_value = mock_ctx

        # Patch os.path.exists to always return True
        stack.enter_context(
            mock.patch("os.path.exists", return_value=True)
        )

        # Now run the test logic
        g = TargetingFlags(sdssc2bv=1)

        assert g.MAPPING_PATH == os.path.dirname(mock_file)
        assert g.MAPPING_BASENAME == "sdss5_target_1_with_groups.csv"
