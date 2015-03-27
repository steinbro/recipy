import sys
from PatchImporter import PatchImporter
from PatchSimple import PatchSimple
import wrapt

from log import *
from utils import *

class PatchPandas(PatchSimple):
    modulename = 'pandas'
    input_functions = ['read_csv', 'read_table', 'read_excel', 'read_hdf', 'read_pickle', 'read_stata']
    output_functions = ['DataFrame.to_csv']

    input_wrapper = create_wrapper(log_input, 0, 'pandas')
    output_wrapper = create_wrapper(log_output, 0, 'pandas')

class PatchMPL(PatchSimple):
    modulename = 'matplotlib.pyplot'

    input_functions = []
    output_functions = ['savefig']

    input_wrapper = create_wrapper(log_input, 0, 'matplotlib')
    output_wrapper = create_wrapper(log_output, 0, 'matplotlib')

class PatchNumpy(PatchSimple):
    modulename = 'numpy'

    input_functions = ['genfromtxt', 'loadtxt', 'load', 'fromfile']
    output_functions = ['save', 'savez', 'savez_compressed', 'savetxt']

    input_wrapper = create_wrapper(log_input, 0, 'numpy')
    output_wrapper = create_wrapper(log_output, 0, 'numpy')

class PatchGDAL(PatchSimple):
    modulename = 'gdal'

    input_functions = ['Open']
    output_functions = ['Driver.Create', 'Driver.CreateCopy']

    input_wrapper = create_wrapper(log_input, 0, 'gdal')
    output_wrapper = create_wrapper(log_output, 0, 'gdal')

sys.meta_path = [PatchPandas(), PatchMPL(), PatchNumpy(), PatchGDAL()]