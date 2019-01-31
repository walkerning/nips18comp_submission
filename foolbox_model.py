from __future__ import print_function
import os
import glob
from fmodel import create_fmodel

here = os.path.dirname(os.path.abspath(__file__))

def unzip_model(name):
    dire = os.path.join(here, "test_models", name)
    if not os.path.isdir(dire):
        import zipfile
        print("Unzip model {} to {}".format(name, dire))
        try:
            zipf = zipfile.ZipFile(dire+".zip", "r")
        except Exception as e:
            print("ERROR while unzipping model! Please make sure git-lfs is installed!")
            raise
        zipf.extractall(os.path.join(here, "test_models"))
        zipf.close()

def create():
    for fname in glob.glob(os.path.join(here, "test_models/*.zip")):
        unzip_model(os.path.basename(fname).rsplit(".", 1)[0])
    fmodel = create_fmodel()
    return fmodel
