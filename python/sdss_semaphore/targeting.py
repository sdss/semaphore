import numpy as np
from typing import Tuple
from sdss_semaphore import BaseFlags


class BaseTargetingFlags(BaseFlags):

    """A base class for communicating SDSS-V targeting information with flags."""

    @property
    def all_mappers(self) -> Tuple[str]:
        """Return a tuple of all mappers."""
        return self._all_attributes("mapper")
    
    @property
    def all_programs(self) -> Tuple[str]:
        """Return a list of all programs."""
        return self._all_attributes("program")
    
    
    @property
    def all_names(self) -> Tuple[str]:
        """Return a list of all carton names."""
        return self._all_attributes("name")
    
    @property
    def all_alt_names(self) -> Tuple[str]:
        """Return a list of all alternative carton names."""
        return self._all_attributes("alt_name")

    @property
    def all_alt_programs(self) -> Tuple[str]:
        """Return a list of all alternative carton programs."""
        return self._all_attributes("alt_program")
        

    def in_carton_pk(self, carton_pk: int) -> np.array:
        """
        Return an N-length boolean array indicating whether the items are assigned to the carton with the given primary key.

        :param carton_pk:
            The carton primary key.            
        """
        return self.is_attribute_set("carton_pk", carton_pk)

    def in_carton_name(self, name) -> np.array:
        """
        Return an N-length boolean array indicating whether the items are assigned to a carton with the given name.
        
        :param name:
            The flag name.
        """
        return self.is_attribute_set("name", name)

    def in_mapper(self, mapper) -> np.array:
        """
        Return an N-length boolean array indicating whether the items are assigned to any cartons with the given mapper.
        
        :param mapper:
            The mapper name.
        """
        return self.is_attribute_set("mapper", mapper)

    def in_program(self, program) -> np.array:
        """
        Return an N-length boolean array indicating whether the items are assigned to any cartons with the given program.
        
        :param program:
            The program name.
        """
        return self.is_attribute_set("program", program)
    
    def in_alt_name(self, alt_name) -> np.array:
        """
        Return an N-length boolean array indicating whether the items are assigned to any cartons with the given alternative name.

        :param alt_name:
            The alternative flag name.
        """
        return self.is_attribute_set("alt_name", alt_name)        

    def in_alt_program(self, alt_program) -> np.array:
        """
        Return an N-length boolean array indicating whether the items are assigned to any cartons with the given alternative program.

        :param alt_program:
            The alternative program name.
        """
        return self.is_attribute_set("alt_program", alt_program)

    def count(self, skip_empty: bool = False) -> dict:
        """
        Return a dictionary containing the number of items assigned by each carton label.

        :param skip_empty: [optional]
            Skip cartons with no items assigned to them.
        
        :returns:
            A dictionary with carton labels as keys and item counts as values.
        """
        return self._count(
            { attrs["label"]: [bit] for bit, attrs in self.mapping.items() }, 
            skip_empty=skip_empty
        )


class TargetingFlags(BaseTargetingFlags):

    """Communicating with SDSS-V targeting flags."""

    dtype, n_bits = (np.uint8, 8)
    meta = { "SDSSC2BV": 1.0 }
    mapping = {
        1: {'label': 'mwm_snc_100pc_0.1.0', 'carton_pk': 126, 'program': 'mwm_snc', 'version': '0.1.0', 'v1': 1.0, 'name': 'mwm_snc_100pc', 'mapper': 'mwm', 'alt_program': 'snc', 'alt_name': 'mwm_snc'},
        2: {'label': 'mwm_snc_250pc_0.1.0', 'carton_pk': 127, 'program': 'mwm_snc', 'version': '0.1.0', 'v1': 1.0, 'name': 'mwm_snc_250pc', 'mapper': 'mwm', 'alt_program': 'snc', 'alt_name': 'mwm_snc'},
        3: {'label': 'mwm_cb_300pc_0.1.0', 'carton_pk': 128, 'program': 'mwm_cb', 'version': '0.1.0', 'v1': 1.0, 'name': 'mwm_cb_300pc', 'mapper': 'mwm', 'alt_program': 'cb', 'alt_name': 'mwm_cb_300pc'},
        4: {'label': 'mwm_cb_cvcandidates_0.1.0', 'carton_pk': 134, 'program': 'mwm_cb', 'version': '0.1.0', 'v1': 1.0, 'name': 'mwm_cb_cvcandidates', 'mapper': 'mwm', 'alt_program': 'cb', 'alt_name': 'mwm_cb_cvcandidates'},
        5: {'label': 'mwm_halo_sm_0.1.0', 'carton_pk': 140, 'program': 'mwm_halo', 'version': '0.1.0', 'v1': 1.0, 'name': 'mwm_halo_sm', 'mapper': 'mwm', 'alt_program': 'halo', 'alt_name': 'mwm_halo_sm'},
        6: {'label': 'mwm_halo_bb_0.1.0', 'carton_pk': 143, 'program': 'mwm_halo', 'version': '0.1.0', 'v1': 1.0, 'name': 'mwm_halo_bb', 'mapper': 'mwm', 'alt_program': 'halo', 'alt_name': 'mwm_halo_bb'},
        7: {'label': 'mwm_yso_s1_0.1.0', 'carton_pk': 144, 'program': 'mwm_yso', 'version': '0.1.0', 'v1': 1.0, 'name': 'mwm_yso_s1', 'mapper': 'mwm', 'alt_program': 'yso', 'alt_name': 'mwm_yso_disk'},
        8: {'label': 'mwm_yso_s2_0.1.0', 'carton_pk': 145, 'program': 'mwm_yso', 'version': '0.1.0', 'v1': 1.0, 'name': 'mwm_yso_s2', 'mapper': 'mwm', 'alt_program': 'yso', 'alt_name': 'mwm_yso_embedded'},
        9: {'label': 'mwm_yso_s2-5_0.1.0', 'carton_pk': 146, 'program': 'mwm_yso', 'version': '0.1.0', 'v1': 1.0, 'name': 'mwm_yso_s2-5', 'mapper': 'mwm', 'alt_program': 'yso', 'alt_name': 'mwm_yso_nebula'},
        10: {'label': 'mwm_yso_s3_0.1.0', 'carton_pk': 147, 'program': 'mwm_yso', 'version': '0.1.0', 'v1': 1.0, 'name': 'mwm_yso_s3', 'mapper': 'mwm', 'alt_program': 'yso', 'alt_name': 'mwm_yso_variable'},
        11: {'label': 'mwm_yso_ob_0.1.0', 'carton_pk': 148, 'program': 'mwm_yso', 'version': '0.1.0', 'v1': 1.0, 'name': 'mwm_yso_ob', 'mapper': 'mwm', 'alt_program': 'yso', 'alt_name': 'mwm_yso_ob'},
        12: {'label': 'mwm_yso_cmz_0.1.0', 'carton_pk': 149, 'program': 'mwm_yso', 'version': '0.1.0', 'v1': 1.0, 'name': 'mwm_yso_cmz', 'mapper': 'mwm', 'alt_program': 'yso', 'alt_name': 'mwm_yso_cmz'},
        13: {'label': 'mwm_yso_cluster_0.1.0', 'carton_pk': 150, 'program': 'mwm_yso', 'version': '0.1.0', 'v1': 1.0, 'name': 'mwm_yso_cluster', 'mapper': 'mwm', 'alt_program': 'yso', 'alt_name': 'mwm_yso_cluster'},
        14: {'label': 'mwm_rv_long-fps_0.1.0', 'carton_pk': 158, 'program': 'mwm_rv', 'version': '0.1.0', 'v1': 1.0, 'name': 'mwm_rv_long-fps', 'mapper': 'mwm', 'alt_program': 'bin', 'alt_name': 'mwm_bin_rv_long'},
        15: {'label': 'mwm_rv_long-bplates_0.1.0', 'carton_pk': 160, 'program': 'mwm_rv', 'version': '0.1.0', 'v1': 1.0, 'name': 'mwm_rv_long-bplates', 'mapper': 'mwm', 'alt_program': 'bin', 'alt_name': 'mwm_bin_rv_long'},
        16: {'label': 'mwm_ob_cepheids_0.1.0', 'carton_pk': 163, 'program': 'mwm_ob', 'version': '0.1.0', 'v1': 1.0, 'name': 'mwm_ob_cepheids', 'mapper': 'mwm', 'alt_program': 'ob', 'alt_name': 'mwm_ob_cepheids'},
        17: {'label': 'mwm_rv_short-fps_0.1.0', 'carton_pk': 164, 'program': 'mwm_rv', 'version': '0.1.0', 'v1': 1.0, 'name': 'mwm_rv_short-fps', 'mapper': 'mwm', 'alt_program': 'bin', 'alt_name': 'mwm_bin_rv_short'},
        18: {'label': 'mwm_rv_short-bplates_0.1.0', 'carton_pk': 165, 'program': 'mwm_rv', 'version': '0.1.0', 'v1': 1.0, 'name': 'mwm_rv_short-bplates', 'mapper': 'mwm', 'alt_program': 'bin', 'alt_name': 'mwm_bin_rv_short'},
        19: {'label': 'mwm_ob_core_0.1.0', 'carton_pk': 236, 'program': 'mwm_ob', 'version': '0.1.0', 'v1': 1.0, 'name': 'mwm_ob_core', 'mapper': 'mwm', 'alt_program': 'ob', 'alt_name': 'mwm_ob_core'},
        20: {'label': 'mwm_rv_short-rm_0.1.0', 'carton_pk': 241, 'program': 'mwm_rv', 'version': '0.1.0', 'v1': 1.0, 'name': 'mwm_rv_short-rm', 'mapper': 'mwm', 'alt_program': 'bin', 'alt_name': 'mwm_bin_rv_short'},
        21: {'label': 'mwm_rv_long-rm_0.1.0', 'carton_pk': 242, 'program': 'mwm_rv', 'version': '0.1.0', 'v1': 1.0, 'name': 'mwm_rv_long-rm', 'mapper': 'mwm', 'alt_program': 'bin', 'alt_name': 'mwm_bin_rv_long'},
        22: {'label': 'ops_std_boss_0.1.0', 'carton_pk': 257, 'program': 'ops_std', 'version': '0.1.0', 'v1': 1.0, 'name': 'ops_std_boss', 'mapper': 'ops', 'alt_program': 'std', 'alt_name': 'ops_std'},
        23: {'label': 'mwm_wd_core_0.1.0', 'carton_pk': 259, 'program': 'mwm_wd', 'version': '0.1.0', 'v1': 1.0, 'name': 'mwm_wd_core', 'mapper': 'mwm', 'alt_program': 'wd', 'alt_name': 'mwm_wd'},
        24: {'label': 'mwm_gg_core_0.1.0', 'carton_pk': 273, 'program': 'mwm_gg', 'version': '0.1.0', 'v1': 1.0, 'name': 'mwm_gg_core', 'mapper': 'mwm', 'alt_program': 'galactic', 'alt_name': 'mwm_galactic_core'},
        25: {'label': 'mwm_planet_tess_0.1.0', 'carton_pk': 274, 'program': 'mwm_planet', 'version': '0.1.0', 'v1': 1.0, 'name': 'mwm_planet_tess', 'mapper': 'mwm', 'alt_program': 'planet', 'alt_name': 'mwm_tess_2min'},
        26: {'label': 'bhm_aqmes_med_0.1.0', 'carton_pk': 278, 'program': 'bhm_aqmes', 'version': '0.1.0', 'v1': 1.0, 'name': 'bhm_aqmes_med', 'mapper': 'bhm', 'alt_program': 'aqmes', 'alt_name': 'bhm_aqmes'},
        27: {'label': 'mwm_cb_gaiagalex_0.1.0', 'carton_pk': 279, 'program': 'mwm_cb', 'version': '0.1.0', 'v1': 1.0, 'name': 'mwm_cb_gaiagalex', 'mapper': 'mwm', 'alt_program': 'cb', 'alt_name': 'mwm_cb_galex'},
        28: {'label': 'bhm_aqmes_med-faint_0.1.0', 'carton_pk': 280, 'program': 'bhm_filler', 'version': '0.1.0', 'v1': 1.0, 'name': 'bhm_aqmes_med-faint', 'mapper': 'bhm', 'alt_program': 'filler', 'alt_name': 'bhm_aqmes'},
        29: {'label': 'mwm_tessrgb_core_0.1.0', 'carton_pk': 281, 'program': 'mwm_tessrgb', 'version': '0.1.0', 'v1': 1.0, 'name': 'mwm_tessrgb_core', 'mapper': 'mwm', 'alt_program': 'tessrgb', 'alt_name': 'mwm_tess_rgb'},
        30: {'label': 'bhm_aqmes_wide3_0.1.0', 'carton_pk': 286, 'program': 'bhm_aqmes', 'version': '0.1.0', 'v1': 1.0, 'name': 'bhm_aqmes_wide3', 'mapper': 'bhm', 'alt_program': 'aqmes', 'alt_name': 'bhm_aqmes'},
        31: {'label': 'bhm_aqmes_wide3-faint_0.1.0', 'carton_pk': 287, 'program': 'bhm_filler', 'version': '0.1.0', 'v1': 1.0, 'name': 'bhm_aqmes_wide3-faint', 'mapper': 'bhm', 'alt_program': 'filler', 'alt_name': 'bhm_aqmes'},
        32: {'label': 'bhm_aqmes_wide2_0.1.0', 'carton_pk': 288, 'program': 'bhm_aqmes', 'version': '0.1.0', 'v1': 1.0, 'name': 'bhm_aqmes_wide2', 'mapper': 'bhm', 'alt_program': 'aqmes', 'alt_name': 'bhm_aqmes'},
        33: {'label': 'bhm_aqmes_wide2-faint_0.1.0', 'carton_pk': 289, 'program': 'bhm_filler', 'version': '0.1.0', 'v1': 1.0, 'name': 'bhm_aqmes_wide2-faint', 'mapper': 'bhm', 'alt_program': 'filler', 'alt_name': 'bhm_aqmes'},
        34: {'label': 'bhm_aqmes_bonus-dark_0.1.0', 'carton_pk': 290, 'program': 'bhm_filler', 'version': '0.1.0', 'v1': 1.0, 'name': 'bhm_aqmes_bonus-dark', 'mapper': 'bhm', 'alt_program': 'filler', 'alt_name': 'bhm_aqmes'},
        35: {'label': 'bhm_aqmes_bonus-bright_0.1.0', 'carton_pk': 291, 'program': 'bhm_filler', 'version': '0.1.0', 'v1': 1.0, 'name': 'bhm_aqmes_bonus-bright', 'mapper': 'bhm', 'alt_program': 'filler', 'alt_name': 'bhm_aqmes'},
        36: {'label': 'bhm_csc_boss-dark_0.1.0', 'carton_pk': 307, 'program': 'bhm_csc', 'version': '0.1.0', 'v1': 1.0, 'name': 'bhm_csc_boss-dark', 'mapper': 'bhm', 'alt_program': 'csc', 'alt_name': 'bhm_csc'},
        37: {'label': 'bhm_csc_boss-bright_0.1.0', 'carton_pk': 308, 'program': 'bhm_csc', 'version': '0.1.0', 'v1': 1.0, 'name': 'bhm_csc_boss-bright', 'mapper': 'bhm', 'alt_program': 'csc', 'alt_name': 'bhm_csc'},
        38: {'label': 'bhm_csc_apogee_0.1.0', 'carton_pk': 309, 'program': 'bhm_csc', 'version': '0.1.0', 'v1': 1.0, 'name': 'bhm_csc_apogee', 'mapper': 'bhm', 'alt_program': 'csc', 'alt_name': 'bhm_csc'},
        39: {'label': 'bhm_gua_dark_0.1.0', 'carton_pk': 310, 'program': 'bhm_filler', 'version': '0.1.0', 'v1': 1.0, 'name': 'bhm_gua_dark', 'mapper': 'bhm', 'alt_program': 'filler', 'alt_name': 'bhm_filler'},
        40: {'label': 'bhm_gua_bright_0.1.0', 'carton_pk': 311, 'program': 'bhm_filler', 'version': '0.1.0', 'v1': 1.0, 'name': 'bhm_gua_bright', 'mapper': 'bhm', 'alt_program': 'filler', 'alt_name': 'bhm_filler'},
        41: {'label': 'ops_std_eboss_0.1.0', 'carton_pk': 319, 'program': 'ops_std', 'version': '0.1.0', 'v1': 1.0, 'name': 'ops_std_eboss', 'mapper': 'ops', 'alt_program': 'std', 'alt_name': 'ops_std'},
        42: {'label': 'ops_sky_apogee_0.1.0', 'carton_pk': 325, 'program': 'ops_sky', 'version': '0.1.0', 'v1': 1.0, 'name': 'ops_sky_apogee', 'mapper': 'ops', 'alt_program': 'sky', 'alt_name': 'ops_sky'},
        43: {'label': 'bhm_rm_core_0.1.0', 'carton_pk': 340, 'program': 'bhm_rm', 'version': '0.1.0', 'v1': 1.0, 'name': 'bhm_rm_core', 'mapper': 'bhm', 'alt_program': 'rm', 'alt_name': 'bhm_rm'},
        44: {'label': 'bhm_rm_known-spec_0.1.0', 'carton_pk': 341, 'program': 'bhm_rm', 'version': '0.1.0', 'v1': 1.0, 'name': 'bhm_rm_known-spec', 'mapper': 'bhm', 'alt_program': 'rm', 'alt_name': 'bhm_rm'},
        45: {'label': 'bhm_rm_var_0.1.0', 'carton_pk': 342, 'program': 'bhm_rm', 'version': '0.1.0', 'v1': 1.0, 'name': 'bhm_rm_var', 'mapper': 'bhm', 'alt_program': 'rm', 'alt_name': 'bhm_rm'},
        46: {'label': 'bhm_rm_ancillary_0.1.0', 'carton_pk': 343, 'program': 'bhm_rm', 'version': '0.1.0', 'v1': 1.0, 'name': 'bhm_rm_ancillary', 'mapper': 'bhm', 'alt_program': 'rm', 'alt_name': 'bhm_rm'},
        47: {'label': 'ops_std_boss-red_0.1.0', 'carton_pk': 351, 'program': 'ops_std', 'version': '0.1.0', 'v1': 1.0, 'name': 'ops_std_boss-red', 'mapper': 'ops', 'alt_program': 'std', 'alt_name': 'ops_std'},
        48: {'label': 'bhm_spiders_agn-efeds_0.1.0', 'carton_pk': 356, 'program': 'bhm_spiders', 'version': '0.1.0', 'v1': 1.0, 'name': 'bhm_spiders_agn-efeds', 'mapper': 'bhm', 'alt_program': 'spiders', 'alt_name': 'bhm_spiders'},
        49: {'label': 'bhm_spiders_clusters-efeds-sdss-redmapper_0.1.0', 'carton_pk': 357, 'program': 'bhm_spiders', 'version': '0.1.0', 'v1': 1.0, 'name': 'bhm_spiders_clusters-efeds-sdss-redmapper', 'mapper': 'bhm', 'alt_program': 'spiders', 'alt_name': 'bhm_spiders'},
        50: {'label': 'bhm_spiders_clusters-efeds-hsc-redmapper_0.1.0', 'carton_pk': 358, 'program': 'bhm_spiders', 'version': '0.1.0', 'v1': 1.0, 'name': 'bhm_spiders_clusters-efeds-hsc-redmapper', 'mapper': 'bhm', 'alt_program': 'spiders', 'alt_name': 'bhm_spiders'},
        51: {'label': 'bhm_spiders_clusters-efeds-ls-redmapper_0.1.0', 'carton_pk': 359, 'program': 'bhm_spiders', 'version': '0.1.0', 'v1': 1.0, 'name': 'bhm_spiders_clusters-efeds-ls-redmapper', 'mapper': 'bhm', 'alt_program': 'spiders', 'alt_name': 'bhm_spiders'},
        52: {'label': 'bhm_spiders_clusters-efeds-erosita_0.1.0', 'carton_pk': 360, 'program': 'bhm_spiders', 'version': '0.1.0', 'v1': 1.0, 'name': 'bhm_spiders_clusters-efeds-erosita', 'mapper': 'bhm', 'alt_program': 'spiders', 'alt_name': 'bhm_spiders'},
        53: {'label': 'mwm_cb_uvex1_0.1.0', 'carton_pk': 361, 'program': 'mwm_cb', 'version': '0.1.0', 'v1': 1.0, 'name': 'mwm_cb_uvex1', 'mapper': 'mwm', 'alt_program': 'cb', 'alt_name': 'mwm_cb_galex'},
        54: {'label': 'mwm_cb_uvex2_0.1.0', 'carton_pk': 362, 'program': 'mwm_cb', 'version': '0.1.0', 'v1': 1.0, 'name': 'mwm_cb_uvex2', 'mapper': 'mwm', 'alt_program': 'cb', 'alt_name': 'mwm_cb_galex'},
        55: {'label': 'mwm_dust_core_0.1.0', 'carton_pk': 363, 'program': 'mwm_dust', 'version': '0.1.0', 'v1': 1.0, 'name': 'mwm_dust_core', 'mapper': 'mwm', 'alt_program': 'dust', 'alt_name': 'mwm_dust_core'},
        56: {'label': 'mwm_cb_uvex3_0.1.0', 'carton_pk': 364, 'program': 'mwm_cb', 'version': '0.1.0', 'v1': 1.0, 'name': 'mwm_cb_uvex3', 'mapper': 'mwm', 'alt_program': 'cb', 'alt_name': 'mwm_cb_xmmom'},
        57: {'label': 'mwm_cb_uvex4_0.1.0', 'carton_pk': 366, 'program': 'mwm_cb', 'version': '0.1.0', 'v1': 1.0, 'name': 'mwm_cb_uvex4', 'mapper': 'mwm', 'alt_program': 'cb', 'alt_name': 'mwm_cb_swiftuvot'},
        58: {'label': 'mwm_cb_uvex5_0.1.0', 'carton_pk': 367, 'program': 'mwm_cb', 'version': '0.1.0', 'v1': 1.0, 'name': 'mwm_cb_uvex5', 'mapper': 'mwm', 'alt_program': 'cb', 'alt_name': 'mwm_cb_galex'},
        59: {'label': 'ops_sky_boss_0.1.0', 'carton_pk': 368, 'program': 'ops_sky', 'version': '0.1.0', 'v1': 1.0, 'name': 'ops_sky_boss', 'mapper': 'ops', 'alt_program': 'sky', 'alt_name': 'ops_sky'},
        60: {'label': 'mwm_legacy_ir2opt_0.1.1', 'carton_pk': 375, 'program': 'mwm_legacy', 'version': '0.1.1', 'v1': 1.01, 'name': 'mwm_legacy_ir2opt', 'mapper': 'mwm', 'alt_program': 'legacy', 'alt_name': 'mwm_legacy_ir2opt'},
        61: {'label': 'ops_apogee_stds_0.1.2', 'carton_pk': 376, 'program': 'ops_std', 'version': '0.1.2', 'v1': 1.02, 'name': 'ops_apogee_stds', 'mapper': 'ops', 'alt_program': 'std', 'alt_name': 'ops_std'},
        62: {'label': 'ops_std_boss_tic_0.1.3', 'carton_pk': 377, 'program': 'ops_std', 'version': '0.1.3', 'v1': 1.03, 'name': 'ops_std_boss_tic', 'mapper': 'ops', 'alt_program': 'std', 'alt_name': 'ops_std'},
        63: {'label': 'mwm_rv_long_bplates_0.1.4', 'carton_pk': 378, 'program': 'mwm_rv', 'version': '0.1.4', 'v1': 1.04, 'name': 'mwm_rv_long_bplates', 'mapper': 'mwm', 'alt_program': 'bin', 'alt_name': 'mwm_bin_rv_long'},
        64: {'label': 'ops_std_eboss_0.5.0', 'carton_pk': 529, 'program': 'ops_std', 'version': '0.5.0', 'v1': 5.0, 'name': 'ops_std_eboss', 'mapper': 'ops', 'alt_program': 'std', 'alt_name': 'ops_std'},
        65: {'label': 'ops_std_boss_0.5.0', 'carton_pk': 530, 'program': 'ops_std', 'version': '0.5.0', 'v1': 5.0, 'name': 'ops_std_boss', 'mapper': 'ops', 'alt_program': 'std', 'alt_name': 'ops_std'},
        66: {'label': 'ops_std_boss_red_0.5.0', 'carton_pk': 531, 'program': 'ops_std', 'version': '0.5.0', 'v1': 5.0, 'name': 'ops_std_boss_red', 'mapper': 'ops', 'alt_program': 'std', 'alt_name': 'ops_std'},
        67: {'label': 'ops_std_apogee_0.5.0', 'carton_pk': 532, 'program': 'ops_std', 'version': '0.5.0', 'v1': 5.0, 'name': 'ops_std_apogee', 'mapper': 'ops', 'alt_program': 'std', 'alt_name': 'ops_std'},
        68: {'label': 'mwm_cb_gaiagalex_apogee_0.5.0', 'carton_pk': 537, 'program': 'mwm_cb', 'version': '0.5.0', 'v1': 5.0, 'name': 'mwm_cb_gaiagalex_apogee', 'mapper': 'mwm', 'alt_program': 'cb', 'alt_name': 'mwm_cb_galex'},
        69: {'label': 'mwm_cb_gaiagalex_boss_0.5.0', 'carton_pk': 538, 'program': 'mwm_cb', 'version': '0.5.0', 'v1': 5.0, 'name': 'mwm_cb_gaiagalex_boss', 'mapper': 'mwm', 'alt_program': 'cb', 'alt_name': 'mwm_cb_galex'},
        70: {'label': 'mwm_cb_cvcandidates_apogee_0.5.0', 'carton_pk': 539, 'program': 'mwm_cb', 'version': '0.5.0', 'v1': 5.0, 'name': 'mwm_cb_cvcandidates_apogee', 'mapper': 'mwm', 'alt_program': 'cb', 'alt_name': 'mwm_cb_cvcandidates'},
        71: {'label': 'mwm_cb_cvcandidates_boss_0.5.0', 'carton_pk': 540, 'program': 'mwm_cb', 'version': '0.5.0', 'v1': 5.0, 'name': 'mwm_cb_cvcandidates_boss', 'mapper': 'mwm', 'alt_program': 'cb', 'alt_name': 'mwm_cb_cvcandidates'},
        72: {'label': 'mwm_galactic_core_0.5.0', 'carton_pk': 544, 'program': 'mwm_galactic', 'version': '0.5.0', 'v1': 5.0, 'name': 'mwm_galactic_core', 'mapper': 'mwm', 'alt_program': 'galactic', 'alt_name': 'mwm_galactic_core'},
        73: {'label': 'mwm_cb_uvex3_0.5.0', 'carton_pk': 547, 'program': 'mwm_cb', 'version': '0.5.0', 'v1': 5.0, 'name': 'mwm_cb_uvex3', 'mapper': 'mwm', 'alt_program': 'cb', 'alt_name': 'mwm_cb_xmmom'},
        74: {'label': 'mwm_cb_uvex4_0.5.0', 'carton_pk': 548, 'program': 'mwm_cb', 'version': '0.5.0', 'v1': 5.0, 'name': 'mwm_cb_uvex4', 'mapper': 'mwm', 'alt_program': 'cb', 'alt_name': 'mwm_cb_swiftuvot'},
        75: {'label': 'mwm_snc_100pc_boss_0.5.0', 'carton_pk': 551, 'program': 'mwm_snc', 'version': '0.5.0', 'v1': 5.0, 'name': 'mwm_snc_100pc_boss', 'mapper': 'mwm', 'alt_program': 'snc', 'alt_name': 'mwm_snc'},
        76: {'label': 'mwm_snc_250pc_apogee_0.5.0', 'carton_pk': 552, 'program': 'mwm_snc', 'version': '0.5.0', 'v1': 5.0, 'name': 'mwm_snc_250pc_apogee', 'mapper': 'mwm', 'alt_program': 'snc', 'alt_name': 'mwm_snc'},
        77: {'label': 'mwm_snc_250pc_boss_0.5.0', 'carton_pk': 553, 'program': 'mwm_snc', 'version': '0.5.0', 'v1': 5.0, 'name': 'mwm_snc_250pc_boss', 'mapper': 'mwm', 'alt_program': 'snc', 'alt_name': 'mwm_snc'},
        78: {'label': 'mwm_halo_sm_boss_0.5.0', 'carton_pk': 557, 'program': 'mwm_filler', 'version': '0.5.0', 'v1': 5.0, 'name': 'mwm_halo_sm_boss', 'mapper': 'mwm', 'alt_program': 'halo', 'alt_name': 'mwm_halo_sm'},
        79: {'label': 'mwm_yso_disk_apogee_0.5.0', 'carton_pk': 558, 'program': 'mwm_yso', 'version': '0.5.0', 'v1': 5.0, 'name': 'mwm_yso_disk_apogee', 'mapper': 'mwm', 'alt_program': 'yso', 'alt_name': 'mwm_yso_disk'},
        80: {'label': 'mwm_yso_disk_boss_0.5.0', 'carton_pk': 559, 'program': 'mwm_yso', 'version': '0.5.0', 'v1': 5.0, 'name': 'mwm_yso_disk_boss', 'mapper': 'mwm', 'alt_program': 'yso', 'alt_name': 'mwm_yso_disk'},
        81: {'label': 'mwm_yso_embedded_apogee_0.5.0', 'carton_pk': 560, 'program': 'mwm_yso', 'version': '0.5.0', 'v1': 5.0, 'name': 'mwm_yso_embedded_apogee', 'mapper': 'mwm', 'alt_program': 'yso', 'alt_name': 'mwm_yso_embedded'},
        82: {'label': 'mwm_yso_nebula_apogee_0.5.0', 'carton_pk': 561, 'program': 'mwm_yso', 'version': '0.5.0', 'v1': 5.0, 'name': 'mwm_yso_nebula_apogee', 'mapper': 'mwm', 'alt_program': 'yso', 'alt_name': 'mwm_yso_nebula'},
        83: {'label': 'mwm_yso_variable_apogee_0.5.0', 'carton_pk': 562, 'program': 'mwm_yso', 'version': '0.5.0', 'v1': 5.0, 'name': 'mwm_yso_variable_apogee', 'mapper': 'mwm', 'alt_program': 'yso', 'alt_name': 'mwm_yso_variable'},
        84: {'label': 'mwm_yso_variable_boss_0.5.0', 'carton_pk': 563, 'program': 'mwm_yso', 'version': '0.5.0', 'v1': 5.0, 'name': 'mwm_yso_variable_boss', 'mapper': 'mwm', 'alt_program': 'yso', 'alt_name': 'mwm_yso_variable'},
        85: {'label': 'mwm_yso_ob_apogee_0.5.0', 'carton_pk': 564, 'program': 'mwm_yso', 'version': '0.5.0', 'v1': 5.0, 'name': 'mwm_yso_ob_apogee', 'mapper': 'mwm', 'alt_program': 'yso', 'alt_name': 'mwm_yso_ob'},
        86: {'label': 'mwm_yso_ob_boss_0.5.0', 'carton_pk': 565, 'program': 'mwm_yso', 'version': '0.5.0', 'v1': 5.0, 'name': 'mwm_yso_ob_boss', 'mapper': 'mwm', 'alt_program': 'yso', 'alt_name': 'mwm_yso_ob'},
        87: {'label': 'mwm_yso_cmz_apogee_0.5.0', 'carton_pk': 566, 'program': 'mwm_yso', 'version': '0.5.0', 'v1': 5.0, 'name': 'mwm_yso_cmz_apogee', 'mapper': 'mwm', 'alt_program': 'yso', 'alt_name': 'mwm_yso_cmz'},
        88: {'label': 'mwm_yso_cluster_apogee_0.5.0', 'carton_pk': 567, 'program': 'mwm_yso', 'version': '0.5.0', 'v1': 5.0, 'name': 'mwm_yso_cluster_apogee', 'mapper': 'mwm', 'alt_program': 'yso', 'alt_name': 'mwm_yso_cluster'},
        89: {'label': 'mwm_yso_cluster_boss_0.5.0', 'carton_pk': 568, 'program': 'mwm_yso', 'version': '0.5.0', 'v1': 5.0, 'name': 'mwm_yso_cluster_boss', 'mapper': 'mwm', 'alt_program': 'yso', 'alt_name': 'mwm_yso_cluster'},
        90: {'label': 'mwm_rv_short_fps_0.5.0', 'carton_pk': 576, 'program': 'mwm_rv', 'version': '0.5.0', 'v1': 5.0, 'name': 'mwm_rv_short_fps', 'mapper': 'mwm', 'alt_program': 'bin', 'alt_name': 'mwm_bin_rv_short'},
        91: {'label': 'mwm_legacy_ir2opt_0.5.0', 'carton_pk': 580, 'program': 'mwm_legacy', 'version': '0.5.0', 'v1': 5.0, 'name': 'mwm_legacy_ir2opt', 'mapper': 'mwm', 'alt_program': 'legacy', 'alt_name': 'mwm_legacy_ir2opt'},
        92: {'label': 'mwm_dust_core_0.5.0', 'carton_pk': 583, 'program': 'mwm_dust', 'version': '0.5.0', 'v1': 5.0, 'name': 'mwm_dust_core', 'mapper': 'mwm', 'alt_program': 'dust', 'alt_name': 'mwm_dust_core'},
        93: {'label': 'mwm_wd_core_0.5.0', 'carton_pk': 585, 'program': 'mwm_wd', 'version': '0.5.0', 'v1': 5.0, 'name': 'mwm_wd_core', 'mapper': 'mwm', 'alt_program': 'wd', 'alt_name': 'mwm_wd'},
        94: {'label': 'mwm_tess_planet_0.5.0', 'carton_pk': 586, 'program': 'mwm_planet', 'version': '0.5.0', 'v1': 5.0, 'name': 'mwm_tess_planet', 'mapper': 'mwm', 'alt_program': 'planet', 'alt_name': 'mwm_tess_2min'},
        95: {'label': 'mwm_snc_100pc_apogee_0.5.0', 'carton_pk': 587, 'program': 'mwm_snc', 'version': '0.5.0', 'v1': 5.0, 'name': 'mwm_snc_100pc_apogee', 'mapper': 'mwm', 'alt_program': 'snc', 'alt_name': 'mwm_snc'},
        96: {'label': 'mwm_tess_ob_0.5.0', 'carton_pk': 629, 'program': 'mwm_tess_ob', 'version': '0.5.0', 'v1': 5.0, 'name': 'mwm_tess_ob', 'mapper': 'mwm', 'alt_program': 'tessob', 'alt_name': 'mwm_tess_ob'},
        97: {'label': 'mwm_cb_uvex1_0.5.0', 'carton_pk': 632, 'program': 'mwm_cb', 'version': '0.5.0', 'v1': 5.0, 'name': 'mwm_cb_uvex1', 'mapper': 'mwm', 'alt_program': 'cb', 'alt_name': 'mwm_cb_galex'},
        98: {'label': 'mwm_cb_uvex2_0.5.0', 'carton_pk': 633, 'program': 'mwm_cb', 'version': '0.5.0', 'v1': 5.0, 'name': 'mwm_cb_uvex2', 'mapper': 'mwm', 'alt_program': 'cb', 'alt_name': 'mwm_cb_galex'},
        99: {'label': 'mwm_tessrgb_core_0.5.0', 'carton_pk': 637, 'program': 'mwm_tessrgb', 'version': '0.5.0', 'v1': 5.0, 'name': 'mwm_tessrgb_core', 'mapper': 'mwm', 'alt_program': 'tessrgb', 'alt_name': 'mwm_tess_rgb'},
        100: {'label': 'ops_std_boss_tic_0.5.0', 'carton_pk': 675, 'program': 'ops_std', 'version': '0.5.0', 'v1': 5.0, 'name': 'ops_std_boss_tic', 'mapper': 'ops', 'alt_program': 'std', 'alt_name': 'ops_std'},
        101: {'label': 'mwm_rv_long_fps_0.5.0', 'carton_pk': 681, 'program': 'mwm_rv', 'version': '0.5.0', 'v1': 5.0, 'name': 'mwm_rv_long_fps', 'mapper': 'mwm', 'alt_program': 'bin', 'alt_name': 'mwm_bin_rv_long'},
        102: {'label': 'mwm_halo_bb_boss_0.5.0', 'carton_pk': 690, 'program': 'mwm_filler', 'version': '0.5.0', 'v1': 5.0, 'name': 'mwm_halo_bb_boss', 'mapper': 'mwm', 'alt_program': 'halo', 'alt_name': 'mwm_halo_bb'},
        103: {'label': 'mwm_cb_300pc_apogee_0.5.0', 'carton_pk': 691, 'program': 'mwm_cb', 'version': '0.5.0', 'v1': 5.0, 'name': 'mwm_cb_300pc_apogee', 'mapper': 'mwm', 'alt_program': 'cb', 'alt_name': 'mwm_cb_300pc'},
        104: {'label': 'mwm_cb_300pc_boss_0.5.0', 'carton_pk': 692, 'program': 'mwm_cb', 'version': '0.5.0', 'v1': 5.0, 'name': 'mwm_cb_300pc_boss', 'mapper': 'mwm', 'alt_program': 'cb', 'alt_name': 'mwm_cb_300pc'},
        105: {'label': 'bhm_spiders_agn_gaiadr2_0.5.0', 'carton_pk': 693, 'program': 'bhm_spiders', 'version': '0.5.0', 'v1': 5.0, 'name': 'bhm_spiders_agn_gaiadr2', 'mapper': 'bhm', 'alt_program': 'spiders', 'alt_name': 'bhm_spiders'},
        106: {'label': 'bhm_spiders_agn_lsdr8_0.5.0', 'carton_pk': 694, 'program': 'bhm_spiders', 'version': '0.5.0', 'v1': 5.0, 'name': 'bhm_spiders_agn_lsdr8', 'mapper': 'bhm', 'alt_program': 'spiders', 'alt_name': 'bhm_spiders'},
        107: {'label': 'bhm_spiders_agn_sep_0.5.0', 'carton_pk': 695, 'program': 'bhm_spiders', 'version': '0.5.0', 'v1': 5.0, 'name': 'bhm_spiders_agn_sep', 'mapper': 'bhm', 'alt_program': 'spiders', 'alt_name': 'bhm_spiders'},
        108: {'label': 'bhm_spiders_agn_efeds_stragglers_0.5.0', 'carton_pk': 696, 'program': 'bhm_spiders', 'version': '0.5.0', 'v1': 5.0, 'name': 'bhm_spiders_agn_efeds_stragglers', 'mapper': 'bhm', 'alt_program': 'spiders', 'alt_name': 'bhm_spiders'},
        109: {'label': 'bhm_spiders_agn_ps1dr2_0.5.0', 'carton_pk': 704, 'program': 'bhm_spiders', 'version': '0.5.0', 'v1': 5.0, 'name': 'bhm_spiders_agn_ps1dr2', 'mapper': 'bhm', 'alt_program': 'spiders', 'alt_name': 'bhm_spiders'},
        110: {'label': 'bhm_spiders_agn_skymapperdr2_0.5.0', 'carton_pk': 705, 'program': 'bhm_spiders', 'version': '0.5.0', 'v1': 5.0, 'name': 'bhm_spiders_agn_skymapperdr2', 'mapper': 'bhm', 'alt_program': 'spiders', 'alt_name': 'bhm_spiders'},
        111: {'label': 'bhm_spiders_agn_supercosmos_0.5.0', 'carton_pk': 706, 'program': 'bhm_spiders', 'version': '0.5.0', 'v1': 5.0, 'name': 'bhm_spiders_agn_supercosmos', 'mapper': 'bhm', 'alt_program': 'spiders', 'alt_name': 'bhm_spiders'},
        112: {'label': 'bhm_spiders_clusters_lsdr8_0.5.0', 'carton_pk': 707, 'program': 'bhm_spiders', 'version': '0.5.0', 'v1': 5.0, 'name': 'bhm_spiders_clusters_lsdr8', 'mapper': 'bhm', 'alt_program': 'spiders', 'alt_name': 'bhm_spiders'},
        113: {'label': 'bhm_spiders_clusters_ps1dr2_0.5.0', 'carton_pk': 708, 'program': 'bhm_spiders', 'version': '0.5.0', 'v1': 5.0, 'name': 'bhm_spiders_clusters_ps1dr2', 'mapper': 'bhm', 'alt_program': 'spiders', 'alt_name': 'bhm_spiders'},
        114: {'label': 'bhm_spiders_clusters_efeds_stragglers_0.5.0', 'carton_pk': 709, 'program': 'bhm_spiders', 'version': '0.5.0', 'v1': 5.0, 'name': 'bhm_spiders_clusters_efeds_stragglers', 'mapper': 'bhm', 'alt_program': 'spiders', 'alt_name': 'bhm_spiders'},
        115: {'label': 'bhm_gua_bright_0.5.0', 'carton_pk': 710, 'program': 'bhm_filler', 'version': '0.5.0', 'v1': 5.0, 'name': 'bhm_gua_bright', 'mapper': 'bhm', 'alt_program': 'filler', 'alt_name': 'bhm_filler'},
        116: {'label': 'bhm_gua_dark_0.5.0', 'carton_pk': 711, 'program': 'bhm_filler', 'version': '0.5.0', 'v1': 5.0, 'name': 'bhm_gua_dark', 'mapper': 'bhm', 'alt_program': 'filler', 'alt_name': 'bhm_filler'},
        117: {'label': 'mwm_cb_uvex5_0.5.0', 'carton_pk': 715, 'program': 'mwm_cb', 'version': '0.5.0', 'v1': 5.0, 'name': 'mwm_cb_uvex5', 'mapper': 'mwm', 'alt_program': 'cb', 'alt_name': 'mwm_cb_galex'},
        118: {'label': 'bhm_rm_known_spec_0.5.0', 'carton_pk': 723, 'program': 'bhm_rm', 'version': '0.5.0', 'v1': 5.0, 'name': 'bhm_rm_known_spec', 'mapper': 'bhm', 'alt_program': 'rm', 'alt_name': 'bhm_rm'},
        119: {'label': 'bhm_rm_core_0.5.0', 'carton_pk': 724, 'program': 'bhm_rm', 'version': '0.5.0', 'v1': 5.0, 'name': 'bhm_rm_core', 'mapper': 'bhm', 'alt_program': 'rm', 'alt_name': 'bhm_rm'},
        120: {'label': 'bhm_rm_var_0.5.0', 'carton_pk': 725, 'program': 'bhm_rm', 'version': '0.5.0', 'v1': 5.0, 'name': 'bhm_rm_var', 'mapper': 'bhm', 'alt_program': 'rm', 'alt_name': 'bhm_rm'},
        121: {'label': 'bhm_rm_ancillary_0.5.0', 'carton_pk': 726, 'program': 'bhm_rm', 'version': '0.5.0', 'v1': 5.0, 'name': 'bhm_rm_ancillary', 'mapper': 'bhm', 'alt_program': 'rm', 'alt_name': 'bhm_rm'},
        122: {'label': 'ops_std_boss_lsdr8_0.5.0', 'carton_pk': 727, 'program': 'ops_std', 'version': '0.5.0', 'v1': 5.0, 'name': 'ops_std_boss_lsdr8', 'mapper': 'ops', 'alt_program': 'std', 'alt_name': 'ops_std'},
        123: {'label': 'ops_std_boss_ps1dr2_0.5.0', 'carton_pk': 728, 'program': 'ops_std', 'version': '0.5.0', 'v1': 5.0, 'name': 'ops_std_boss_ps1dr2', 'mapper': 'ops', 'alt_program': 'std', 'alt_name': 'ops_std'},
        124: {'label': 'ops_std_boss_gdr2_0.5.0', 'carton_pk': 729, 'program': 'ops_std', 'version': '0.5.0', 'v1': 5.0, 'name': 'ops_std_boss_gdr2', 'mapper': 'ops', 'alt_program': 'std', 'alt_name': 'ops_std'},
        125: {'label': 'bhm_aqmes_med_0.5.0', 'carton_pk': 731, 'program': 'bhm_aqmes', 'version': '0.5.0', 'v1': 5.0, 'name': 'bhm_aqmes_med', 'mapper': 'bhm', 'alt_program': 'aqmes', 'alt_name': 'bhm_aqmes'},
        126: {'label': 'bhm_aqmes_med_faint_0.5.0', 'carton_pk': 732, 'program': 'bhm_filler', 'version': '0.5.0', 'v1': 5.0, 'name': 'bhm_aqmes_med_faint', 'mapper': 'bhm', 'alt_program': 'filler', 'alt_name': 'bhm_aqmes'},
        127: {'label': 'bhm_csc_boss_dark_0.5.0', 'carton_pk': 733, 'program': 'bhm_csc', 'version': '0.5.0', 'v1': 5.0, 'name': 'bhm_csc_boss_dark', 'mapper': 'bhm', 'alt_program': 'csc', 'alt_name': 'bhm_csc'},
        128: {'label': 'bhm_csc_boss_bright_0.5.0', 'carton_pk': 734, 'program': 'bhm_csc', 'version': '0.5.0', 'v1': 5.0, 'name': 'bhm_csc_boss_bright', 'mapper': 'bhm', 'alt_program': 'csc', 'alt_name': 'bhm_csc'},
        129: {'label': 'bhm_csc_apogee_0.5.0', 'carton_pk': 735, 'program': 'bhm_csc', 'version': '0.5.0', 'v1': 5.0, 'name': 'bhm_csc_apogee', 'mapper': 'bhm', 'alt_program': 'csc', 'alt_name': 'bhm_csc'},
        130: {'label': 'mwm_yso_pms_apogee_0.5.1', 'carton_pk': 750, 'program': 'mwm_yso', 'version': '0.5.1', 'v1': 5.01, 'name': 'mwm_yso_pms_apogee', 'mapper': 'mwm', 'alt_program': 'yso', 'alt_name': 'mwm_yso_pms'},
        131: {'label': 'mwm_yso_pms_boss_0.5.1', 'carton_pk': 751, 'program': 'mwm_yso', 'version': '0.5.1', 'v1': 5.01, 'name': 'mwm_yso_pms_boss', 'mapper': 'mwm', 'alt_program': 'yso', 'alt_name': 'mwm_yso_pms'},
        132: {'label': 'mwm_ob_core_0.5.1', 'carton_pk': 752, 'program': 'mwm_ob', 'version': '0.5.1', 'v1': 5.01, 'name': 'mwm_ob_core', 'mapper': 'mwm', 'alt_program': 'ob', 'alt_name': 'mwm_ob_core'},
        133: {'label': 'mwm_ob_cepheids_0.5.1', 'carton_pk': 753, 'program': 'mwm_ob', 'version': '0.5.1', 'v1': 5.01, 'name': 'mwm_ob_cepheids', 'mapper': 'mwm', 'alt_program': 'ob', 'alt_name': 'mwm_ob_cepheids'},
        134: {'label': 'mwm_halo_bb_boss_0.5.1', 'carton_pk': 754, 'program': 'mwm_filler', 'version': '0.5.1', 'v1': 5.01, 'name': 'mwm_halo_bb_boss', 'mapper': 'mwm', 'alt_program': 'halo', 'alt_name': 'mwm_halo_bb'},
        135: {'label': 'mwm_halo_sm_boss_0.5.1', 'carton_pk': 755, 'program': 'mwm_filler', 'version': '0.5.1', 'v1': 5.01, 'name': 'mwm_halo_sm_boss', 'mapper': 'mwm', 'alt_program': 'halo', 'alt_name': 'mwm_halo_sm'},
        136: {'label': 'mwm_erosita_stars_0.5.2', 'carton_pk': 770, 'program': 'mwm_erosita', 'version': '0.5.2', 'v1': 5.02, 'name': 'mwm_erosita_stars', 'mapper': 'mwm', 'alt_program': 'erosita', 'alt_name': 'mwm_erosita_stars'},
        137: {'label': 'mwm_erosita_compact_gen_0.5.2', 'carton_pk': 771, 'program': 'mwm_erosita', 'version': '0.5.2', 'v1': 5.02, 'name': 'mwm_erosita_compact_gen', 'mapper': 'mwm', 'alt_program': 'erosita', 'alt_name': 'mwm_erosita_compact'},
        138: {'label': 'mwm_erosita_compact_var_0.5.2', 'carton_pk': 772, 'program': 'mwm_erosita', 'version': '0.5.2', 'v1': 5.02, 'name': 'mwm_erosita_compact_var', 'mapper': 'mwm', 'alt_program': 'erosita', 'alt_name': 'mwm_erosita_compact'},
        139: {'label': 'openfibertargets_nov2020_25_0.5.2-test', 'carton_pk': 892, 'program': 'open_fiber', 'version': '0.5.2-test', 'v1': 5.02, 'name': 'openfibertargets_nov2020_25', 'mapper': 'open', 'alt_program': 'open_fiber', 'alt_name': 'mwm_halo_local'},
        140: {'label': 'openfibertargets_nov2020_28a_0.5.2-test', 'carton_pk': 895, 'program': 'open_fiber', 'version': '0.5.2-test', 'v1': 5.02, 'name': 'openfibertargets_nov2020_28a', 'mapper': 'open', 'alt_program': 'open_fiber', 'alt_name': 'manual_mwm_halo_distant_kgiant'},
        141: {'label': 'openfibertargets_nov2020_28b_0.5.2-test', 'carton_pk': 896, 'program': 'open_fiber', 'version': '0.5.2-test', 'v1': 5.02, 'name': 'openfibertargets_nov2020_28b', 'mapper': 'open', 'alt_program': 'open_fiber', 'alt_name': 'manual_mwm_halo_distant_bhb'},
        142: {'label': 'openfibertargets_nov2020_28c_0.5.2-test', 'carton_pk': 897, 'program': 'open_fiber', 'version': '0.5.2-test', 'v1': 5.02, 'name': 'openfibertargets_nov2020_28c', 'mapper': 'open', 'alt_program': 'open_fiber', 'alt_name': 'mwm_halo_distant_rrl'},
        143: {'label': 'openfibertargets_nov2020_35a_0.5.2-test', 'carton_pk': 903, 'program': 'open_fiber', 'version': '0.5.2-test', 'v1': 5.02, 'name': 'openfibertargets_nov2020_35a', 'mapper': 'open', 'alt_program': 'open_fiber', 'alt_name': 'manual_mwm_halo_mp_wise'},
        144: {'label': 'openfibertargets_nov2020_35b_0.5.2-test', 'carton_pk': 904, 'program': 'open_fiber', 'version': '0.5.2-test', 'v1': 5.02, 'name': 'openfibertargets_nov2020_35b', 'mapper': 'open', 'alt_program': 'open_fiber', 'alt_name': 'mwm_halo_openfiber'},
        145: {'label': 'openfibertargets_nov2020_5_0.5.2-test', 'carton_pk': 912, 'program': 'open_fiber', 'version': '0.5.2-test', 'v1': 5.02, 'name': 'openfibertargets_nov2020_5', 'mapper': 'open', 'alt_program': 'open_fiber', 'alt_name': 'mwm_halo_openfiber'},
        146: {'label': 'openfibertargets_nov2020_6b_0.5.2-test', 'carton_pk': 914, 'program': 'open_fiber', 'version': '0.5.2-test', 'v1': 5.02, 'name': 'openfibertargets_nov2020_6b', 'mapper': 'open', 'alt_program': 'open_fiber', 'alt_name': 'mwm_halo_openfiber'},
        147: {'label': 'openfibertargets_nov2020_6c_0.5.2-test', 'carton_pk': 915, 'program': 'open_fiber', 'version': '0.5.2-test', 'v1': 5.02, 'name': 'openfibertargets_nov2020_6c', 'mapper': 'open', 'alt_program': 'open_fiber', 'alt_name': 'mwm_halo_openfiber'},
        148: {'label': 'openfibertargets_nov2020_10_0.5.3', 'carton_pk': 999, 'program': 'open_fiber', 'version': '0.5.3', 'v1': 5.03, 'name': 'openfibertargets_nov2020_10', 'mapper': 'open', 'alt_program': 'open_fiber', 'alt_name': 'mwm_bin_openfiber'},
        149: {'label': 'openfibertargets_nov2020_1000_0.5.3', 'carton_pk': 1000, 'program': 'open_fiber', 'version': '0.5.3', 'v1': 5.03, 'name': 'openfibertargets_nov2020_1000', 'mapper': 'open', 'alt_program': 'open_fiber', 'alt_name': 'mwm_cluster_openfiber'},
        150: {'label': 'openfibertargets_nov2020_1001a_0.5.3', 'carton_pk': 1001, 'program': 'open_fiber', 'version': '0.5.3', 'v1': 5.03, 'name': 'openfibertargets_nov2020_1001a', 'mapper': 'open', 'alt_program': 'open_fiber', 'alt_name': 'mwm_bin_openfiber'},
        151: {'label': 'openfibertargets_nov2020_1001b_0.5.3', 'carton_pk': 1002, 'program': 'open_fiber', 'version': '0.5.3', 'v1': 5.03, 'name': 'openfibertargets_nov2020_1001b', 'mapper': 'open', 'alt_program': 'open_fiber', 'alt_name': 'mwm_bin_openfiber'},
        152: {'label': 'openfibertargets_nov2020_11_0.5.3', 'carton_pk': 1003, 'program': 'open_fiber', 'version': '0.5.3', 'v1': 5.03, 'name': 'openfibertargets_nov2020_11', 'mapper': 'open', 'alt_program': 'open_fiber', 'alt_name': 'bhm_openfiber'},
        153: {'label': 'openfibertargets_nov2020_12_0.5.3', 'carton_pk': 1004, 'program': 'open_fiber', 'version': '0.5.3', 'v1': 5.03, 'name': 'openfibertargets_nov2020_12', 'mapper': 'open', 'alt_program': 'open_fiber', 'alt_name': 'mwm_bin_openfiber'},
        154: {'label': 'openfibertargets_nov2020_14_0.5.3', 'carton_pk': 1005, 'program': 'open_fiber', 'version': '0.5.3', 'v1': 5.03, 'name': 'openfibertargets_nov2020_14', 'mapper': 'open', 'alt_program': 'open_fiber', 'alt_name': 'mwm_bin_openfiber'},
        155: {'label': 'openfibertargets_nov2020_15_0.5.3', 'carton_pk': 1006, 'program': 'open_fiber', 'version': '0.5.3', 'v1': 5.03, 'name': 'openfibertargets_nov2020_15', 'mapper': 'open', 'alt_program': 'open_fiber', 'alt_name': 'mwm_cluster_openfiber'},
        156: {'label': 'openfibertargets_nov2020_17_0.5.3', 'carton_pk': 1007, 'program': 'open_fiber', 'version': '0.5.3', 'v1': 5.03, 'name': 'openfibertargets_nov2020_17', 'mapper': 'open', 'alt_program': 'open_fiber', 'alt_name': 'mwm_yso_pms'},
        157: {'label': 'openfibertargets_nov2020_18_0.5.3', 'carton_pk': 1008, 'program': 'open_fiber', 'version': '0.5.3', 'v1': 5.03, 'name': 'openfibertargets_nov2020_18', 'mapper': 'open', 'alt_program': 'open_fiber', 'alt_name': 'bhm_openfiber'},
        158: {'label': 'openfibertargets_nov2020_22_0.5.3', 'carton_pk': 1009, 'program': 'open_fiber', 'version': '0.5.3', 'v1': 5.03, 'name': 'openfibertargets_nov2020_22', 'mapper': 'open', 'alt_program': 'open_fiber', 'alt_name': 'mwm_bin_openfiber'},
        159: {'label': 'openfibertargets_nov2020_24_0.5.3', 'carton_pk': 1010, 'program': 'open_fiber', 'version': '0.5.3', 'v1': 5.03, 'name': 'openfibertargets_nov2020_24', 'mapper': 'open', 'alt_program': 'open_fiber', 'alt_name': 'mwm_snc_openfiber'},
        160: {'label': 'openfibertargets_nov2020_25_0.5.3', 'carton_pk': 1011, 'program': 'open_fiber', 'version': '0.5.3', 'v1': 5.03, 'name': 'openfibertargets_nov2020_25', 'mapper': 'open', 'alt_program': 'open_fiber', 'alt_name': 'mwm_halo_local'},
        161: {'label': 'openfibertargets_nov2020_26_0.5.3', 'carton_pk': 1012, 'program': 'open_fiber', 'version': '0.5.3', 'v1': 5.03, 'name': 'openfibertargets_nov2020_26', 'mapper': 'open', 'alt_program': 'open_fiber', 'alt_name': 'bhm_openfiber'},
        162: {'label': 'openfibertargets_nov2020_27_0.5.3', 'carton_pk': 1013, 'program': 'open_fiber', 'version': '0.5.3', 'v1': 5.03, 'name': 'openfibertargets_nov2020_27', 'mapper': 'open', 'alt_program': 'open_fiber', 'alt_name': 'bhm_openfiber'},
        163: {'label': 'openfibertargets_nov2020_28a_0.5.3', 'carton_pk': 1014, 'program': 'open_fiber', 'version': '0.5.3', 'v1': 5.03, 'name': 'openfibertargets_nov2020_28a', 'mapper': 'open', 'alt_program': 'open_fiber', 'alt_name': 'manual_mwm_halo_distant_kgiant'},
        164: {'label': 'openfibertargets_nov2020_28b_0.5.3', 'carton_pk': 1015, 'program': 'open_fiber', 'version': '0.5.3', 'v1': 5.03, 'name': 'openfibertargets_nov2020_28b', 'mapper': 'open', 'alt_program': 'open_fiber', 'alt_name': 'manual_mwm_halo_distant_bhb'},
        165: {'label': 'openfibertargets_nov2020_28c_0.5.3', 'carton_pk': 1016, 'program': 'open_fiber', 'version': '0.5.3', 'v1': 5.03, 'name': 'openfibertargets_nov2020_28c', 'mapper': 'open', 'alt_program': 'open_fiber', 'alt_name': 'mwm_halo_distant_rrl'},
        166: {'label': 'openfibertargets_nov2020_29_0.5.3', 'carton_pk': 1017, 'program': 'open_fiber', 'version': '0.5.3', 'v1': 5.03, 'name': 'openfibertargets_nov2020_29', 'mapper': 'open', 'alt_program': 'open_fiber', 'alt_name': 'mwm_cluster_openfiber'},
        167: {'label': 'openfibertargets_nov2020_3_0.5.3', 'carton_pk': 1018, 'program': 'open_fiber', 'version': '0.5.3', 'v1': 5.03, 'name': 'openfibertargets_nov2020_3', 'mapper': 'open', 'alt_program': 'open_fiber', 'alt_name': 'mwm_bin_openfiber'},
        168: {'label': 'openfibertargets_nov2020_30_0.5.3', 'carton_pk': 1019, 'program': 'open_fiber', 'version': '0.5.3', 'v1': 5.03, 'name': 'openfibertargets_nov2020_30', 'mapper': 'open', 'alt_program': 'open_fiber', 'alt_name': 'bhm_openfiber'},
        169: {'label': 'openfibertargets_nov2020_31_0.5.3', 'carton_pk': 1020, 'program': 'open_fiber', 'version': '0.5.3', 'v1': 5.03, 'name': 'openfibertargets_nov2020_31', 'mapper': 'open', 'alt_program': 'open_fiber', 'alt_name': 'mwm_validation_openfiber'},
        170: {'label': 'openfibertargets_nov2020_32_0.5.3', 'carton_pk': 1021, 'program': 'open_fiber', 'version': '0.5.3', 'v1': 5.03, 'name': 'openfibertargets_nov2020_32', 'mapper': 'open', 'alt_program': 'open_fiber', 'alt_name': 'mwm_bin_openfiber'},
        171: {'label': 'openfibertargets_nov2020_33_0.5.3', 'carton_pk': 1022, 'program': 'open_fiber', 'version': '0.5.3', 'v1': 5.03, 'name': 'openfibertargets_nov2020_33', 'mapper': 'open', 'alt_program': 'open_fiber', 'alt_name': 'bhm_openfiber'},
        172: {'label': 'openfibertargets_nov2020_35a_0.5.3', 'carton_pk': 1023, 'program': 'open_fiber', 'version': '0.5.3', 'v1': 5.03, 'name': 'openfibertargets_nov2020_35a', 'mapper': 'open', 'alt_program': 'open_fiber', 'alt_name': 'manual_mwm_halo_mp_wise'},
        173: {'label': 'openfibertargets_nov2020_35b_0.5.3', 'carton_pk': 1024, 'program': 'open_fiber', 'version': '0.5.3', 'v1': 5.03, 'name': 'openfibertargets_nov2020_35b', 'mapper': 'open', 'alt_program': 'open_fiber', 'alt_name': 'mwm_halo_openfiber'},
        174: {'label': 'openfibertargets_nov2020_35c_0.5.3', 'carton_pk': 1025, 'program': 'open_fiber', 'version': '0.5.3', 'v1': 5.03, 'name': 'openfibertargets_nov2020_35c', 'mapper': 'open', 'alt_program': 'open_fiber', 'alt_name': 'mwm_halo_openfiber'},
        175: {'label': 'openfibertargets_nov2020_46_0.5.3', 'carton_pk': 1026, 'program': 'open_fiber', 'version': '0.5.3', 'v1': 5.03, 'name': 'openfibertargets_nov2020_46', 'mapper': 'open', 'alt_program': 'open_fiber', 'alt_name': 'mwm_bin_openfiber'},
        176: {'label': 'openfibertargets_nov2020_47a_0.5.3', 'carton_pk': 1027, 'program': 'open_fiber', 'version': '0.5.3', 'v1': 5.03, 'name': 'openfibertargets_nov2020_47a', 'mapper': 'open', 'alt_program': 'open_fiber', 'alt_name': 'mwm_magcloud_rgb'},
        177: {'label': 'openfibertargets_nov2020_47b_0.5.3', 'carton_pk': 1028, 'program': 'open_fiber', 'version': '0.5.3', 'v1': 5.03, 'name': 'openfibertargets_nov2020_47b', 'mapper': 'open', 'alt_program': 'open_fiber', 'alt_name': 'mwm_magcloud_agb'},
        178: {'label': 'openfibertargets_nov2020_47c_0.5.3', 'carton_pk': 1029, 'program': 'open_fiber', 'version': '0.5.3', 'v1': 5.03, 'name': 'openfibertargets_nov2020_47c', 'mapper': 'open', 'alt_program': 'open_fiber', 'alt_name': 'mwm_magcloud_massive'},
        179: {'label': 'openfibertargets_nov2020_47d_0.5.3', 'carton_pk': 1030, 'program': 'open_fiber', 'version': '0.5.3', 'v1': 5.03, 'name': 'openfibertargets_nov2020_47d', 'mapper': 'open', 'alt_program': 'open_fiber', 'alt_name': 'mwm_magcloud_massive'},
        180: {'label': 'openfibertargets_nov2020_47e_0.5.3', 'carton_pk': 1031, 'program': 'open_fiber', 'version': '0.5.3', 'v1': 5.03, 'name': 'openfibertargets_nov2020_47e', 'mapper': 'open', 'alt_program': 'open_fiber', 'alt_name': 'mwm_magcloud_symbiotic'},
        181: {'label': 'openfibertargets_nov2020_8_0.5.3', 'carton_pk': 1036, 'program': 'open_fiber', 'version': '0.5.3', 'v1': 5.03, 'name': 'openfibertargets_nov2020_8', 'mapper': 'open', 'alt_program': 'open_fiber', 'alt_name': 'mwm_cluster_openfiber'},
        182: {'label': 'openfibertargets_nov2020_9_0.5.3', 'carton_pk': 1037, 'program': 'open_fiber', 'version': '0.5.3', 'v1': 5.03, 'name': 'openfibertargets_nov2020_9', 'mapper': 'open', 'alt_program': 'open_fiber', 'alt_name': 'mwm_cluster_openfiber'},
        183: {'label': 'openfibertargets_nov2020_19a_0.5.3', 'carton_pk': 1040, 'program': 'open_fiber', 'version': '0.5.3', 'v1': 5.03, 'name': 'openfibertargets_nov2020_19a', 'mapper': 'open', 'alt_program': 'open_fiber', 'alt_name': 'mwm_tess_2min'},
        184: {'label': 'openfibertargets_nov2020_19b_0.5.3', 'carton_pk': 1041, 'program': 'open_fiber', 'version': '0.5.3', 'v1': 5.03, 'name': 'openfibertargets_nov2020_19b', 'mapper': 'open', 'alt_program': 'open_fiber', 'alt_name': 'mwm_tess_2min'},
        185: {'label': 'openfibertargets_nov2020_19c_0.5.3', 'carton_pk': 1042, 'program': 'open_fiber', 'version': '0.5.3', 'v1': 5.03, 'name': 'openfibertargets_nov2020_19c', 'mapper': 'open', 'alt_program': 'open_fiber', 'alt_name': 'mwm_tess_2min'},
        186: {'label': 'manual_nsbh_apogee_0.5.3', 'carton_pk': 1043, 'program': 'mwm_cb', 'version': '0.5.3', 'v1': 5.03, 'name': 'manual_nsbh_apogee', 'mapper': 'mwm', 'alt_program': 'nsbh', 'alt_name': 'manual_mwm_nsbh'},
        187: {'label': 'manual_nsbh_boss_0.5.3', 'carton_pk': 1044, 'program': 'mwm_cb', 'version': '0.5.3', 'v1': 5.03, 'name': 'manual_nsbh_boss', 'mapper': 'mwm', 'alt_program': 'nsbh', 'alt_name': 'manual_mwm_nsbh'},
        188: {'label': 'manual_bhm_spiders_comm_0.5.3', 'carton_pk': 1048, 'program': 'commissioning', 'version': '0.5.3', 'v1': 5.03, 'name': 'manual_bhm_spiders_comm', 'mapper': 'ops', 'alt_program': 'commissioning', 'alt_name': 'bhm_spiders'},
        189: {'label': 'bhm_aqmes_bonus_bright_0.5.4', 'carton_pk': 1049, 'program': 'bhm_filler', 'version': '0.5.4', 'v1': 5.04, 'name': 'bhm_aqmes_bonus_bright', 'mapper': 'bhm', 'alt_program': 'filler', 'alt_name': 'bhm_aqmes'},
        190: {'label': 'bhm_aqmes_bonus_core_0.5.4', 'carton_pk': 1050, 'program': 'bhm_filler', 'version': '0.5.4', 'v1': 5.04, 'name': 'bhm_aqmes_bonus_core', 'mapper': 'bhm', 'alt_program': 'filler', 'alt_name': 'bhm_aqmes'},
        191: {'label': 'bhm_aqmes_bonus_faint_0.5.4', 'carton_pk': 1051, 'program': 'bhm_filler', 'version': '0.5.4', 'v1': 5.04, 'name': 'bhm_aqmes_bonus_faint', 'mapper': 'bhm', 'alt_program': 'filler', 'alt_name': 'bhm_aqmes'},
        192: {'label': 'bhm_aqmes_wide2_0.5.4', 'carton_pk': 1052, 'program': 'bhm_aqmes', 'version': '0.5.4', 'v1': 5.04, 'name': 'bhm_aqmes_wide2', 'mapper': 'bhm', 'alt_program': 'aqmes', 'alt_name': 'bhm_aqmes'},
        193: {'label': 'bhm_aqmes_wide2_faint_0.5.4', 'carton_pk': 1053, 'program': 'bhm_filler', 'version': '0.5.4', 'v1': 5.04, 'name': 'bhm_aqmes_wide2_faint', 'mapper': 'bhm', 'alt_program': 'filler', 'alt_name': 'bhm_aqmes'},
        194: {'label': 'mwm_cb_300pc_boss_0.5.4', 'carton_pk': 1055, 'program': 'mwm_cb', 'version': '0.5.4', 'v1': 5.04, 'name': 'mwm_cb_300pc_boss', 'mapper': 'mwm', 'alt_program': 'cb', 'alt_name': 'mwm_cb_300pc'},
        195: {'label': 'openfibertargets_nov2020_5_0.5.3', 'carton_pk': 1056, 'program': 'open_fiber', 'version': '0.5.3', 'v1': 5.03, 'name': 'openfibertargets_nov2020_5', 'mapper': 'open', 'alt_program': 'open_fiber', 'alt_name': 'mwm_halo_openfiber'},
        196: {'label': 'openfibertargets_nov2020_6a_0.5.3', 'carton_pk': 1057, 'program': 'open_fiber', 'version': '0.5.3', 'v1': 5.03, 'name': 'openfibertargets_nov2020_6a', 'mapper': 'open', 'alt_program': 'open_fiber', 'alt_name': 'mwm_halo_openfiber'},
        197: {'label': 'openfibertargets_nov2020_6b_0.5.3', 'carton_pk': 1058, 'program': 'open_fiber', 'version': '0.5.3', 'v1': 5.03, 'name': 'openfibertargets_nov2020_6b', 'mapper': 'open', 'alt_program': 'open_fiber', 'alt_name': 'mwm_halo_openfiber'},
        198: {'label': 'openfibertargets_nov2020_6c_0.5.3', 'carton_pk': 1059, 'program': 'open_fiber', 'version': '0.5.3', 'v1': 5.03, 'name': 'openfibertargets_nov2020_6c', 'mapper': 'open', 'alt_program': 'open_fiber', 'alt_name': 'mwm_halo_openfiber'},
        199: {'label': 'manual_bright_target_offsets_1_0.5.3', 'carton_pk': 1069, 'program': 'commissioning', 'version': '0.5.3', 'v1': 5.03, 'name': 'manual_bright_target_offsets_1', 'mapper': 'ops', 'alt_program': 'commissioning', 'alt_name': 'mwm_ob_core'},
        200: {'label': 'manual_bright_target_offsets_1_g13_0.5.3', 'carton_pk': 1070, 'program': 'commissioning', 'version': '0.5.3', 'v1': 5.03, 'name': 'manual_bright_target_offsets_1_g13', 'mapper': 'ops', 'alt_program': 'commissioning', 'alt_name': 'mwm_ob_core'},
        201: {'label': 'manual_bright_targets_g13_0.5.3', 'carton_pk': 1073, 'program': 'commissioning', 'version': '0.5.3', 'v1': 5.03, 'name': 'manual_bright_targets_g13', 'mapper': 'ops', 'alt_program': 'commissioning', 'alt_name': 'mwm_ob_core'},
        202: {'label': 'manual_bright_targets_g13_offset_fixed_1_0.5.3', 'carton_pk': 1074, 'program': 'commissioning', 'version': '0.5.3', 'v1': 5.03, 'name': 'manual_bright_targets_g13_offset_fixed_1', 'mapper': 'ops', 'alt_program': 'commissioning', 'alt_name': 'mwm_ob_core'},
        203: {'label': 'manual_bright_targets_g13_offset_fixed_3_0.5.3', 'carton_pk': 1076, 'program': 'commissioning', 'version': '0.5.3', 'v1': 5.03, 'name': 'manual_bright_targets_g13_offset_fixed_3', 'mapper': 'ops', 'alt_program': 'commissioning', 'alt_name': 'mwm_ob_core'},
        204: {'label': 'manual_bright_targets_g13_offset_fixed_5_0.5.3', 'carton_pk': 1078, 'program': 'commissioning', 'version': '0.5.3', 'v1': 5.03, 'name': 'manual_bright_targets_g13_offset_fixed_5', 'mapper': 'ops', 'alt_program': 'commissioning', 'alt_name': 'mwm_ob_core'},
        205: {'label': 'manual_bright_targets_g13_offset_fixed_7_0.5.3', 'carton_pk': 1080, 'program': 'commissioning', 'version': '0.5.3', 'v1': 5.03, 'name': 'manual_bright_targets_g13_offset_fixed_7', 'mapper': 'ops', 'alt_program': 'commissioning', 'alt_name': 'mwm_ob_core'},
        206: {'label': 'ops_sky_boss_best_0.5.7', 'carton_pk': 1082, 'program': 'SKY', 'version': '0.5.7', 'v1': 5.07, 'name': 'ops_sky_boss_best', 'mapper': 'ops', 'alt_program': 'sky', 'alt_name': 'ops_sky'},
        207: {'label': 'ops_sky_boss_good_0.5.7', 'carton_pk': 1083, 'program': 'SKY', 'version': '0.5.7', 'v1': 5.07, 'name': 'ops_sky_boss_good', 'mapper': 'ops', 'alt_program': 'sky', 'alt_name': 'ops_sky'},
        208: {'label': 'ops_sky_boss_best_0.5.8', 'carton_pk': 1090, 'program': 'SKY', 'version': '0.5.8', 'v1': 5.08, 'name': 'ops_sky_boss_best', 'mapper': 'ops', 'alt_program': 'sky', 'alt_name': 'ops_sky'},
        209: {'label': 'ops_sky_boss_good_0.5.8', 'carton_pk': 1091, 'program': 'SKY', 'version': '0.5.8', 'v1': 5.08, 'name': 'ops_sky_boss_good', 'mapper': 'ops', 'alt_program': 'sky', 'alt_name': 'ops_sky'},
        210: {'label': 'ops_sky_apogee_best_0.5.8', 'carton_pk': 1092, 'program': 'SKY', 'version': '0.5.8', 'v1': 5.08, 'name': 'ops_sky_apogee_best', 'mapper': 'ops', 'alt_program': 'sky', 'alt_name': 'ops_sky'},
        211: {'label': 'ops_sky_apogee_good_0.5.8', 'carton_pk': 1093, 'program': 'SKY', 'version': '0.5.8', 'v1': 5.08, 'name': 'ops_sky_apogee_good', 'mapper': 'ops', 'alt_program': 'sky', 'alt_name': 'ops_sky'},
        212: {'label': 'manual_fps_position_stars_0.5.3', 'carton_pk': 1094, 'program': 'commissioning', 'version': '0.5.3', 'v1': 5.03, 'name': 'manual_fps_position_stars', 'mapper': 'ops', 'alt_program': 'commissioning', 'alt_name': 'manual_fps_position_stars_apogee'},
        213: {'label': 'ops_sky_boss_best_0.5.9', 'carton_pk': 1095, 'program': 'ops_sky', 'version': '0.5.9', 'v1': 5.09, 'name': 'ops_sky_boss_best', 'mapper': 'ops', 'alt_program': 'sky', 'alt_name': 'ops_sky'},
        214: {'label': 'ops_sky_boss_good_0.5.9', 'carton_pk': 1096, 'program': 'ops_sky', 'version': '0.5.9', 'v1': 5.09, 'name': 'ops_sky_boss_good', 'mapper': 'ops', 'alt_program': 'sky', 'alt_name': 'ops_sky'},
        215: {'label': 'ops_sky_apogee_best_0.5.9', 'carton_pk': 1097, 'program': 'ops_sky', 'version': '0.5.9', 'v1': 5.09, 'name': 'ops_sky_apogee_best', 'mapper': 'ops', 'alt_program': 'sky', 'alt_name': 'ops_sky'},
        216: {'label': 'ops_sky_apogee_good_0.5.9', 'carton_pk': 1098, 'program': 'ops_sky', 'version': '0.5.9', 'v1': 5.09, 'name': 'ops_sky_apogee_good', 'mapper': 'ops', 'alt_program': 'sky', 'alt_name': 'ops_sky'},
        217: {'label': 'mwm_tess_ob_0.5.11', 'carton_pk': 1104, 'program': 'mwm_tessob', 'version': '0.5.11', 'v1': 5.11, 'name': 'mwm_tess_ob', 'mapper': 'mwm', 'alt_program': 'tessob', 'alt_name': 'mwm_tess_ob'},
        218: {'label': 'manual_fps_position_stars_10_0.5.3', 'carton_pk': 1105, 'program': 'commissioning', 'version': '0.5.3', 'v1': 5.03, 'name': 'manual_fps_position_stars_10', 'mapper': 'ops', 'alt_program': 'commissioning', 'alt_name': 'manual_fps_position_stars_apogee'},
        219: {'label': 'ops_sky_boss_fallback_0.5.12', 'carton_pk': 1108, 'program': 'ops_sky', 'version': '0.5.12', 'v1': 5.12, 'name': 'ops_sky_boss_fallback', 'mapper': 'ops', 'alt_program': 'sky', 'alt_name': 'ops_sky'},
        220: {'label': 'openfibertargets_nov2020_34a_0.5.13', 'carton_pk': 1110, 'program': 'open_fiber', 'version': '0.5.13', 'v1': 5.13, 'name': 'openfibertargets_nov2020_34a', 'mapper': 'open', 'alt_program': 'open_fiber', 'alt_name': 'mwm_openfiber'},
        221: {'label': 'openfibertargets_nov2020_34b_0.5.13', 'carton_pk': 1111, 'program': 'open_fiber', 'version': '0.5.13', 'v1': 5.13, 'name': 'openfibertargets_nov2020_34b', 'mapper': 'open', 'alt_program': 'open_fiber', 'alt_name': 'mwm_openfiber'},
        222: {'label': 'bhm_csc_boss_0.5.14', 'carton_pk': 1112, 'program': 'bhm_csc', 'version': '0.5.14', 'v1': 5.14, 'name': 'bhm_csc_boss', 'mapper': 'bhm', 'alt_program': 'csc', 'alt_name': 'bhm_csc'},
        223: {'label': 'bhm_csc_boss_0.5.15', 'carton_pk': 1114, 'program': 'bhm_csc', 'version': '0.5.15', 'v1': 5.15, 'name': 'bhm_csc_boss', 'mapper': 'bhm', 'alt_program': 'csc', 'alt_name': 'bhm_csc'},
        224: {'label': 'bhm_csc_apogee_0.5.15', 'carton_pk': 1115, 'program': 'bhm_csc', 'version': '0.5.15', 'v1': 5.15, 'name': 'bhm_csc_apogee', 'mapper': 'bhm', 'alt_program': 'csc', 'alt_name': 'bhm_csc'},
        225: {'label': 'bhm_colr_galaxies_lsdr8_0.5.16', 'carton_pk': 1116, 'program': 'bhm_filler', 'version': '0.5.16', 'v1': 5.16, 'name': 'bhm_colr_galaxies_lsdr8', 'mapper': 'bhm', 'alt_program': 'filler', 'alt_name': 'bhm_filler'},
        226: {'label': 'mwm_yso_cluster_apogee_0.5.17', 'carton_pk': 1121, 'program': 'mwm_yso', 'version': '0.5.17', 'v1': 5.17, 'name': 'mwm_yso_cluster_apogee', 'mapper': 'mwm', 'alt_program': 'yso', 'alt_name': 'mwm_yso_cluster'},
        227: {'label': 'mwm_yso_cluster_boss_0.5.17', 'carton_pk': 1122, 'program': 'mwm_yso', 'version': '0.5.17', 'v1': 5.17, 'name': 'mwm_yso_cluster_boss', 'mapper': 'mwm', 'alt_program': 'yso', 'alt_name': 'mwm_yso_cluster'},
        228: {'label': 'mwm_yso_cmz_apogee_0.5.17', 'carton_pk': 1123, 'program': 'mwm_yso', 'version': '0.5.17', 'v1': 5.17, 'name': 'mwm_yso_cmz_apogee', 'mapper': 'mwm', 'alt_program': 'yso', 'alt_name': 'mwm_yso_cmz'},
        229: {'label': 'mwm_yso_disk_apogee_0.5.17', 'carton_pk': 1124, 'program': 'mwm_yso', 'version': '0.5.17', 'v1': 5.17, 'name': 'mwm_yso_disk_apogee', 'mapper': 'mwm', 'alt_program': 'yso', 'alt_name': 'mwm_yso_disk'},
        230: {'label': 'mwm_yso_disk_boss_0.5.17', 'carton_pk': 1125, 'program': 'mwm_yso', 'version': '0.5.17', 'v1': 5.17, 'name': 'mwm_yso_disk_boss', 'mapper': 'mwm', 'alt_program': 'yso', 'alt_name': 'mwm_yso_disk'},
        231: {'label': 'mwm_yso_embedded_apogee_0.5.17', 'carton_pk': 1126, 'program': 'mwm_yso', 'version': '0.5.17', 'v1': 5.17, 'name': 'mwm_yso_embedded_apogee', 'mapper': 'mwm', 'alt_program': 'yso', 'alt_name': 'mwm_yso_embedded'},
        232: {'label': 'mwm_yso_nebula_apogee_0.5.17', 'carton_pk': 1127, 'program': 'mwm_yso', 'version': '0.5.17', 'v1': 5.17, 'name': 'mwm_yso_nebula_apogee', 'mapper': 'mwm', 'alt_program': 'yso', 'alt_name': 'mwm_yso_nebula'},
        233: {'label': 'mwm_yso_variable_apogee_0.5.17', 'carton_pk': 1128, 'program': 'mwm_yso', 'version': '0.5.17', 'v1': 5.17, 'name': 'mwm_yso_variable_apogee', 'mapper': 'mwm', 'alt_program': 'yso', 'alt_name': 'mwm_yso_variable'},
        234: {'label': 'mwm_yso_variable_boss_0.5.17', 'carton_pk': 1129, 'program': 'mwm_yso', 'version': '0.5.17', 'v1': 5.17, 'name': 'mwm_yso_variable_boss', 'mapper': 'mwm', 'alt_program': 'yso', 'alt_name': 'mwm_yso_variable'},
        235: {'label': 'mwm_rv_long_fps_0.5.18', 'carton_pk': 1130, 'program': 'mwm_rv', 'version': '0.5.18', 'v1': 5.18, 'name': 'mwm_rv_long_fps', 'mapper': 'mwm', 'alt_program': 'bin', 'alt_name': 'mwm_bin_rv_long'},
        236: {'label': 'mwm_rv_short_fps_0.5.18', 'carton_pk': 1131, 'program': 'mwm_rv', 'version': '0.5.18', 'v1': 5.18, 'name': 'mwm_rv_short_fps', 'mapper': 'mwm', 'alt_program': 'bin', 'alt_name': 'mwm_bin_rv_short'},
        237: {'label': 'mwm_cb_300pc_apogee_0.5.19', 'carton_pk': 1132, 'program': 'mwm_cb', 'version': '0.5.19', 'v1': 5.19, 'name': 'mwm_cb_300pc_apogee', 'mapper': 'mwm', 'alt_program': 'cb', 'alt_name': 'mwm_cb_300pc'},
        238: {'label': 'mwm_cb_300pc_boss_0.5.19', 'carton_pk': 1133, 'program': 'mwm_cb', 'version': '0.5.19', 'v1': 5.19, 'name': 'mwm_cb_300pc_boss', 'mapper': 'mwm', 'alt_program': 'cb', 'alt_name': 'mwm_cb_300pc'},
        239: {'label': 'manual_mwm_tess_ob_0.5.13', 'carton_pk': 1134, 'program': 'mwm_tessob', 'version': '0.5.13', 'v1': 5.13, 'name': 'manual_mwm_tess_ob', 'mapper': 'mwm', 'alt_program': 'tess', 'alt_name': 'mwm_tess_ob'},
        240: {'label': 'manual_fps_position_stars_apogee_10_0.5.13', 'carton_pk': 1135, 'program': 'commissioning', 'version': '0.5.13', 'v1': 5.13, 'name': 'manual_fps_position_stars_apogee_10', 'mapper': 'ops', 'alt_program': 'commissioning', 'alt_name': 'manual_fps_position_stars_apogee'},
        241: {'label': 'manual_offset_mwmhalo_off00_0.5.13', 'carton_pk': 1137, 'program': 'commissioning', 'version': '0.5.13', 'v1': 5.13, 'name': 'manual_offset_mwmhalo_off00', 'mapper': 'ops', 'alt_program': 'commissioning', 'alt_name': 'manual_offset_mwmhalo'},
        242: {'label': 'manual_offset_mwmhalo_off05_0.5.13', 'carton_pk': 1138, 'program': 'commissioning', 'version': '0.5.13', 'v1': 5.13, 'name': 'manual_offset_mwmhalo_off05', 'mapper': 'ops', 'alt_program': 'commissioning', 'alt_name': 'manual_offset_mwmhalo'},
        243: {'label': 'manual_offset_mwmhalo_off10_0.5.13', 'carton_pk': 1139, 'program': 'commissioning', 'version': '0.5.13', 'v1': 5.13, 'name': 'manual_offset_mwmhalo_off10', 'mapper': 'ops', 'alt_program': 'commissioning', 'alt_name': 'manual_offset_mwmhalo'},
        244: {'label': 'manual_offset_mwmhalo_off20_0.5.13', 'carton_pk': 1140, 'program': 'commissioning', 'version': '0.5.13', 'v1': 5.13, 'name': 'manual_offset_mwmhalo_off20', 'mapper': 'ops', 'alt_program': 'commissioning', 'alt_name': 'manual_offset_mwmhalo'},
        245: {'label': 'manual_offset_mwmhalo_off30_0.5.13', 'carton_pk': 1141, 'program': 'commissioning', 'version': '0.5.13', 'v1': 5.13, 'name': 'manual_offset_mwmhalo_off30', 'mapper': 'ops', 'alt_program': 'commissioning', 'alt_name': 'manual_offset_mwmhalo'},
        246: {'label': 'manual_offset_mwmhalo_offa_0.5.13', 'carton_pk': 1142, 'program': 'commissioning', 'version': '0.5.13', 'v1': 5.13, 'name': 'manual_offset_mwmhalo_offa', 'mapper': 'ops', 'alt_program': 'commissioning', 'alt_name': 'manual_offset_mwmhalo'},
        247: {'label': 'manual_offset_mwmhalo_offb_0.5.13', 'carton_pk': 1143, 'program': 'commissioning', 'version': '0.5.13', 'v1': 5.13, 'name': 'manual_offset_mwmhalo_offb', 'mapper': 'ops', 'alt_program': 'commissioning', 'alt_name': 'manual_offset_mwmhalo'},
        248: {'label': 'manual_bright_target_offsets_3_0.5.20', 'carton_pk': 1158, 'program': 'mwm_ob', 'version': '0.5.20', 'v1': 5.2, 'name': 'manual_bright_target_offsets_3', 'mapper': 'ops', 'alt_program': 'commissioning', 'alt_name': 'mwm_ob_core'},
        249: {'label': 'ops_std_apogee_0.5.22', 'carton_pk': 1163, 'program': 'ops_std', 'version': '0.5.22', 'v1': 5.22, 'name': 'ops_std_apogee', 'mapper': 'ops', 'alt_program': 'std', 'alt_name': 'ops_std'},
        250: {'label': 'manual_bhm_spiders_comm_lco_0.5.23', 'carton_pk': 1165, 'program': 'commissioning', 'version': '0.5.23', 'v1': 5.23, 'name': 'manual_bhm_spiders_comm_lco', 'mapper': 'ops', 'alt_program': 'commissioning', 'alt_name': 'bhm_spiders'},
        251: {'label': 'manual_fps_position_stars_lco_apogee_10_0.5.23', 'carton_pk': 1166, 'program': 'commissioning', 'version': '0.5.23', 'v1': 5.23, 'name': 'manual_fps_position_stars_lco_apogee_10', 'mapper': 'ops', 'alt_program': 'commissioning', 'alt_name': 'manual_fps_position_stars_apogee'},
        252: {'label': 'bhm_spiders_agn_sep_1.0.5', 'carton_pk': 1253, 'program': 'bhm_spiders', 'version': '1.0.5', 'v1': 10.05, 'name': 'bhm_spiders_agn_sep', 'mapper': 'bhm', 'alt_program': 'spiders', 'alt_name': 'bhm_spiders'},
        253: {'label': 'ops_std_boss_lsdr10_1.0.5', 'carton_pk': 1263, 'program': 'ops_std', 'version': '1.0.5', 'v1': 10.05, 'name': 'ops_std_boss_lsdr10', 'mapper': 'ops', 'alt_program': 'std', 'alt_name': 'ops_std'},
        254: {'label': 'mwm_yso_cluster_apogee_1.0.6', 'carton_pk': 1267, 'program': 'mwm_yso', 'version': '1.0.6', 'v1': 10.06, 'name': 'mwm_yso_cluster_apogee', 'mapper': 'mwm', 'alt_program': 'yso', 'alt_name': 'mwm_yso_cluster'},
        255: {'label': 'mwm_yso_cluster_boss_1.0.6', 'carton_pk': 1268, 'program': 'mwm_yso', 'version': '1.0.6', 'v1': 10.06, 'name': 'mwm_yso_cluster_boss', 'mapper': 'mwm', 'alt_program': 'yso', 'alt_name': 'mwm_yso_cluster'},
        256: {'label': 'mwm_yso_disk_apogee_1.0.6', 'carton_pk': 1271, 'program': 'mwm_yso', 'version': '1.0.6', 'v1': 10.06, 'name': 'mwm_yso_disk_apogee', 'mapper': 'mwm', 'alt_program': 'yso', 'alt_name': 'mwm_yso_disk'},
        257: {'label': 'mwm_yso_disk_boss_1.0.6', 'carton_pk': 1272, 'program': 'mwm_yso', 'version': '1.0.6', 'v1': 10.06, 'name': 'mwm_yso_disk_boss', 'mapper': 'mwm', 'alt_program': 'yso', 'alt_name': 'mwm_yso_disk'},
        258: {'label': 'mwm_yso_cmz_apogee_1.0.6', 'carton_pk': 1273, 'program': 'mwm_yso', 'version': '1.0.6', 'v1': 10.06, 'name': 'mwm_yso_cmz_apogee', 'mapper': 'mwm', 'alt_program': 'yso', 'alt_name': 'mwm_yso_cmz'},
        259: {'label': 'mwm_yso_variable_apogee_1.0.6', 'carton_pk': 1274, 'program': 'mwm_yso', 'version': '1.0.6', 'v1': 10.06, 'name': 'mwm_yso_variable_apogee', 'mapper': 'mwm', 'alt_program': 'yso', 'alt_name': 'mwm_yso_variable'},
        260: {'label': 'mwm_yso_variable_boss_1.0.6', 'carton_pk': 1275, 'program': 'mwm_yso', 'version': '1.0.6', 'v1': 10.06, 'name': 'mwm_yso_variable_boss', 'mapper': 'mwm', 'alt_program': 'yso', 'alt_name': 'mwm_yso_variable'},
        261: {'label': 'mwm_yso_embedded_apogee_1.0.6', 'carton_pk': 1276, 'program': 'mwm_yso', 'version': '1.0.6', 'v1': 10.06, 'name': 'mwm_yso_embedded_apogee', 'mapper': 'mwm', 'alt_program': 'yso', 'alt_name': 'mwm_yso_embedded'},
        262: {'label': 'mwm_yso_pms_apogee_zari18pms_1.0.6', 'carton_pk': 1278, 'program': 'mwm_yso', 'version': '1.0.6', 'v1': 10.06, 'name': 'mwm_yso_pms_apogee_zari18pms', 'mapper': 'mwm', 'alt_program': 'yso', 'alt_name': 'mwm_yso_pms'},
        263: {'label': 'mwm_yso_pms_boss_sagitta_edr3_1.0.6', 'carton_pk': 1279, 'program': 'mwm_yso', 'version': '1.0.6', 'v1': 10.06, 'name': 'mwm_yso_pms_boss_sagitta_edr3', 'mapper': 'mwm', 'alt_program': 'yso', 'alt_name': 'mwm_yso_pms'},
        264: {'label': 'mwm_yso_pms_boss_zari18pms_1.0.6', 'carton_pk': 1280, 'program': 'mwm_yso', 'version': '1.0.6', 'v1': 10.06, 'name': 'mwm_yso_pms_boss_zari18pms', 'mapper': 'mwm', 'alt_program': 'yso', 'alt_name': 'mwm_yso_pms'},
        265: {'label': 'openfibertargets_nov2020_11_1.0.7', 'carton_pk': 1289, 'program': 'open_fiber', 'version': '1.0.7', 'v1': 10.07, 'name': 'openfibertargets_nov2020_11', 'mapper': 'open', 'alt_program': 'open_fiber', 'alt_name': 'bhm_openfiber'},
        266: {'label': 'openfibertargets_nov2020_18_1.0.7', 'carton_pk': 1290, 'program': 'open_fiber', 'version': '1.0.7', 'v1': 10.07, 'name': 'openfibertargets_nov2020_18', 'mapper': 'open', 'alt_program': 'open_fiber', 'alt_name': 'bhm_openfiber'},
        267: {'label': 'openfibertargets_nov2020_26_1.0.7', 'carton_pk': 1291, 'program': 'open_fiber', 'version': '1.0.7', 'v1': 10.07, 'name': 'openfibertargets_nov2020_26', 'mapper': 'open', 'alt_program': 'open_fiber', 'alt_name': 'bhm_openfiber'},
        268: {'label': 'openfibertargets_nov2020_27_1.0.7', 'carton_pk': 1292, 'program': 'open_fiber', 'version': '1.0.7', 'v1': 10.07, 'name': 'openfibertargets_nov2020_27', 'mapper': 'open', 'alt_program': 'open_fiber', 'alt_name': 'bhm_openfiber'},
        269: {'label': 'openfibertargets_nov2020_30_1.0.7', 'carton_pk': 1293, 'program': 'open_fiber', 'version': '1.0.7', 'v1': 10.07, 'name': 'openfibertargets_nov2020_30', 'mapper': 'open', 'alt_program': 'open_fiber', 'alt_name': 'bhm_openfiber'},
        270: {'label': 'mwm_yso_nebula_apogee_1.0.8', 'carton_pk': 1308, 'program': 'mwm_yso', 'version': '1.0.8', 'v1': 10.08, 'name': 'mwm_yso_nebula_apogee', 'mapper': 'mwm', 'alt_program': 'yso', 'alt_name': 'mwm_yso_nebula'},
        271: {'label': 'manual_mwm_halo_distant_kgiant_1.0.7', 'carton_pk': 1317, 'program': 'mwm_halo', 'version': '1.0.7', 'v1': 10.07, 'name': 'manual_mwm_halo_distant_kgiant', 'mapper': 'mwm', 'alt_program': 'halo', 'alt_name': 'manual_mwm_halo_distant_kgiant'},
        272: {'label': 'manual_mwm_halo_mp_bbb_1.0.7', 'carton_pk': 1318, 'program': 'mwm_halo', 'version': '1.0.7', 'v1': 10.07, 'name': 'manual_mwm_halo_mp_bbb', 'mapper': 'mwm', 'alt_program': 'halo', 'alt_name': 'manual_mwm_halo_mp_wise'},
        273: {'label': 'openfibertargets_nov2020_10_1.0.7', 'carton_pk': 1320, 'program': 'open_fiber', 'version': '1.0.7', 'v1': 10.07, 'name': 'openfibertargets_nov2020_10', 'mapper': 'open', 'alt_program': 'open_fiber', 'alt_name': 'mwm_bin_openfiber'},
        274: {'label': 'openfibertargets_nov2020_1000_1.0.7', 'carton_pk': 1321, 'program': 'open_fiber', 'version': '1.0.7', 'v1': 10.07, 'name': 'openfibertargets_nov2020_1000', 'mapper': 'open', 'alt_program': 'open_fiber', 'alt_name': 'mwm_cluster_openfiber'},
        275: {'label': 'openfibertargets_nov2020_12_1.0.7', 'carton_pk': 1322, 'program': 'open_fiber', 'version': '1.0.7', 'v1': 10.07, 'name': 'openfibertargets_nov2020_12', 'mapper': 'open', 'alt_program': 'open_fiber', 'alt_name': 'mwm_bin_openfiber'},
        276: {'label': 'openfibertargets_nov2020_14_1.0.7', 'carton_pk': 1323, 'program': 'open_fiber', 'version': '1.0.7', 'v1': 10.07, 'name': 'openfibertargets_nov2020_14', 'mapper': 'open', 'alt_program': 'open_fiber', 'alt_name': 'mwm_bin_openfiber'},
        277: {'label': 'openfibertargets_nov2020_15_1.0.7', 'carton_pk': 1324, 'program': 'open_fiber', 'version': '1.0.7', 'v1': 10.07, 'name': 'openfibertargets_nov2020_15', 'mapper': 'open', 'alt_program': 'open_fiber', 'alt_name': 'mwm_cluster_openfiber'},
        278: {'label': 'openfibertargets_nov2020_22_1.0.7', 'carton_pk': 1325, 'program': 'open_fiber', 'version': '1.0.7', 'v1': 10.07, 'name': 'openfibertargets_nov2020_22', 'mapper': 'open', 'alt_program': 'open_fiber', 'alt_name': 'mwm_bin_openfiber'},
        279: {'label': 'openfibertargets_nov2020_24_1.0.7', 'carton_pk': 1326, 'program': 'open_fiber', 'version': '1.0.7', 'v1': 10.07, 'name': 'openfibertargets_nov2020_24', 'mapper': 'open', 'alt_program': 'open_fiber', 'alt_name': 'mwm_snc_openfiber'},
        280: {'label': 'openfibertargets_nov2020_29_1.0.7', 'carton_pk': 1327, 'program': 'open_fiber', 'version': '1.0.7', 'v1': 10.07, 'name': 'openfibertargets_nov2020_29', 'mapper': 'open', 'alt_program': 'open_fiber', 'alt_name': 'mwm_cluster_openfiber'},
        281: {'label': 'openfibertargets_nov2020_3_1.0.7', 'carton_pk': 1328, 'program': 'open_fiber', 'version': '1.0.7', 'v1': 10.07, 'name': 'openfibertargets_nov2020_3', 'mapper': 'open', 'alt_program': 'open_fiber', 'alt_name': 'mwm_bin_openfiber'},
        282: {'label': 'openfibertargets_nov2020_31_1.0.7', 'carton_pk': 1329, 'program': 'open_fiber', 'version': '1.0.7', 'v1': 10.07, 'name': 'openfibertargets_nov2020_31', 'mapper': 'open', 'alt_program': 'open_fiber', 'alt_name': 'mwm_validation_openfiber'},
        283: {'label': 'openfibertargets_nov2020_34a_1.0.7', 'carton_pk': 1330, 'program': 'open_fiber', 'version': '1.0.7', 'v1': 10.07, 'name': 'openfibertargets_nov2020_34a', 'mapper': 'open', 'alt_program': 'open_fiber', 'alt_name': 'mwm_openfiber'},
        284: {'label': 'openfibertargets_nov2020_34b_1.0.7', 'carton_pk': 1331, 'program': 'open_fiber', 'version': '1.0.7', 'v1': 10.07, 'name': 'openfibertargets_nov2020_34b', 'mapper': 'open', 'alt_program': 'open_fiber', 'alt_name': 'mwm_openfiber'},
        285: {'label': 'openfibertargets_nov2020_35b_1.0.7', 'carton_pk': 1332, 'program': 'open_fiber', 'version': '1.0.7', 'v1': 10.07, 'name': 'openfibertargets_nov2020_35b', 'mapper': 'open', 'alt_program': 'open_fiber', 'alt_name': 'mwm_halo_openfiber'},
        286: {'label': 'openfibertargets_nov2020_35c_1.0.7', 'carton_pk': 1333, 'program': 'open_fiber', 'version': '1.0.7', 'v1': 10.07, 'name': 'openfibertargets_nov2020_35c', 'mapper': 'open', 'alt_program': 'open_fiber', 'alt_name': 'mwm_halo_openfiber'},
        287: {'label': 'openfibertargets_nov2020_46_1.0.7', 'carton_pk': 1334, 'program': 'open_fiber', 'version': '1.0.7', 'v1': 10.07, 'name': 'openfibertargets_nov2020_46', 'mapper': 'open', 'alt_program': 'open_fiber', 'alt_name': 'mwm_bin_openfiber'},
        288: {'label': 'openfibertargets_nov2020_5_1.0.7', 'carton_pk': 1335, 'program': 'open_fiber', 'version': '1.0.7', 'v1': 10.07, 'name': 'openfibertargets_nov2020_5', 'mapper': 'open', 'alt_program': 'open_fiber', 'alt_name': 'mwm_halo_openfiber'},
        289: {'label': 'openfibertargets_nov2020_6a_1.0.7', 'carton_pk': 1336, 'program': 'open_fiber', 'version': '1.0.7', 'v1': 10.07, 'name': 'openfibertargets_nov2020_6a', 'mapper': 'open', 'alt_program': 'open_fiber', 'alt_name': 'mwm_halo_openfiber'},
        290: {'label': 'openfibertargets_nov2020_6b_1.0.7', 'carton_pk': 1337, 'program': 'open_fiber', 'version': '1.0.7', 'v1': 10.07, 'name': 'openfibertargets_nov2020_6b', 'mapper': 'open', 'alt_program': 'open_fiber', 'alt_name': 'mwm_halo_openfiber'},
        291: {'label': 'openfibertargets_nov2020_6c_1.0.7', 'carton_pk': 1338, 'program': 'open_fiber', 'version': '1.0.7', 'v1': 10.07, 'name': 'openfibertargets_nov2020_6c', 'mapper': 'open', 'alt_program': 'open_fiber', 'alt_name': 'mwm_halo_openfiber'},
        292: {'label': 'openfibertargets_nov2020_8_1.0.7', 'carton_pk': 1339, 'program': 'open_fiber', 'version': '1.0.7', 'v1': 10.07, 'name': 'openfibertargets_nov2020_8', 'mapper': 'open', 'alt_program': 'open_fiber', 'alt_name': 'mwm_cluster_openfiber'},
        293: {'label': 'openfibertargets_nov2020_9_1.0.7', 'carton_pk': 1340, 'program': 'open_fiber', 'version': '1.0.7', 'v1': 10.07, 'name': 'openfibertargets_nov2020_9', 'mapper': 'open', 'alt_program': 'open_fiber', 'alt_name': 'mwm_cluster_openfiber'},
        294: {'label': 'openfibertargets_nov2020_28a_1.0.7', 'carton_pk': 1344, 'program': 'open_fiber', 'version': '1.0.7', 'v1': 10.07, 'name': 'openfibertargets_nov2020_28a', 'mapper': 'open', 'alt_program': 'open_fiber', 'alt_name': 'manual_mwm_halo_distant_kgiant'},
        295: {'label': 'openfibertargets_nov2020_33_1.0.10', 'carton_pk': 1358, 'program': 'open_fiber', 'version': '1.0.10', 'v1': 10.1, 'name': 'openfibertargets_nov2020_33', 'mapper': 'open', 'alt_program': 'open_fiber', 'alt_name': 'bhm_openfiber'},
        296: {'label': 'bhm_rm_core_1.0.12', 'carton_pk': 1359, 'program': 'bhm_rm', 'version': '1.0.12', 'v1': 10.12, 'name': 'bhm_rm_core', 'mapper': 'bhm', 'alt_program': 'rm', 'alt_name': 'bhm_rm'},
        297: {'label': 'bhm_rm_known_spec_1.0.12', 'carton_pk': 1360, 'program': 'bhm_rm', 'version': '1.0.12', 'v1': 10.12, 'name': 'bhm_rm_known_spec', 'mapper': 'bhm', 'alt_program': 'rm', 'alt_name': 'bhm_rm'},
        298: {'label': 'bhm_rm_var_1.0.12', 'carton_pk': 1361, 'program': 'bhm_rm', 'version': '1.0.12', 'v1': 10.12, 'name': 'bhm_rm_var', 'mapper': 'bhm', 'alt_program': 'rm', 'alt_name': 'bhm_rm'},
        299: {'label': 'bhm_rm_ancillary_1.0.12', 'carton_pk': 1362, 'program': 'bhm_rm', 'version': '1.0.12', 'v1': 10.12, 'name': 'bhm_rm_ancillary', 'mapper': 'bhm', 'alt_program': 'rm', 'alt_name': 'bhm_rm'},
        300: {'label': 'bhm_rm_xrayqso_1.0.12', 'carton_pk': 1363, 'program': 'bhm_rm', 'version': '1.0.12', 'v1': 10.12, 'name': 'bhm_rm_xrayqso', 'mapper': 'bhm', 'alt_program': 'rm', 'alt_name': 'bhm_rm'},
        301: {'label': 'manual_mwm_magcloud_massive_apogee_1.0.10', 'carton_pk': 1367, 'program': 'mwm_magcloud', 'version': '1.0.10', 'v1': 10.1, 'name': 'manual_mwm_magcloud_massive_apogee', 'mapper': 'mwm', 'alt_program': 'magcloud', 'alt_name': 'mwm_magcloud_massive'},
        302: {'label': 'manual_mwm_magcloud_massive_boss_1.0.10', 'carton_pk': 1368, 'program': 'mwm_magcloud', 'version': '1.0.10', 'v1': 10.1, 'name': 'manual_mwm_magcloud_massive_boss', 'mapper': 'mwm', 'alt_program': 'magcloud', 'alt_name': 'mwm_magcloud_massive'},
        303: {'label': 'manual_mwm_magcloud_symbiotic_apogee_1.0.10', 'carton_pk': 1369, 'program': 'mwm_magcloud', 'version': '1.0.10', 'v1': 10.1, 'name': 'manual_mwm_magcloud_symbiotic_apogee', 'mapper': 'mwm', 'alt_program': 'magcloud', 'alt_name': 'mwm_magcloud_symbiotic'},
        304: {'label': 'ops_std_boss_gdr2_1.0.13', 'carton_pk': 1370, 'program': 'ops_std', 'version': '1.0.13', 'v1': 10.13, 'name': 'ops_std_boss_gdr2', 'mapper': 'ops', 'alt_program': 'std', 'alt_name': 'ops_std'},
        305: {'label': 'ops_std_apogee_1.0.14', 'carton_pk': 1371, 'program': 'ops_std', 'version': '1.0.14', 'v1': 10.14, 'name': 'ops_std_apogee', 'mapper': 'ops', 'alt_program': 'std', 'alt_name': 'ops_std'},
        306: {'label': 'ops_std_eboss_1.0.15', 'carton_pk': 1372, 'program': 'ops_std', 'version': '1.0.15', 'v1': 10.15, 'name': 'ops_std_eboss', 'mapper': 'ops', 'alt_program': 'std', 'alt_name': 'ops_std'},
        307: {'label': 'ops_std_boss_1.0.16', 'carton_pk': 1374, 'program': 'ops_std', 'version': '1.0.16', 'v1': 10.16, 'name': 'ops_std_boss', 'mapper': 'ops', 'alt_program': 'std', 'alt_name': 'ops_std'},
        308: {'label': 'ops_std_boss_red_1.0.16', 'carton_pk': 1375, 'program': 'ops_std', 'version': '1.0.16', 'v1': 10.16, 'name': 'ops_std_boss_red', 'mapper': 'ops', 'alt_program': 'std', 'alt_name': 'ops_std'},
        309: {'label': 'ops_std_boss_tic_1.0.16', 'carton_pk': 1376, 'program': 'ops_std', 'version': '1.0.16', 'v1': 10.16, 'name': 'ops_std_boss_tic', 'mapper': 'ops', 'alt_program': 'std', 'alt_name': 'ops_std'},
        310: {'label': 'mwm_snc_100pc_apogee_1.0.17', 'carton_pk': 1378, 'program': 'mwm_snc', 'version': '1.0.17', 'v1': 10.17, 'name': 'mwm_snc_100pc_apogee', 'mapper': 'mwm', 'alt_program': 'snc', 'alt_name': 'mwm_snc'},
        311: {'label': 'mwm_snc_100pc_boss_1.0.17', 'carton_pk': 1379, 'program': 'mwm_snc', 'version': '1.0.17', 'v1': 10.17, 'name': 'mwm_snc_100pc_boss', 'mapper': 'mwm', 'alt_program': 'snc', 'alt_name': 'mwm_snc'},
        312: {'label': 'mwm_bin_gaia_astb_apogee_1.0.19', 'carton_pk': 1400, 'program': 'mwm_bin', 'version': '1.0.19', 'v1': 10.19, 'name': 'mwm_bin_gaia_astb_apogee', 'mapper': 'mwm', 'alt_program': 'bin', 'alt_name': 'mwm_bin_gaia_astb'},
        313: {'label': 'mwm_bin_gaia_astb_boss_1.0.19', 'carton_pk': 1401, 'program': 'mwm_bin', 'version': '1.0.19', 'v1': 10.19, 'name': 'mwm_bin_gaia_astb_boss', 'mapper': 'mwm', 'alt_program': 'bin', 'alt_name': 'mwm_bin_gaia_astb'},
        314: {'label': 'mwm_bin_gaia_sb_apogee_1.0.19', 'carton_pk': 1402, 'program': 'mwm_bin', 'version': '1.0.19', 'v1': 10.19, 'name': 'mwm_bin_gaia_sb_apogee', 'mapper': 'mwm', 'alt_program': 'bin', 'alt_name': 'mwm_bin_gaia_sb'},
        315: {'label': 'mwm_bin_gaia_sb_boss_1.0.19', 'carton_pk': 1403, 'program': 'mwm_bin', 'version': '1.0.19', 'v1': 10.19, 'name': 'mwm_bin_gaia_sb_boss', 'mapper': 'mwm', 'alt_program': 'bin', 'alt_name': 'mwm_bin_gaia_sb'},
        316: {'label': 'mwm_yso_pms_apogee_sagitta_edr3_1.0.20', 'carton_pk': 1412, 'program': 'mwm_yso', 'version': '1.0.20', 'v1': 10.2, 'name': 'mwm_yso_pms_apogee_sagitta_edr3', 'mapper': 'mwm', 'alt_program': 'yso', 'alt_name': 'mwm_yso_pms'},
        317: {'label': 'mwm_snc_100pc_boss_1.0.24', 'carton_pk': 1427, 'program': 'mwm_snc', 'version': '1.0.24', 'v1': 10.24, 'name': 'mwm_snc_100pc_boss', 'mapper': 'mwm', 'alt_program': 'snc', 'alt_name': 'mwm_snc'},
        318: {'label': 'mwm_snc_100pc_boss_1.0.28', 'carton_pk': 1448, 'program': 'mwm_snc', 'version': '1.0.28', 'v1': 10.28, 'name': 'mwm_snc_100pc_boss', 'mapper': 'mwm', 'alt_program': 'snc', 'alt_name': 'mwm_snc'},
        319: {'label': 'mwm_yso_disk_apogee_single_1.0.33', 'carton_pk': 1462, 'program': 'mwm_yso', 'version': '1.0.33', 'v1': 10.33, 'name': 'mwm_yso_disk_apogee_single', 'mapper': 'mwm', 'alt_program': 'yso', 'alt_name': 'mwm_yso_disk'},
        320: {'label': 'mwm_yso_disk_boss_single_1.0.33', 'carton_pk': 1463, 'program': 'mwm_yso', 'version': '1.0.33', 'v1': 10.33, 'name': 'mwm_yso_disk_boss_single', 'mapper': 'mwm', 'alt_program': 'yso', 'alt_name': 'mwm_yso_disk'},
        321: {'label': 'mwm_yso_embedded_apogee_single_1.0.33', 'carton_pk': 1464, 'program': 'mwm_yso', 'version': '1.0.33', 'v1': 10.33, 'name': 'mwm_yso_embedded_apogee_single', 'mapper': 'mwm', 'alt_program': 'yso', 'alt_name': 'mwm_yso_embedded'},
        322: {'label': 'mwm_yso_nebula_apogee_single_1.0.33', 'carton_pk': 1465, 'program': 'mwm_yso', 'version': '1.0.33', 'v1': 10.33, 'name': 'mwm_yso_nebula_apogee_single', 'mapper': 'mwm', 'alt_program': 'yso', 'alt_name': 'mwm_yso_nebula'},
        323: {'label': 'mwm_yso_variable_apogee_single_1.0.33', 'carton_pk': 1466, 'program': 'mwm_yso', 'version': '1.0.33', 'v1': 10.33, 'name': 'mwm_yso_variable_apogee_single', 'mapper': 'mwm', 'alt_program': 'yso', 'alt_name': 'mwm_yso_variable'},
        324: {'label': 'mwm_yso_variable_boss_single_1.0.33', 'carton_pk': 1467, 'program': 'mwm_yso', 'version': '1.0.33', 'v1': 10.33, 'name': 'mwm_yso_variable_boss_single', 'mapper': 'mwm', 'alt_program': 'yso', 'alt_name': 'mwm_yso_variable'},
        325: {'label': 'mwm_yso_cmz_apogee_single_1.0.33', 'carton_pk': 1468, 'program': 'mwm_yso', 'version': '1.0.33', 'v1': 10.33, 'name': 'mwm_yso_cmz_apogee_single', 'mapper': 'mwm', 'alt_program': 'yso', 'alt_name': 'mwm_yso_cmz'},
        326: {'label': 'mwm_yso_cluster_apogee_single_1.0.33', 'carton_pk': 1469, 'program': 'mwm_yso', 'version': '1.0.33', 'v1': 10.33, 'name': 'mwm_yso_cluster_apogee_single', 'mapper': 'mwm', 'alt_program': 'yso', 'alt_name': 'mwm_yso_cluster'},
        327: {'label': 'mwm_yso_cluster_boss_single_1.0.33', 'carton_pk': 1470, 'program': 'mwm_yso', 'version': '1.0.33', 'v1': 10.33, 'name': 'mwm_yso_cluster_boss_single', 'mapper': 'mwm', 'alt_program': 'yso', 'alt_name': 'mwm_yso_cluster'},
        328: {'label': 'mwm_yso_pms_apogee_sagitta_edr3_single_1.0.33', 'carton_pk': 1471, 'program': 'mwm_yso', 'version': '1.0.33', 'v1': 10.33, 'name': 'mwm_yso_pms_apogee_sagitta_edr3_single', 'mapper': 'mwm', 'alt_program': 'yso', 'alt_name': 'mwm_yso_pms'},
        329: {'label': 'mwm_yso_pms_apogee_zari18pms_single_1.0.33', 'carton_pk': 1472, 'program': 'mwm_yso', 'version': '1.0.33', 'v1': 10.33, 'name': 'mwm_yso_pms_apogee_zari18pms_single', 'mapper': 'mwm', 'alt_program': 'yso', 'alt_name': 'mwm_yso_pms'},
        330: {'label': 'mwm_yso_pms_boss_sagitta_edr3_single_1.0.33', 'carton_pk': 1473, 'program': 'mwm_yso', 'version': '1.0.33', 'v1': 10.33, 'name': 'mwm_yso_pms_boss_sagitta_edr3_single', 'mapper': 'mwm', 'alt_program': 'yso', 'alt_name': 'mwm_yso_pms'},
        331: {'label': 'mwm_yso_pms_boss_zari18pms_single_1.0.33', 'carton_pk': 1474, 'program': 'mwm_yso', 'version': '1.0.33', 'v1': 10.33, 'name': 'mwm_yso_pms_boss_zari18pms_single', 'mapper': 'mwm', 'alt_program': 'yso', 'alt_name': 'mwm_yso_pms'},
        332: {'label': 'ops_std_boss_ps1dr2_1.0.29', 'carton_pk': 1475, 'program': 'ops_std', 'version': '1.0.29', 'v1': 10.29, 'name': 'ops_std_boss_ps1dr2', 'mapper': 'ops', 'alt_program': 'std', 'alt_name': 'ops_std'},
        333: {'label': 'bhm_csc_boss_1.0.37', 'carton_pk': 1498, 'program': 'bhm_csc', 'version': '1.0.37', 'v1': 10.37, 'name': 'bhm_csc_boss', 'mapper': 'bhm', 'alt_program': 'csc', 'alt_name': 'bhm_csc'},
        334: {'label': 'bhm_csc_apogee_1.0.37', 'carton_pk': 1499, 'program': 'bhm_csc', 'version': '1.0.37', 'v1': 10.37, 'name': 'bhm_csc_apogee', 'mapper': 'bhm', 'alt_program': 'csc', 'alt_name': 'bhm_csc'},
        335: {'label': 'bhm_gua_dark_1.0.37', 'carton_pk': 1500, 'program': 'bhm_filler', 'version': '1.0.37', 'v1': 10.37, 'name': 'bhm_gua_dark', 'mapper': 'bhm', 'alt_program': 'filler', 'alt_name': 'bhm_filler'},
        336: {'label': 'bhm_gua_bright_1.0.37', 'carton_pk': 1501, 'program': 'bhm_filler', 'version': '1.0.37', 'v1': 10.37, 'name': 'bhm_gua_bright', 'mapper': 'bhm', 'alt_program': 'filler', 'alt_name': 'bhm_filler'},
        337: {'label': 'bhm_spiders_clusters_lsdr10_1.0.37', 'carton_pk': 1502, 'program': 'bhm_spiders', 'version': '1.0.37', 'v1': 10.37, 'name': 'bhm_spiders_clusters_lsdr10', 'mapper': 'bhm', 'alt_program': 'spiders', 'alt_name': 'bhm_spiders'},
        338: {'label': 'bhm_spiders_agn_lsdr10_1.0.37', 'carton_pk': 1503, 'program': 'bhm_spiders', 'version': '1.0.37', 'v1': 10.37, 'name': 'bhm_spiders_agn_lsdr10', 'mapper': 'bhm', 'alt_program': 'spiders', 'alt_name': 'bhm_spiders'},
        339: {'label': 'bhm_spiders_agn_hard_1.0.37', 'carton_pk': 1504, 'program': 'bhm_spiders', 'version': '1.0.37', 'v1': 10.37, 'name': 'bhm_spiders_agn_hard', 'mapper': 'bhm', 'alt_program': 'spiders', 'alt_name': 'bhm_spiders'},
        340: {'label': 'bhm_spiders_agn_gaiadr3_1.0.37', 'carton_pk': 1505, 'program': 'bhm_spiders', 'version': '1.0.37', 'v1': 10.37, 'name': 'bhm_spiders_agn_gaiadr3', 'mapper': 'bhm', 'alt_program': 'spiders', 'alt_name': 'bhm_spiders'},
        341: {'label': 'bhm_spiders_agn_tda_1.0.37', 'carton_pk': 1506, 'program': 'bhm_spiders', 'version': '1.0.37', 'v1': 10.37, 'name': 'bhm_spiders_agn_tda', 'mapper': 'bhm', 'alt_program': 'spiders', 'alt_name': 'bhm_spiders'},
        342: {'label': 'bhm_spiders_agn_sep_1.0.37', 'carton_pk': 1507, 'program': 'bhm_spiders', 'version': '1.0.37', 'v1': 10.37, 'name': 'bhm_spiders_agn_sep', 'mapper': 'bhm', 'alt_program': 'spiders', 'alt_name': 'bhm_spiders'},
        343: {'label': 'bhm_aqmes_med_1.0.37', 'carton_pk': 1508, 'program': 'bhm_aqmes', 'version': '1.0.37', 'v1': 10.37, 'name': 'bhm_aqmes_med', 'mapper': 'bhm', 'alt_program': 'aqmes', 'alt_name': 'bhm_aqmes'},
        344: {'label': 'bhm_aqmes_med_faint_1.0.37', 'carton_pk': 1509, 'program': 'bhm_filler', 'version': '1.0.37', 'v1': 10.37, 'name': 'bhm_aqmes_med_faint', 'mapper': 'bhm', 'alt_program': 'filler', 'alt_name': 'bhm_aqmes'},
        345: {'label': 'bhm_aqmes_wide2_1.0.37', 'carton_pk': 1510, 'program': 'bhm_aqmes', 'version': '1.0.37', 'v1': 10.37, 'name': 'bhm_aqmes_wide2', 'mapper': 'bhm', 'alt_program': 'aqmes', 'alt_name': 'bhm_aqmes'},
        346: {'label': 'bhm_aqmes_wide2_faint_1.0.37', 'carton_pk': 1511, 'program': 'bhm_filler', 'version': '1.0.37', 'v1': 10.37, 'name': 'bhm_aqmes_wide2_faint', 'mapper': 'bhm', 'alt_program': 'filler', 'alt_name': 'bhm_aqmes'},
        347: {'label': 'bhm_aqmes_bonus_core_1.0.37', 'carton_pk': 1515, 'program': 'bhm_filler', 'version': '1.0.37', 'v1': 10.37, 'name': 'bhm_aqmes_bonus_core', 'mapper': 'bhm', 'alt_program': 'filler', 'alt_name': 'bhm_aqmes'},
        348: {'label': 'bhm_aqmes_bonus_bright_1.0.37', 'carton_pk': 1516, 'program': 'bhm_filler', 'version': '1.0.37', 'v1': 10.37, 'name': 'bhm_aqmes_bonus_bright', 'mapper': 'bhm', 'alt_program': 'filler', 'alt_name': 'bhm_aqmes'},
        349: {'label': 'bhm_aqmes_bonus_faint_1.0.37', 'carton_pk': 1517, 'program': 'bhm_filler', 'version': '1.0.37', 'v1': 10.37, 'name': 'bhm_aqmes_bonus_faint', 'mapper': 'bhm', 'alt_program': 'filler', 'alt_name': 'bhm_aqmes'},
        350: {'label': 'manual_mwm_crosscalib_apogee_1.0.35', 'carton_pk': 1525, 'program': 'mwm_validation', 'version': '1.0.35', 'v1': 10.35, 'name': 'manual_mwm_crosscalib_apogee', 'mapper': 'mwm', 'alt_program': 'validation', 'alt_name': 'mwm_crosscalib'},
        351: {'label': 'manual_mwm_crosscalib_yso_apogee_1.0.35', 'carton_pk': 1526, 'program': 'mwm_validation', 'version': '1.0.35', 'v1': 10.35, 'name': 'manual_mwm_crosscalib_yso_apogee', 'mapper': 'mwm', 'alt_program': 'validation', 'alt_name': 'mwm_crosscalib_yso'},
        352: {'label': 'manual_mwm_crosscalib_yso_boss_1.0.35', 'carton_pk': 1527, 'program': 'mwm_validation', 'version': '1.0.35', 'v1': 10.35, 'name': 'manual_mwm_crosscalib_yso_boss', 'mapper': 'mwm', 'alt_program': 'validation', 'alt_name': 'mwm_crosscalib_yso'},
        353: {'label': 'manual_mwm_halo_distant_bhb_boss_1.0.35', 'carton_pk': 1528, 'program': 'mwm_halo', 'version': '1.0.35', 'v1': 10.35, 'name': 'manual_mwm_halo_distant_bhb_boss', 'mapper': 'mwm', 'alt_program': 'halo', 'alt_name': 'manual_mwm_halo_distant_bhb'},
        354: {'label': 'manual_mwm_halo_distant_bhb_boss_single_1.0.35', 'carton_pk': 1529, 'program': 'mwm_halo', 'version': '1.0.35', 'v1': 10.35, 'name': 'manual_mwm_halo_distant_bhb_boss_single', 'mapper': 'mwm', 'alt_program': 'halo', 'alt_name': 'manual_mwm_halo_distant_bhb'},
        355: {'label': 'manual_mwm_halo_distant_kgiant_far_boss_1.0.35', 'carton_pk': 1530, 'program': 'mwm_halo', 'version': '1.0.35', 'v1': 10.35, 'name': 'manual_mwm_halo_distant_kgiant_far_boss', 'mapper': 'mwm', 'alt_program': 'halo', 'alt_name': 'manual_mwm_halo_distant_kgiant'},
        356: {'label': 'manual_mwm_halo_distant_kgiant_far_boss_single_1.0.35', 'carton_pk': 1531, 'program': 'mwm_halo', 'version': '1.0.35', 'v1': 10.35, 'name': 'manual_mwm_halo_distant_kgiant_far_boss_single', 'mapper': 'mwm', 'alt_program': 'halo', 'alt_name': 'manual_mwm_halo_distant_kgiant'},
        357: {'label': 'manual_mwm_halo_distant_kgiant_near_boss_1.0.35', 'carton_pk': 1532, 'program': 'mwm_halo', 'version': '1.0.35', 'v1': 10.35, 'name': 'manual_mwm_halo_distant_kgiant_near_boss', 'mapper': 'mwm', 'alt_program': 'halo', 'alt_name': 'manual_mwm_halo_distant_kgiant'},
        358: {'label': 'manual_mwm_halo_distant_kgiant_near_boss_single_1.0.35', 'carton_pk': 1533, 'program': 'mwm_halo', 'version': '1.0.35', 'v1': 10.35, 'name': 'manual_mwm_halo_distant_kgiant_near_boss_single', 'mapper': 'mwm', 'alt_program': 'halo', 'alt_name': 'manual_mwm_halo_distant_kgiant'},
        359: {'label': 'manual_mwm_halo_mp_wise_apogee_1.0.35', 'carton_pk': 1534, 'program': 'mwm_halo', 'version': '1.0.35', 'v1': 10.35, 'name': 'manual_mwm_halo_mp_wise_apogee', 'mapper': 'mwm', 'alt_program': 'halo', 'alt_name': 'manual_mwm_halo_mp_wise'},
        360: {'label': 'manual_mwm_halo_mp_wise_apogee_single_1.0.35', 'carton_pk': 1535, 'program': 'mwm_halo', 'version': '1.0.35', 'v1': 10.35, 'name': 'manual_mwm_halo_mp_wise_apogee_single', 'mapper': 'mwm', 'alt_program': 'halo', 'alt_name': 'manual_mwm_halo_mp_wise'},
        361: {'label': 'manual_mwm_halo_mp_wise_boss_1.0.35', 'carton_pk': 1536, 'program': 'mwm_halo', 'version': '1.0.35', 'v1': 10.35, 'name': 'manual_mwm_halo_mp_wise_boss', 'mapper': 'mwm', 'alt_program': 'halo', 'alt_name': 'manual_mwm_halo_mp_wise'},
        362: {'label': 'manual_mwm_halo_mp_wise_boss_single_1.0.35', 'carton_pk': 1537, 'program': 'mwm_halo', 'version': '1.0.35', 'v1': 10.35, 'name': 'manual_mwm_halo_mp_wise_boss_single', 'mapper': 'mwm', 'alt_program': 'halo', 'alt_name': 'manual_mwm_halo_mp_wise'},
        363: {'label': 'manual_mwm_halo_vmp_wise_apogee_1.0.35', 'carton_pk': 1538, 'program': 'mwm_halo', 'version': '1.0.35', 'v1': 10.35, 'name': 'manual_mwm_halo_vmp_wise_apogee', 'mapper': 'mwm', 'alt_program': 'halo', 'alt_name': 'manual_mwm_halo_mp_wise'},
        364: {'label': 'manual_mwm_halo_vmp_wise_apogee_single_1.0.35', 'carton_pk': 1539, 'program': 'mwm_halo', 'version': '1.0.35', 'v1': 10.35, 'name': 'manual_mwm_halo_vmp_wise_apogee_single', 'mapper': 'mwm', 'alt_program': 'halo', 'alt_name': 'manual_mwm_halo_mp_wise'},
        365: {'label': 'manual_mwm_halo_vmp_wise_boss_1.0.35', 'carton_pk': 1540, 'program': 'mwm_halo', 'version': '1.0.35', 'v1': 10.35, 'name': 'manual_mwm_halo_vmp_wise_boss', 'mapper': 'mwm', 'alt_program': 'halo', 'alt_name': 'manual_mwm_halo_mp_wise'},
        366: {'label': 'manual_mwm_halo_vmp_wise_boss_single_1.0.35', 'carton_pk': 1541, 'program': 'mwm_halo', 'version': '1.0.35', 'v1': 10.35, 'name': 'manual_mwm_halo_vmp_wise_boss_single', 'mapper': 'mwm', 'alt_program': 'halo', 'alt_name': 'manual_mwm_halo_mp_wise'},
        367: {'label': 'manual_mwm_tess_ob_apogee_1.0.35', 'carton_pk': 1554, 'program': 'mwm_tessob', 'version': '1.0.35', 'v1': 10.35, 'name': 'manual_mwm_tess_ob_apogee', 'mapper': 'mwm', 'alt_program': 'tess', 'alt_name': 'mwm_tess_ob'},
        368: {'label': 'bhm_colr_galaxies_lsdr10_1.0.38', 'carton_pk': 1555, 'program': 'bhm_filler', 'version': '1.0.38', 'v1': 10.38, 'name': 'bhm_colr_galaxies_lsdr10', 'mapper': 'bhm', 'alt_program': 'filler', 'alt_name': 'bhm_filler'},
        369: {'label': 'manual_mwm_validation_cool_apogee_1.0.35', 'carton_pk': 1556, 'program': 'mwm_validation', 'version': '1.0.35', 'v1': 10.35, 'name': 'manual_mwm_validation_cool_apogee', 'mapper': 'mwm', 'alt_program': 'validation', 'alt_name': 'mwm_validation_cool'},
        370: {'label': 'manual_mwm_validation_cool_boss_1.0.35', 'carton_pk': 1557, 'program': 'mwm_validation', 'version': '1.0.35', 'v1': 10.35, 'name': 'manual_mwm_validation_cool_boss', 'mapper': 'mwm', 'alt_program': 'validation', 'alt_name': 'mwm_validation_cool'},
        371: {'label': 'manual_mwm_validation_hot_apogee_1.0.35', 'carton_pk': 1558, 'program': 'mwm_validation', 'version': '1.0.35', 'v1': 10.35, 'name': 'manual_mwm_validation_hot_apogee', 'mapper': 'mwm', 'alt_program': 'validation', 'alt_name': 'mwm_validation_hot'},
        372: {'label': 'manual_mwm_validation_hot_boss_1.0.35', 'carton_pk': 1559, 'program': 'mwm_validation', 'version': '1.0.35', 'v1': 10.35, 'name': 'manual_mwm_validation_hot_boss', 'mapper': 'mwm', 'alt_program': 'validation', 'alt_name': 'mwm_validation_hot'},
        373: {'label': 'mwm_ob_core_boss_1.0.39', 'carton_pk': 1561, 'program': 'mwm_ob', 'version': '1.0.39', 'v1': 10.39, 'name': 'mwm_ob_core_boss', 'mapper': 'mwm', 'alt_program': 'ob', 'alt_name': 'mwm_ob_core'},
        374: {'label': 'mwm_ob_core_boss_single_1.0.39', 'carton_pk': 1562, 'program': 'mwm_ob', 'version': '1.0.39', 'v1': 10.39, 'name': 'mwm_ob_core_boss_single', 'mapper': 'mwm', 'alt_program': 'ob', 'alt_name': 'mwm_ob_core'},
        375: {'label': 'mwm_ob_cepheids_boss_1.0.39', 'carton_pk': 1565, 'program': 'mwm_ob', 'version': '1.0.39', 'v1': 10.39, 'name': 'mwm_ob_cepheids_boss', 'mapper': 'mwm', 'alt_program': 'ob', 'alt_name': 'mwm_ob_cepheids'},
        376: {'label': 'mwm_bin_rv_long_apogee_1.0.39', 'carton_pk': 1566, 'program': 'mwm_bin', 'version': '1.0.39', 'v1': 10.39, 'name': 'mwm_bin_rv_long_apogee', 'mapper': 'mwm', 'alt_program': 'bin', 'alt_name': 'mwm_bin_rv_long'},
        377: {'label': 'mwm_bin_rv_short_mdwarf_apogee_18epoch_1.0.39', 'carton_pk': 1567, 'program': 'mwm_bin', 'version': '1.0.39', 'v1': 10.39, 'name': 'mwm_bin_rv_short_mdwarf_apogee_18epoch', 'mapper': 'mwm', 'alt_program': 'bin', 'alt_name': 'mwm_bin_rv_short_mdwarf'},
        378: {'label': 'mwm_bin_rv_short_mdwarf_apogee_12epoch_1.0.39', 'carton_pk': 1568, 'program': 'mwm_bin', 'version': '1.0.39', 'v1': 10.39, 'name': 'mwm_bin_rv_short_mdwarf_apogee_12epoch', 'mapper': 'mwm', 'alt_program': 'bin', 'alt_name': 'mwm_bin_rv_short_mdwarf'},
        379: {'label': 'mwm_bin_rv_short_mdwarf_apogee_08epoch_1.0.39', 'carton_pk': 1569, 'program': 'mwm_bin', 'version': '1.0.39', 'v1': 10.39, 'name': 'mwm_bin_rv_short_mdwarf_apogee_08epoch', 'mapper': 'mwm', 'alt_program': 'bin', 'alt_name': 'mwm_bin_rv_short_mdwarf'},
        380: {'label': 'mwm_bin_rv_short_subgiant_apogee_1.0.39', 'carton_pk': 1570, 'program': 'mwm_bin', 'version': '1.0.39', 'v1': 10.39, 'name': 'mwm_bin_rv_short_subgiant_apogee', 'mapper': 'mwm', 'alt_program': 'bin', 'alt_name': 'mwm_bin_rv_short_subgiant'},
        381: {'label': 'mwm_bin_rv_short_rgb_apogee_1.0.39', 'carton_pk': 1571, 'program': 'mwm_bin', 'version': '1.0.39', 'v1': 10.39, 'name': 'mwm_bin_rv_short_rgb_apogee', 'mapper': 'mwm', 'alt_program': 'bin', 'alt_name': 'mwm_bin_rv_short_rgb'},
        382: {'label': 'mwm_halo_distant_rrl_boss_single_1.0.39', 'carton_pk': 1572, 'program': 'mwm_halo', 'version': '1.0.39', 'v1': 10.39, 'name': 'mwm_halo_distant_rrl_boss_single', 'mapper': 'mwm', 'alt_program': 'halo', 'alt_name': 'mwm_halo_distant_rrl'},
        383: {'label': 'mwm_halo_distant_rrl_boss_1.0.39', 'carton_pk': 1573, 'program': 'mwm_halo', 'version': '1.0.39', 'v1': 10.39, 'name': 'mwm_halo_distant_rrl_boss', 'mapper': 'mwm', 'alt_program': 'halo', 'alt_name': 'mwm_halo_distant_rrl'},
        384: {'label': 'mwm_halo_vmp_xp_boss_single_1.0.39', 'carton_pk': 1574, 'program': 'mwm_halo', 'version': '1.0.39', 'v1': 10.39, 'name': 'mwm_halo_vmp_xp_boss_single', 'mapper': 'mwm', 'alt_program': 'halo', 'alt_name': 'mwm_halo_mp_xp'},
        385: {'label': 'mwm_halo_nmp_xp_boss_single_1.0.39', 'carton_pk': 1576, 'program': 'mwm_halo', 'version': '1.0.39', 'v1': 10.39, 'name': 'mwm_halo_nmp_xp_boss_single', 'mapper': 'mwm', 'alt_program': 'halo', 'alt_name': 'mwm_halo_mp_xp'},
        386: {'label': 'mwm_halo_vmp_xp_apogee_single_1.0.39', 'carton_pk': 1577, 'program': 'mwm_halo', 'version': '1.0.39', 'v1': 10.39, 'name': 'mwm_halo_vmp_xp_apogee_single', 'mapper': 'mwm', 'alt_program': 'halo', 'alt_name': 'mwm_halo_mp_xp'},
        387: {'label': 'mwm_halo_mp_xp_apogee_single_1.0.39', 'carton_pk': 1578, 'program': 'mwm_halo', 'version': '1.0.39', 'v1': 10.39, 'name': 'mwm_halo_mp_xp_apogee_single', 'mapper': 'mwm', 'alt_program': 'halo', 'alt_name': 'mwm_halo_mp_xp'},
        388: {'label': 'mwm_halo_nmp_xp_apogee_single_1.0.39', 'carton_pk': 1579, 'program': 'mwm_halo', 'version': '1.0.39', 'v1': 10.39, 'name': 'mwm_halo_nmp_xp_apogee_single', 'mapper': 'mwm', 'alt_program': 'halo', 'alt_name': 'mwm_halo_mp_xp'},
        389: {'label': 'mwm_halo_vmp_xp_boss_1.0.39', 'carton_pk': 1580, 'program': 'mwm_halo', 'version': '1.0.39', 'v1': 10.39, 'name': 'mwm_halo_vmp_xp_boss', 'mapper': 'mwm', 'alt_program': 'halo', 'alt_name': 'mwm_halo_mp_xp'},
        390: {'label': 'mwm_halo_mp_xp_boss_1.0.39', 'carton_pk': 1581, 'program': 'mwm_halo', 'version': '1.0.39', 'v1': 10.39, 'name': 'mwm_halo_mp_xp_boss', 'mapper': 'mwm', 'alt_program': 'halo', 'alt_name': 'mwm_halo_mp_xp'},
        391: {'label': 'mwm_halo_nmp_xp_boss_1.0.39', 'carton_pk': 1582, 'program': 'mwm_halo', 'version': '1.0.39', 'v1': 10.39, 'name': 'mwm_halo_nmp_xp_boss', 'mapper': 'mwm', 'alt_program': 'halo', 'alt_name': 'mwm_halo_mp_xp'},
        392: {'label': 'mwm_halo_vmp_xp_apogee_1.0.39', 'carton_pk': 1583, 'program': 'mwm_halo', 'version': '1.0.39', 'v1': 10.39, 'name': 'mwm_halo_vmp_xp_apogee', 'mapper': 'mwm', 'alt_program': 'halo', 'alt_name': 'mwm_halo_mp_xp'},
        393: {'label': 'mwm_halo_mp_xp_apogee_1.0.39', 'carton_pk': 1584, 'program': 'mwm_halo', 'version': '1.0.39', 'v1': 10.39, 'name': 'mwm_halo_mp_xp_apogee', 'mapper': 'mwm', 'alt_program': 'halo', 'alt_name': 'mwm_halo_mp_xp'},
        394: {'label': 'mwm_halo_nmp_xp_apogee_1.0.39', 'carton_pk': 1585, 'program': 'mwm_halo', 'version': '1.0.39', 'v1': 10.39, 'name': 'mwm_halo_nmp_xp_apogee', 'mapper': 'mwm', 'alt_program': 'halo', 'alt_name': 'mwm_halo_mp_xp'},
        395: {'label': 'mwm_halo_local_high_apogee_single_1.0.39', 'carton_pk': 1586, 'program': 'mwm_halo', 'version': '1.0.39', 'v1': 10.39, 'name': 'mwm_halo_local_high_apogee_single', 'mapper': 'mwm', 'alt_program': 'halo', 'alt_name': 'mwm_halo_local'},
        396: {'label': 'mwm_halo_local_high_boss_single_1.0.39', 'carton_pk': 1587, 'program': 'mwm_halo', 'version': '1.0.39', 'v1': 10.39, 'name': 'mwm_halo_local_high_boss_single', 'mapper': 'mwm', 'alt_program': 'halo', 'alt_name': 'mwm_halo_local'},
        397: {'label': 'mwm_halo_local_low_apogee_single_1.0.39', 'carton_pk': 1588, 'program': 'mwm_halo', 'version': '1.0.39', 'v1': 10.39, 'name': 'mwm_halo_local_low_apogee_single', 'mapper': 'mwm', 'alt_program': 'halo', 'alt_name': 'mwm_halo_local'},
        398: {'label': 'mwm_halo_local_low_boss_single_1.0.39', 'carton_pk': 1589, 'program': 'mwm_halo', 'version': '1.0.39', 'v1': 10.39, 'name': 'mwm_halo_local_low_boss_single', 'mapper': 'mwm', 'alt_program': 'halo', 'alt_name': 'mwm_halo_local'},
        399: {'label': 'mwm_halo_local_high_apogee_1.0.39', 'carton_pk': 1590, 'program': 'mwm_halo', 'version': '1.0.39', 'v1': 10.39, 'name': 'mwm_halo_local_high_apogee', 'mapper': 'mwm', 'alt_program': 'halo', 'alt_name': 'mwm_halo_local'},
        400: {'label': 'mwm_halo_local_high_boss_1.0.39', 'carton_pk': 1591, 'program': 'mwm_halo', 'version': '1.0.39', 'v1': 10.39, 'name': 'mwm_halo_local_high_boss', 'mapper': 'mwm', 'alt_program': 'halo', 'alt_name': 'mwm_halo_local'},
        401: {'label': 'mwm_halo_local_low_apogee_1.0.39', 'carton_pk': 1592, 'program': 'mwm_halo', 'version': '1.0.39', 'v1': 10.39, 'name': 'mwm_halo_local_low_apogee', 'mapper': 'mwm', 'alt_program': 'halo', 'alt_name': 'mwm_halo_local'},
        402: {'label': 'mwm_halo_local_low_boss_1.0.39', 'carton_pk': 1593, 'program': 'mwm_halo', 'version': '1.0.39', 'v1': 10.39, 'name': 'mwm_halo_local_low_boss', 'mapper': 'mwm', 'alt_program': 'halo', 'alt_name': 'mwm_halo_local'},
        403: {'label': 'mwm_erosita_stars_boss_1.0.40', 'carton_pk': 1594, 'program': 'mwm_erosita', 'version': '1.0.40', 'v1': 10.4, 'name': 'mwm_erosita_stars_boss', 'mapper': 'mwm', 'alt_program': 'erosita', 'alt_name': 'mwm_erosita_stars'},
        404: {'label': 'mwm_erosita_compact_boss_1.0.40', 'carton_pk': 1595, 'program': 'mwm_erosita', 'version': '1.0.40', 'v1': 10.4, 'name': 'mwm_erosita_compact_boss', 'mapper': 'mwm', 'alt_program': 'erosita', 'alt_name': 'mwm_erosita_compact'},
        405: {'label': 'mwm_erosita_compact_boss_shallow_1.0.40', 'carton_pk': 1596, 'program': 'mwm_erosita', 'version': '1.0.40', 'v1': 10.4, 'name': 'mwm_erosita_compact_boss_shallow', 'mapper': 'mwm', 'alt_program': 'erosita', 'alt_name': 'mwm_erosita_compact'},
        406: {'label': 'mwm_halo_mp_xp_boss_single_1.0.41', 'carton_pk': 1597, 'program': 'mwm_halo', 'version': '1.0.41', 'v1': 10.41, 'name': 'mwm_halo_mp_xp_boss_single', 'mapper': 'mwm', 'alt_program': 'halo', 'alt_name': 'mwm_halo_mp_xp'},
        407: {'label': 'mwm_snc_ext_main_apogee_1.0.41', 'carton_pk': 1598, 'program': 'mwm_snc', 'version': '1.0.41', 'v1': 10.41, 'name': 'mwm_snc_ext_main_apogee', 'mapper': 'mwm', 'alt_program': 'snc', 'alt_name': 'mwm_snc'},
        408: {'label': 'mwm_snc_ext_filler_apogee_1.0.41', 'carton_pk': 1599, 'program': 'mwm_snc', 'version': '1.0.41', 'v1': 10.41, 'name': 'mwm_snc_ext_filler_apogee', 'mapper': 'mwm', 'alt_program': 'snc', 'alt_name': 'mwm_snc'},
        409: {'label': 'mwm_snc_ext_main_boss_1.0.41', 'carton_pk': 1600, 'program': 'mwm_snc', 'version': '1.0.41', 'v1': 10.41, 'name': 'mwm_snc_ext_main_boss', 'mapper': 'mwm', 'alt_program': 'snc', 'alt_name': 'mwm_snc'},
        410: {'label': 'mwm_snc_ext_filler_boss_1.0.41', 'carton_pk': 1601, 'program': 'mwm_snc', 'version': '1.0.41', 'v1': 10.41, 'name': 'mwm_snc_ext_filler_boss', 'mapper': 'mwm', 'alt_program': 'snc', 'alt_name': 'mwm_snc'},
        411: {'label': 'mwm_monitor_n188_apogee_long_1.0.42', 'carton_pk': 1611, 'program': 'mwm_monitor', 'version': '1.0.42', 'v1': 10.42, 'name': 'mwm_monitor_n188_apogee_long', 'mapper': 'mwm', 'alt_program': 'monitor', 'alt_name': 'mwm_monitor_apogee_n188'},
        412: {'label': 'mwm_monitor_n188_apogee_short_1.0.42', 'carton_pk': 1612, 'program': 'mwm_monitor', 'version': '1.0.42', 'v1': 10.42, 'name': 'mwm_monitor_n188_apogee_short', 'mapper': 'mwm', 'alt_program': 'monitor', 'alt_name': 'mwm_monitor_apogee_n188'},
        413: {'label': 'mwm_monitor_m67_apogee_long_1.0.42', 'carton_pk': 1613, 'program': 'mwm_monitor', 'version': '1.0.42', 'v1': 10.42, 'name': 'mwm_monitor_m67_apogee_long', 'mapper': 'mwm', 'alt_program': 'monitor', 'alt_name': 'mwm_monitor_apogee_m67'},
        414: {'label': 'mwm_monitor_m67_apogee_short_1.0.42', 'carton_pk': 1614, 'program': 'mwm_monitor', 'version': '1.0.42', 'v1': 10.42, 'name': 'mwm_monitor_m67_apogee_short', 'mapper': 'mwm', 'alt_program': 'monitor', 'alt_name': 'mwm_monitor_apogee_m67'},
        415: {'label': 'mwm_monitor_m15_apogee_long_1.0.42', 'carton_pk': 1615, 'program': 'mwm_monitor', 'version': '1.0.42', 'v1': 10.42, 'name': 'mwm_monitor_m15_apogee_long', 'mapper': 'mwm', 'alt_program': 'monitor', 'alt_name': 'mwm_monitor_apogee_m15'},
        416: {'label': 'mwm_monitor_m15_apogee_short_1.0.42', 'carton_pk': 1616, 'program': 'mwm_monitor', 'version': '1.0.42', 'v1': 10.42, 'name': 'mwm_monitor_m15_apogee_short', 'mapper': 'mwm', 'alt_program': 'monitor', 'alt_name': 'mwm_monitor_apogee_m15'},
        417: {'label': 'mwm_wd_pwd_boss_1.0.42', 'carton_pk': 1617, 'program': 'mwm_wd', 'version': '1.0.42', 'v1': 10.42, 'name': 'mwm_wd_pwd_boss', 'mapper': 'mwm', 'alt_program': 'wd', 'alt_name': 'mwm_wd'},
        418: {'label': 'mwm_wd_gaia_boss_1.0.42', 'carton_pk': 1618, 'program': 'mwm_wd', 'version': '1.0.42', 'v1': 10.42, 'name': 'mwm_wd_gaia_boss', 'mapper': 'mwm', 'alt_program': 'wd', 'alt_name': 'mwm_wd'},
        419: {'label': 'mwm_cb_galex_mag_boss_1.0.42', 'carton_pk': 1619, 'program': 'mwm_cb', 'version': '1.0.42', 'v1': 10.42, 'name': 'mwm_cb_galex_mag_boss', 'mapper': 'mwm', 'alt_program': 'cb', 'alt_name': 'mwm_cb_galex'},
        420: {'label': 'mwm_cb_galex_vol_boss_1.0.42', 'carton_pk': 1620, 'program': 'mwm_cb', 'version': '1.0.42', 'v1': 10.42, 'name': 'mwm_cb_galex_vol_boss', 'mapper': 'mwm', 'alt_program': 'cb', 'alt_name': 'mwm_cb_galex'},
        421: {'label': 'mwm_cb_xmmom_boss_1.0.42', 'carton_pk': 1621, 'program': 'mwm_cb', 'version': '1.0.42', 'v1': 10.42, 'name': 'mwm_cb_xmmom_boss', 'mapper': 'mwm', 'alt_program': 'cb', 'alt_name': 'mwm_cb_xmmom'},
        422: {'label': 'mwm_cb_swiftuvot_boss_1.0.42', 'carton_pk': 1622, 'program': 'mwm_cb', 'version': '1.0.42', 'v1': 10.42, 'name': 'mwm_cb_swiftuvot_boss', 'mapper': 'mwm', 'alt_program': 'cb', 'alt_name': 'mwm_cb_swiftuvot'},
        423: {'label': 'mwm_astar_core_boss_1.0.43', 'carton_pk': 1624, 'program': 'mwm_ob', 'version': '1.0.43', 'v1': 10.43, 'name': 'mwm_astar_core_boss', 'mapper': 'mwm', 'alt_program': 'ob', 'alt_name': 'mwm_ob_core'},
        424: {'label': 'mwm_astar_core_boss_single_1.0.43', 'carton_pk': 1625, 'program': 'mwm_ob', 'version': '1.0.43', 'v1': 10.43, 'name': 'mwm_astar_core_boss_single', 'mapper': 'mwm', 'alt_program': 'ob', 'alt_name': 'mwm_ob_core'},
        425: {'label': 'mwm_bin_vis_apogee_1.0.44', 'carton_pk': 1626, 'program': 'mwm_filler', 'version': '1.0.44', 'v1': 10.44, 'name': 'mwm_bin_vis_apogee', 'mapper': 'mwm', 'alt_program': 'bin', 'alt_name': 'mwm_bin_vis'},
        426: {'label': 'mwm_bin_vis_boss_1.0.44', 'carton_pk': 1627, 'program': 'mwm_filler', 'version': '1.0.44', 'v1': 10.44, 'name': 'mwm_bin_vis_boss', 'mapper': 'mwm', 'alt_program': 'bin', 'alt_name': 'mwm_bin_vis'},
        427: {'label': 'mwm_galactic_core_dist_apogee_1.0.44', 'carton_pk': 1628, 'program': 'mwm_galactic', 'version': '1.0.44', 'v1': 10.44, 'name': 'mwm_galactic_core_dist_apogee', 'mapper': 'mwm', 'alt_program': 'galactic', 'alt_name': 'mwm_galactic_core'},
        428: {'label': 'mwm_dust_core_dist_apogee_1.0.45', 'carton_pk': 1631, 'program': 'mwm_dust', 'version': '1.0.45', 'v1': 10.45, 'name': 'mwm_dust_core_dist_apogee', 'mapper': 'mwm', 'alt_program': 'dust', 'alt_name': 'mwm_dust_core'},
        429: {'label': 'manual_mwm_nsbh_apogee_1.0.46', 'carton_pk': 1632, 'program': 'mwm_cb', 'version': '1.0.46', 'v1': 10.46, 'name': 'manual_mwm_nsbh_apogee', 'mapper': 'mwm', 'alt_program': 'nsbh', 'alt_name': 'manual_mwm_nsbh'},
        430: {'label': 'manual_mwm_nsbh_boss_1.0.46', 'carton_pk': 1633, 'program': 'mwm_cb', 'version': '1.0.46', 'v1': 10.46, 'name': 'manual_mwm_nsbh_boss', 'mapper': 'mwm', 'alt_program': 'nsbh', 'alt_name': 'manual_mwm_nsbh'},
        431: {'label': 'manual_mwm_validation_rv_apogee_1.0.46', 'carton_pk': 1634, 'program': 'mwm_validation', 'version': '1.0.46', 'v1': 10.46, 'name': 'manual_mwm_validation_rv_apogee', 'mapper': 'mwm', 'alt_program': 'validation', 'alt_name': 'mwm_validation_rv'},
        432: {'label': 'mwm_cb_cvcandidates_apogee_1.0.47', 'carton_pk': 1636, 'program': 'mwm_cb', 'version': '1.0.47', 'v1': 10.47, 'name': 'mwm_cb_cvcandidates_apogee', 'mapper': 'mwm', 'alt_program': 'cb', 'alt_name': 'mwm_cb_cvcandidates'},
        433: {'label': 'mwm_cb_cvcandidates_boss_1.0.47', 'carton_pk': 1637, 'program': 'mwm_cb', 'version': '1.0.47', 'v1': 10.47, 'name': 'mwm_cb_cvcandidates_boss', 'mapper': 'mwm', 'alt_program': 'cb', 'alt_name': 'mwm_cb_cvcandidates'},
        434: {'label': 'mwm_legacy_ir2opt_boss_1.0.47', 'carton_pk': 1638, 'program': 'mwm_legacy', 'version': '1.0.47', 'v1': 10.47, 'name': 'mwm_legacy_ir2opt_boss', 'mapper': 'mwm', 'alt_program': 'legacy', 'alt_name': 'mwm_legacy_ir2opt'},
        435: {'label': 'bhm_rm_core_1.0.48', 'carton_pk': 1639, 'program': 'bhm_rm', 'version': '1.0.48', 'v1': 10.48, 'name': 'bhm_rm_core', 'mapper': 'bhm', 'alt_program': 'rm', 'alt_name': 'bhm_rm'},
        436: {'label': 'bhm_rm_known_spec_1.0.48', 'carton_pk': 1640, 'program': 'bhm_rm', 'version': '1.0.48', 'v1': 10.48, 'name': 'bhm_rm_known_spec', 'mapper': 'bhm', 'alt_program': 'rm', 'alt_name': 'bhm_rm'},
        437: {'label': 'bhm_rm_var_1.0.48', 'carton_pk': 1641, 'program': 'bhm_rm', 'version': '1.0.48', 'v1': 10.48, 'name': 'bhm_rm_var', 'mapper': 'bhm', 'alt_program': 'rm', 'alt_name': 'bhm_rm'},
        438: {'label': 'bhm_rm_ancillary_1.0.48', 'carton_pk': 1642, 'program': 'bhm_rm', 'version': '1.0.48', 'v1': 10.48, 'name': 'bhm_rm_ancillary', 'mapper': 'bhm', 'alt_program': 'rm', 'alt_name': 'bhm_rm'},
        439: {'label': 'mwm_tess_2min_apogee_1.0.49', 'carton_pk': 1644, 'program': 'mwm_planet', 'version': '1.0.49', 'v1': 10.49, 'name': 'mwm_tess_2min_apogee', 'mapper': 'mwm', 'alt_program': 'planet', 'alt_name': 'mwm_tess_2min'},
        440: {'label': 'mwm_tess_rgb_apogee_1.0.49', 'carton_pk': 1645, 'program': 'mwm_tessrgb', 'version': '1.0.49', 'v1': 10.49, 'name': 'mwm_tess_rgb_apogee', 'mapper': 'mwm', 'alt_program': 'tessrgb', 'alt_name': 'mwm_tess_rgb'},
        441: {'label': 'manual_mwm_planet_gaia_astrometry_apogee_1.0.46', 'carton_pk': 1647, 'program': 'mwm_planet', 'version': '1.0.46', 'v1': 10.46, 'name': 'manual_mwm_planet_gaia_astrometry_apogee', 'mapper': 'mwm', 'alt_program': 'planet', 'alt_name': 'manual_mwm_planet_gaia_astrometry'},
        442: {'label': 'manual_mwm_planet_gpi_apogee_1.0.46', 'carton_pk': 1648, 'program': 'mwm_planet', 'version': '1.0.46', 'v1': 10.46, 'name': 'manual_mwm_planet_gpi_apogee', 'mapper': 'mwm', 'alt_program': 'planet', 'alt_name': 'manual_mwm_planet_gpi'},
        443: {'label': 'manual_mwm_planet_harps_apogee_1.0.46', 'carton_pk': 1649, 'program': 'mwm_planet', 'version': '1.0.46', 'v1': 10.46, 'name': 'manual_mwm_planet_harps_apogee', 'mapper': 'mwm', 'alt_program': 'planet', 'alt_name': 'manual_mwm_planet_harps'},
        444: {'label': 'manual_mwm_planet_known_apogee_1.0.46', 'carton_pk': 1650, 'program': 'mwm_planet', 'version': '1.0.46', 'v1': 10.46, 'name': 'manual_mwm_planet_known_apogee', 'mapper': 'mwm', 'alt_program': 'planet', 'alt_name': 'manual_mwm_planet_known'},
        445: {'label': 'manual_mwm_planet_sophie_apogee_1.0.46', 'carton_pk': 1651, 'program': 'mwm_planet', 'version': '1.0.46', 'v1': 10.46, 'name': 'manual_mwm_planet_sophie_apogee', 'mapper': 'mwm', 'alt_program': 'planet', 'alt_name': 'manual_mwm_planet_sophie'},
        446: {'label': 'manual_mwm_planet_sphere_apogee_1.0.46', 'carton_pk': 1652, 'program': 'mwm_planet', 'version': '1.0.46', 'v1': 10.46, 'name': 'manual_mwm_planet_sphere_apogee', 'mapper': 'mwm', 'alt_program': 'planet', 'alt_name': 'manual_mwm_planet_sphere'},
        447: {'label': 'manual_mwm_planet_tess_eb_apogee_1.0.46', 'carton_pk': 1653, 'program': 'mwm_planet', 'version': '1.0.46', 'v1': 10.46, 'name': 'manual_mwm_planet_tess_eb_apogee', 'mapper': 'mwm', 'alt_program': 'planet', 'alt_name': 'manual_mwm_planet_tess_eb'},
        448: {'label': 'manual_mwm_planet_tess_pc_apogee_1.0.46', 'carton_pk': 1654, 'program': 'mwm_planet', 'version': '1.0.46', 'v1': 10.46, 'name': 'manual_mwm_planet_tess_pc_apogee', 'mapper': 'mwm', 'alt_program': 'planet', 'alt_name': 'manual_mwm_planet_tess_pc'},
        449: {'label': 'mwm_magcloud_agb_apogee_1.0.50', 'carton_pk': 1657, 'program': 'mwm_magcloud', 'version': '1.0.50', 'v1': 10.5, 'name': 'mwm_magcloud_agb_apogee', 'mapper': 'mwm', 'alt_program': 'magcloud', 'alt_name': 'mwm_magcloud_agb'},
        450: {'label': 'mwm_magcloud_rgb_boss_1.0.50', 'carton_pk': 1658, 'program': 'mwm_magcloud', 'version': '1.0.50', 'v1': 10.5, 'name': 'mwm_magcloud_rgb_boss', 'mapper': 'mwm', 'alt_program': 'magcloud', 'alt_name': 'mwm_magcloud_rgb'},
        451: {'label': 'manual_mwm_planet_ca_legacy_apogee_1.0.46', 'carton_pk': 1659, 'program': 'mwm_planet', 'version': '1.0.46', 'v1': 10.46, 'name': 'manual_mwm_planet_ca_legacy_apogee', 'mapper': 'mwm', 'alt_program': 'planet', 'alt_name': 'manual_mwm_planet_ca_legacy'},
        452: {'label': 'manual_mwm_planet_transiting_bd_apogee_1.0.46', 'carton_pk': 1660, 'program': 'mwm_planet', 'version': '1.0.46', 'v1': 10.46, 'name': 'manual_mwm_planet_transiting_bd_apogee', 'mapper': 'mwm', 'alt_program': 'planet', 'alt_name': 'manual_mwm_planet_transiting_bd'},        
    }


