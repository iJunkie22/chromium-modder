__author__ = 'ethan'
import os
from . import lookup

def load_chrome_folder(par_directory):

    chrome_d = os.path.join(par_directory, 'chrome')
    assert os.path.isdir(chrome_d)
    for id_str, ext_str, vcp_str in lookup.read_table():
        real_cpath = lookup.to_non_chrome_path(vcp_str)
        full_rcp = os.path.join(par_directory, real_cpath)
        if os.path.isfile(full_rcp):
            print "Injecting", os.path.basename(full_rcp), "as", id_str + "." + ext_str
            #TODO: write code to do stuff

