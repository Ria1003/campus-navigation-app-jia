#!/Users/daviddoyle/workspace/github.com/DavidDoyle20/campus-navigation-app/myenv/bin/python3.12

import sys

from osgeo.gdal import deprecation_warn

# import osgeo_utils.gdalcompare as a convenience to use as a script
from osgeo_utils.gdalcompare import *  # noqa
from osgeo_utils.gdalcompare import main

deprecation_warn("gdalcompare")
sys.exit(main(sys.argv))
