source virtual-env/bin/activate
cd school
python -m unittest tests.test_read_models tests.test_write_models \
    tests.test_timing
deactivate
