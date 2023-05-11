
if dpkg -l $conda; then
    conda install -c conda-forge astromatic-source-extractor
    conda install -c conda-forge astromatic-psfex
    conda install -c conda-forge astromatic-swarp
    echo 'done'
else
    echo 'install anaconda first!!'
fi