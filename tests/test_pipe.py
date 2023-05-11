from decam_lib import decam_processing


print('Import Works')

output_dir = 'tests/data_test/workdir'
data_dir = 'tests/data_test'

pipeline_test = decam_processing.Decam_pipeline(output_dir=output_dir, data_dir=data_dir, config_dir='tests/config')

# Perform PSF photometry
pipeline_test.photometry()

# Make final catalogs
pipeline_test.join_final_catalogs2()

# Delete temporary files
pipeline_test.delete_temp()