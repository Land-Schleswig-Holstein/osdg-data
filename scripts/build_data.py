from sdg.open_sdg import open_sdg_build

open_sdg_build(config='config_data.yml')

 """Stops the numpy error showing up"""
import warnings
warnings.filterwarnings("ignore", message="numpy.dtype size changed")
warnings.filterwarnings("ignore", message="numpy.ufunc size changed") 
