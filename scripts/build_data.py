from sdg.open_sdg import open_sdg_build

open_sdg_build(config='config_data.yml')

import warnings
warnings.filterwarnings("ignore", message="numpy.dtype size changed")
warnings.filterwarnings("ignore", message="numpy.ufunc size changed") 
