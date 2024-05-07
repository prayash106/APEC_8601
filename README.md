## APEC_8601
## Final Project
In this project, you will pick a country. You may want to pick a relatively small country to speed up computation time, but that’s up to you.  
### Component 1: 

a)	Use SEALS to generate LULC maps for your country for 2030, 2035 and 2040. Do this for at least two different SSPs. 

Country of choice: Taiwan (ISO code: TWN) - choose a small country to make analysis faster.

SSPs choice: The SSPs are framework that are used to develop new socio-economic scenarios to be used in global climate change studies. Basically, there are five different SSPs (1-5) which narrate different socio-economic challenges to mitigation and adoption. For further reading, please refer [Popp et al. (2016)](https://www.sciencedirect.com/science/article/pii/S0959378016303399).
For this analysis, I have choosen SSP1 and SSP5 -  where SSP1 describes a future pathway with comparatively low challenges for adaptation and mitigation but SSP5, on the other hand, represents high challenges to mitigation combined with low challenges to adaptation. Basically, under SPP1 we will be seeing strong regulation to avaoid environmental tradeoffs and in case of SSP5 we will see medium regulations. 

Steps to make these changes on the pre-installed earth economy devstack workspace (to learn more about these workspace visit [Justin Polasky lab](https://johnsonpolaskylab.umn.edu)) or [earth_economy_devstack](https://github.com/jandrewjohnson?tab=repositories).
- Navigate to scenario_definations.csv files and change the respective labels based on your choice of country and SSP. AOI was chnaged to "TWN". Years was changed to 2030/35/40. Coarse projections input for respective SSP/RCP definations were downloaded from "Land Use Harmonization data" and defined in correct path.
  
b)	Plot these maps using QGIS or whatever plotting method you like.  

After running the test_standard.py python file with the changes made above, the respective LULC maps can be viewed in the visualization folder under seals of your workspace. 

My output are depicted below starting from the baseline (BAU) scenarion then under the different SSP scenarios for each year.

![lulc_esa_seals7_luh2-message_2017](https://github.com/prayash106/APEC_8601/assets/145133689/9005b66e-9383-44f3-8e79-53fca5f1ae4b)

![lulc_esa_seals7_ssp1_rcp26_luh2-message_bau_2030](https://github.com/prayash106/APEC_8601/assets/145133689/bf8f3048-f074-4514-b9a3-eaa41f3d8366)

![lulc_esa_seals7_ssp1_rcp26_luh2-message_bau_2035](https://github.com/prayash106/APEC_8601/assets/145133689/e39d62ef-1150-40c8-a161-2fc917a2857f)

![lulc_esa_seals7_ssp1_rcp26_luh2-message_bau_2040](https://github.com/prayash106/APEC_8601/assets/145133689/16f9567f-2c2a-4a9b-9e64-06879ea3371f)

![lulc_esa_seals7_ssp5_rcp85_luh2-message_bau_2030](https://github.com/prayash106/APEC_8601/assets/145133689/f4a0a080-ef18-4d37-8ea0-745d44a09bc0)

![lulc_esa_seals7_ssp5_rcp85_luh2-message_bau_2035](https://github.com/prayash106/APEC_8601/assets/145133689/bc375d38-2463-4a87-91bb-2818ad1d67fc)

![lulc_esa_seals7_ssp5_rcp85_luh2-message_bau_2040](https://github.com/prayash106/APEC_8601/assets/145133689/0cbcb614-60c3-4407-b7e0-af00c0192fe5)

c.)	Add a new “policy” layer that prevents/encourages certain types of land-use change in certain areas. For instance, you could modify the calibration parameters file to decrease the likelihood that agricultural expansion happens on steep slopes.

This step is also fairly simple as all it involves is redefining the scenarios just like we did above. In this case, we navigate to defualt inputs under seals of our base data. There we alter the policy we like by changing the inputs in the defualt_global_coefficients_csv. In this example, I try a new policy in Taiwan where we do not allow changes in cropland. These can be done by chnaging the calibration parameters to 0.

The LULC ouput that we get from this are depicted below - just like above starting from BAU model to different SSP scenarions for all years:

![lulc_esa_seals7_luh2-message_2017](https://github.com/prayash106/APEC_8601/assets/145133689/7c473c8e-5039-4623-b2d9-8e86a9b04fe2)

![lulc_esa_seals7_ssp1_rcp26_luh2-message_bau_2030](https://github.com/prayash106/APEC_8601/assets/145133689/4183270e-d200-42ae-a939-f51af5e717c4)

![lulc_esa_seals7_ssp1_rcp26_luh2-message_bau_2035](https://github.com/prayash106/APEC_8601/assets/145133689/d46626f7-5764-48d5-a7f8-9814f2cbb5c9)

![lulc_esa_seals7_ssp1_rcp26_luh2-message_bau_2040](https://github.com/prayash106/APEC_8601/assets/145133689/21a23447-fb66-4425-9f06-6dfe17c89fb7)

![lulc_esa_seals7_ssp5_rcp85_luh2-message_bau_2030](https://github.com/prayash106/APEC_8601/assets/145133689/c085a815-8da3-4972-bf06-64b7a303c480)

![lulc_esa_seals7_ssp5_rcp85_luh2-message_bau_2035](https://github.com/prayash106/APEC_8601/assets/145133689/9a463076-0602-484a-83dc-7b4def1b7504)

![lulc_esa_seals7_ssp5_rcp85_luh2-message_bau_2040](https://github.com/prayash106/APEC_8601/assets/145133689/0014a27d-9c56-4292-aa81-d6463b2045c3)

d)	Write a narrative description of how the different scenarios differ in terms of what classes expand/contract and where.

### Component 2: 

a)	Use the maps you generated to assess run ecosystem service assessments for each scenario. Specifically, run:

a.	Carbon Storage

Run the "Carbon Storage and Sequestration" InVest model. Detailed information about the inputs and outputs can be found in the [user guide](http://releases.naturalcapitalproject.org/invest-userguide/latest/en/carbonstorage.html).

The inputs used to run the model are:
- LULC maps - which we have derived above from SEALS.
- Carbon pools - which can be generated for choosen country.

The ouputs that we get are (for each LULC):
- Total carbon storage: Rasters showing the amount of carbon stored in each pixel
- Carbon stored above: Raster of aboveground carbon values.
- Carbon stored below: Raster of belowground carbon values.
- Carbon in soil: Raster of soil carbon values.
- Carbon dead : Raster of dead carbon values

The outputs from my run have been attached below for each year and SSPs. 
[Carbon storage outputs.pdf](https://github.com/prayash106/APEC_8601/files/15227545/Carbon.storage.outputs.pdf)

b.	Pollination

Run the "Crop Pollination" Invest model. Detailed information about the inputs and outputs can be found in the [user guide](http://releases.naturalcapitalproject.org/invest-userguide/latest/en/croppollination.html).

The inputs used to run this model are:
- LULC maps - which we have derived above from SEALS.
- Biophysical table
- Guild table

The ouputs generated from this model are:
- Pollinator abundance for each species and season (Apis/Bombus for Spring/Summer)
- Pollinator supply for each season (Spring/Summer)
- Total pollinator abundance for each season (Spring/Summer)
  
The outputs from my run have been attached below for each year and SSPs. 
[Pollination outputs.pdf](https://github.com/prayash106/APEC_8601/files/15227690/Pollination.outputs.pdf)

c. Water purification/ Nutrient Delivery ratio

Run the "Nutrient Delivery ratio" Invest model. Detailed information about the inputs and outputs can be found in the [user guide](http://releases.naturalcapitalproject.org/invest-userguide/latest/ndr.html).

The inputs used to run this model are:
- Digital elevation model - which I extracted from [ASTER](https://asterweb.jpl.nasa.gov/gdem.asp).
- LULC maps - which we have derived above from SEALS.
- Nutrient Runoff proxy - where we can use annual precipitaion data.
- Watersheds - extract watershed map for youe respective area of interest.
- Biophysical table

A thing to note here is ti be careful for aligning each of these inputs in same projection. In my case, I re-projected each of them into World_Robinson before feeding them to InVest.

The ouputs generated from this model are:
 - watershed_results_ndr - vector containing aggregrated nutrient model results per wateshed
 - p_surface_export
 - n_surface_export
 - n_subsurface_export
 - n_total_export

The outputs from my run have been attached below for each year and SSPs. The attached file contains only watershed_results_ndr but othe results can be provided if needed.
[Water purification:NDR.pdf](https://github.com/prayash106/APEC_8601/files/15240361/Water.purification.NDR.pdf)

d. Water Yield

Run the "Annual Water Yield" Invest model. Detailed information about the inputs and outputs can be found in the [user guide] (http://releases.naturalcapitalproject.org/invest-userguide/latest/reservoirhydropowerproduction.html). 

The inputs used to run this model are:
- Precipitation - use the same annual precipitation file from NDR.
- Evapotranspiration
- Root restricting layer depth
- Plant Available Water content
- LULC
- Biophysical table
- Watersheds

e. Sediment retention

Run the "Sediment Delivery Ratio" Invest model. Detailed information about the inputs and outputs can be found in the [user guide] (http://releases.naturalcapitalproject.org/invest-userguide/latest/en/sdr.html).

The inputs used to run this model are:
- Digital elevation model
- LULC
- Biophysical table
- Watersheds
- Erosivity
- Soil erodibility


c)	Write a narrative description of how the different scenarios differ in terms of which ecosystem services see localized increases/decreases.


d)	Write a 1 paragraph executive summary on your results from the perspective of what a policy maker interested in “green economic development” should know about their country’s ecosystem services.

### Component 3:
a.)	Post and organize all of the code you have worked on this semester in a single repository. Make a readme.md (which is the default files that Github renders when you visit the repository) that highlights/summarizes/organizes what you’ve done. You’ll probably want to highlight the policy summary that you did above, but also include the other code you’ve developed.

b.)	Either make the repository public (recommended to start building your portfolio for later job searching success) or invite me to it. Submit the link to your repo on Canvas.














