
.. _api:

API
===

.. _api-main:

Targeting Flags
---------------

The `TargetingFlags` class is relevant to SDSS carton-to-bit version 1 (`SDSSC2BV`).

.. autoclass:: sdss_semaphore.targeting.TargetingFlags
   :members:
   :inherited-members:
   :exclude-members: mapping, dtype
   :show-inheritance:

Base Targeting Flags
--------------------

The `BaseTargetingFlags` class provides utilities for targeting flags which do not depend on a specific version of the SDSS carton-to-bit mapping.

.. autoclass:: sdss_semaphore.targeting.BaseTargetingFlags
   :members:
   :inherited-members:
   :show-inheritance:


Base Flags
----------

The `BaseFlags` class provides functionality for any kind of flagging system, irrespective of the bit-attribute mapping.

.. autoclass:: sdss_semaphore.BaseFlags
   :members:
   :show-inheritance: 

