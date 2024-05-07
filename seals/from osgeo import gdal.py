from osgeo import gdal 

# REPROJ SEALS
input_raster = "/Users/prayashpathak/Files/seals/projects/test_standard/intermediate/stitched_lulc_simplified_scenarios/lulc_esa_seals7_luh2-message_2017.tiff" 
output_raster="/Users/prayashpathak/Files/seals/projects/test_standard/output/lulc_esa_seals7_luh2-message_2017_rep.tif" 
gdal.Warp(output_raster, input_raster, dstSRS='ESRI:54030')