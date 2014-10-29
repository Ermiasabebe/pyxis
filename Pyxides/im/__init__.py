from Pyxis.ModSupport import *
register_pyxis_module('im')


#class set():
# def __init__(self):
    # external tools  
define('IMAGER','lwimager','Imager to user. Default is lwimager.')
define('LWIMAGER_PATH','lwimager','path to lwimager binary. Default is to look in the system PATH.')
define('WSCLEAN_PATH_Template','wsclean','Path to WSCLEAN')
define('MORESANE_PATH_Template','moresane','Path to PyMORSANE')

# default clean algorithm
define("CLEAN_ALGORITHM","clark","CLEAN algorithm (clark, hogbom, csclean, etc.)")
# Default imaging colun
define('COLUMN','CORRECTED_DATA','default column to image')

# filenames for images
define("BASENAME_IMAGE_Template","${OUTFILE}${-<IMAGER}","default base name for all image filenames below")
define("DIRTY_IMAGE_Template", "${BASENAME_IMAGE}.dirty.fits","output filename for dirty image")
define("PSF_IMAGE_Template", "${BASENAME_IMAGE}.psf.fits","output filename for psf image")
define("RESTORED_IMAGE_Template", "${BASENAME_IMAGE}.restored.fits","output filename for restored image")
define("RESIDUAL_IMAGE_Template", "${BASENAME_IMAGE}.residual.fits","output filename for deconvolution residuals")
define("MODEL_IMAGE_Template", "${BASENAME_IMAGE}.model.fits","output filename for deconvolution model")
define("FULLREST_IMAGE_Template", "${BASENAME_IMAGE}.fullrest.fits","output filename for LSM-restored image")
define("MASK_IMAGE_Template", "${BASENAME_IMAGE}.mask.fits","output filename for CLEAN mask")

# How to channelize the output image. 0 for average all, 1 to include all, 2 to average with a step of 2, etc.
# None means defer to 'imager' module options
define("IMAGE_CHANNELIZE",0,"image channels selection: 0 for all, 1 for per-channel cube")
# passed to tigger-restore when restoring models into images. Use e.g. "-b 45" for a 45" restoring beam.
define("RESTORING_OPTIONS","","extra options to tigger-restore for LSM-restoring")

# Standard imaging options
#ifrs = ""
#npix = 1024
#cellsize = "2arcsec"
#mode = "channel"
#stokes = "IQUV"
#weight = "briggs"
#robust = 0
#niter = 1000
#gain = .1
#threshold = 0
#wprojplanes = 0
#cachesize = 4096
#fixed = 0
## rescale images by factor
#flux_rescale=1
## use velocity rather than frequency
#velocity = False 
#no_weight_fov = False


import wsclean
import lwimager
import moresane
