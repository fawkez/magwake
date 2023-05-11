# Decamagwake

Decamagwake is a Python library that provides PSF photometry on DECAM data using the sextractor and psfex packages. This library is published on PyPI, and it can be installed using pip:

```
pip install decamagwake
```

## Installation Requirements

Before installing Decamagwake, you need to have the following packages installed on your system:

- astropy
- numpy
- pandas
- sextractor
- psfex

## Usage

The following example shows how to use Decamagwake to perform PSF photometry on a DECAM data set:

```
from decam_lib import decam_processing

# Set up output and data directories
output_dir = 'tests/data_test/workdir'
data_dir = 'tests/data_test'

# Create Decam_pipeline object
pipeline_test = decam_processing.Decam_pipeline(output_dir=output_dir, data_dir=data_dir, config_dir='tests/config')

# Perform PSF photometry
pipeline_test.photometry()

# Make final catalogs
pipeline_test.join_final_catalogs2()

# Delete temporary files
pipeline_test.delete_temp()
```

## License

This library is released under the MIT license. See LICENSE for more information.

## Contributing

Contributions to this library are welcome. Please see CONTRIBUTING.md for more information.

## Contact

If you have any questions or comments about this library, please contact us at decamagwake@gmail.com



