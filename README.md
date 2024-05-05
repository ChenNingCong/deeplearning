Here is a simple (flat-layout) template for deep learning code development. It should be sufficient for oridinary usage. 

# Basic
Simply git clone the repository and edit the code in the repository (under deeplearning). You may want to use a different name for the repository then just change `deeplearning` to your preferred name.

# Build package and deploy
1. If you wish to publish the package:
```
python3 -m build
```
See https://packaging.python.org/en/latest/tutorials/packaging-projects/ for more information. You need to at least change the name of the package. If you use flat layout, then you should pay attention to the `tool.setuptools.packages.find`.

Then follow the upload documentation to upload the package.

2. If you don't want to publish your package (because you need a pypi account), but you want to install the package and use it globally. Then you can simply `pip install git+<your github repo link> --force-reinstall --upgrade` (we force reinstall the package so that we can receive updates in the master branch immediately). You can also git clone the package and do a `pip install -e .`.

# Run test
`python -m unittest test/test1.py`
See https://docs.python.org/3/library/unittest.html for more information.

# Run script
You need to set up the PYTHONPATH. Or maybe write a launcher script by yourself.