Motivation
----------

SDSS has a long history of using flags to indicate the quality of data.
These flags have usually been stored as 64-bit integers.
When more than 64 flag definitions have been needed, multiple flag columns have been used.
For example, `APOGEE_TARGET1` and `APOGEE_TARGET2` are two 64-bit flag columns used by APOGEE to indicate targeting information.
In APOGEE-2, another three columns were added: `APOGEE2_TARGET1`, `APOGEE2_TARGET2`, and `APOGEE2_TARGET3`.

This is manageable if there are only a few columns, but becomes unweildly when there are many.
If the targeting information in SDSS-V were stored in this way, it would require dozens of flag columns.
To check whether a flag is set, you'd need to know which column to look up for that flag, and the bit position for that flag.

The `semaphore` package provides a way to store flags in a single column. 
The underlying flags are still stored as integers in a 2D array, but this package provides a way to create, store, and query an unlimited number of flags in a single column.


Installation
------------
The current version is |semaphore_version|. You can install the package by doing

.. code-block:: console

  $ pip install sdss-semaphore


Notebooks
---------

- `Using targeting flags <https://github.com/sdss/semaphore/blob/main/notebooks/20231011_sdss5_targeting.ipynb>`_
- `Creating targeting flags for users <https://github.com/sdss/semaphore/blob/main/notebooks/20231011_sdss5_targeting_creation.ipynb>`_


Reference
---------

.. toctree::
   :maxdepth: 1

   api


Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
