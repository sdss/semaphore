Motivation
----------

SDSS has a long history of using flags to indicate the quality of data.
These flags have usually been stored as 64-bit integers.
When more than 64 flag definitions have been needed, multiple flag columns have been used.
For example, `APOGEE_TARGET1` and `APOGEE_TARGET2` are two 64-bit flag columns used by APOGEE to indicate targeting information.

This is manageable if there are only a few columns, but becomes unweildly when there are many.
If the targeting information in SDSS-V were stored in this way, it would require dozens of flag columns.
To check whether a flag is set, you'd need to know which column to look up for that flag, and the bit position for that flag.

The `semaphore` package provides a way to store flags in a single column. 
The underlying flags are still stored as integers in a 2D array, but this package provides a way to create, store, and query an unlimited number of flags in a single column.


Installation
------------
The current version is |semaphore_version|. You can install the package by doing

.. code-block:: console

  $ git clone git@github.com:sdss/semaphore.git
  $ cd semaphore
  $ python setup.py install 


Interpreting flags
------------------

If you've downloaded a SDSS data product that uses `semaphore` flags, you can use the `semaphore` package to interpret the flags.
The only thing you'll need is the 'flag reference': a set of flag definitions that map the bit location of a flag to its name, description, and potentially any other attributes.
The flag reference can be stored as a table (e.g., a CSV file), and the location of the flag reference should be stored in the comments where the original flags are stored.

Let's run through an example:

.. code-block:: python

  from astropy.io import fits
  import semaphore

  # Load the flag reference
  reference = semaphore.FlagReference.from_csv("target_flags_ipl3.csv")

  # Load a SDSS data product that uses semaphore flags
  all_star = fits.open("allStar-ipl3.fits")[1].data

  # The targeting flags are stored in the 'TARGETING' column
  target_flags = semaphore.FlagsArray(all_star["TARGETING"], reference=reference)

  # Query the flags.
  # This will give us a boolean mask indicating whether a source is in `mwm_gg_core` (True) or not (False)
  in_gg_core = target_flags.is_flag_set("mwm_gg_core")

  # We can also query multiple flags at once
  in_gg_or_wd = target_flags.are_any_flags_set("mwm_gg_core", "mwm_wd_core")

  # Or require both (NO sources should exist here, if we have done our targeting correctly...)
  in_gg_and_wd = target_flags.are_all_flags_set("mwm_gg_core", "mwm_wd_core")



Creating flags
--------------

If you are creating a SDSS data product that uses `semaphore` flags, you'll first need to create a flag reference.
It's recommended to use a flag reference that does not have any gaps in the bit locations, as this makes storing the flags more compact.

Here's an example where we will create a flag reference for a set of cartons from the SDSS targeting database. 

.. code-block:: python

  from astropy.io import fits
  from astropy.table import Table
  from tqdm import tqdm
  from sdssdb.peewee.sdss5db.targetdb import database, Target, Carton, CartonToTarget
  from semaphore import Flags, FlagsArray, FlagsReference 

  database.set_profile("operations")

  q = Carton.select().dicts()
  definitions = Table(rows=list(q))
  definitions.write("target_flags_ipl3.csv", overwrite=True)

  # Create a reference from the carton definitions, using `carton` name as the "unique" flag name.
  # If you wanted a different flag name, you could create a new column in your table and use that.
  reference = FlagsReference.from_table(definitions, flag_name_key="carton")


Now let's query the database for a million target assignments and store their flags.

Since we are querying a million "target assignments" (and not a million targets), we may not know how many targets we will get back.
So here we will create a `Flags` object for each source (unique by catalog identifier) and merge them together into a `FlagsArray` before storing them.

.. code-block:: python


  # We will only store 1 million assignments for this example.
  limit = 1_000_000 

  q = (
      Target
      .select(
          Target.catalogid,
          Carton.carton # This will be the flag name to set
      )
      .join(CartonToTarget)
      .join(Carton)
      .limit(limit)
      .tuples()
      .iterator()
  )

  assignments = {}
  for catalogid, flag in tqdm(q):
      assignments.setdefault(catalogid, Flags(reference=reference))
      assignments[catalogid].set_flags(flag)

  # Now we have a dictionary of Flags objects, we can merge them into a FlagsArray.
  catalog_identifiers = list(assignments.keys())

  flags_array = FlagsArray(catalog_identifiers.values())
  
  table = fits.BinTableHDU.from_columns(
    [
      fits.Column(name="CATALOGID", array=catalog_identifiers),
      flags_array.to_fits_column(name="TARGETING")
    ]
  )
  
  hdu_list = fits.HDUList([
    fits.PrimaryHDU(),
    table
  ])
  hdu_list.writeto("allStar-ipl3.fits")

Now you can distribute the targeting.fits file with your data product, and users can use the `semaphore` package to interpret the flags.
Just make sure users know where to find the flag reference file. In the example above we should really either store the flag references
in another HDU in the same FITS file, or store the location of the flag reference in the comments of the FITS file.


Reference
---------

.. toctree::
   :maxdepth: 1

   api


Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
