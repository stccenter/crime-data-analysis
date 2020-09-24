<!--
 * @Author: your name
 * @Date: 2020-09-23 17:36:34
 * @LastEditTime: 2020-09-24 17:22:24
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: \github_test\crime_readme.md
-->
# Crime Data Analysis

### What are the software requirements?
1.	Python IDE
2.	R
3.	Microsoft Excel

### Where to download the data?
- Crime events 2019: <https://github.com/stccenter/crime-data-analysis/tree/master/Crime%20events%202019>
- Crime events 2020: <https://github.com/stccenter/crime-data-analysis/tree/master/Crime%20events%202020>
- Crime events with coordinates 0515-0615, 2020: <https://github.com/stccenter/crime-data-analysis/tree/master/Crime%20events%20with%20coordinates%200515-0615%2C%202020>
- Crime number statistics 2019: <https://github.com/stccenter/crime-data-analysis/tree/master/Crime%20number%20statistics%202019>
- Crime number statistics 2020: <https://github.com/stccenter/crime-data-analysis/tree/master/Crime%20number%20statistics%202020>


### How to get the results?
Run the below scripts. Install required packages for the scripts.
1.	geocoding.py
This script is used to convert addresses (like a street address) into geographic coordinates (like latitude and longitude).
    1.	package: geocoder, pandas, csv
    2.	variables that can be changed:
        a.	input_file – input file path.
        b.	output_file – output file path.
        c.	date - the date of crime events of the form mm/dd/yy
2.	statistic.py
This script is used to count the number of crimes per day in each city/county based on crime event data.
    1.	package: pandas
    2.	variables that can be changed:
        a.	input_file – input file path.
        b.	output_file – output file path.
3.	boxplot.py
This script is used to generate a boxplot of crime rates of all counties/cities.
    1.	package: os, numpy, pandas, matplotlib
    2.	variables that can be changed:
        a.	input_path – root directory of crime input file.
        b.	pop_file - input file with population.
4.	linechart.py
This script is used to generate a line chart of seven crime types.
    1.	package: os, numpy, pandas, matplotlib
    2.	variables that can be changed:
        a.	input_path – root directory of input file.
        b.	output_path – root directory of output image.
5.	pcc.py
This script is used to calculate Person Correlation Coefficient value between different variables.
    1.	package: pandas
    2.	variables that can be changed:
        a)	input_file – input file path.
        b)	output_file – output file path.
6.	ANN
    1. ANN.py
    This script is used to calculate the Average Nearest Neighbor value for the crime cases every day over the target region.
        1.	package: math, pandas, numpy, scipy
        2.	variables that can be changed:
            a.	input_file – input file path
            b.	output_file – output file path.
            c.	area – area of the county/city (square kilometer)
            d.	crime_type – the type of crime, including Total, Arrest, Arson, Assault, Burglary, Robbery, Shooting, Theft, Vandalism, and Other
    2. barchart.py
    This script is used to visualize the results of ANN.py through a bar graph.
        1.	package: pandas, numpy, matplotlib
        2.	variables that can be changed:
            a.	input_file – input file path.
7.	hotspot
    1. hotspot.py
    This script is used to analyze crime hotspots of a given day. A heat map layer will be created.
        1.	package: pandas, folium
        2.	variables that can be changed:
            a.	input_file – input file path.
            b.	output_file – output file path.
            c.	date – the date of crime events of the form mm/dd/yy
            d.	crime_type – the type of crime, including Total, Arrest, Arson, Assault, Burglary, Robbery, Shooting, Theft, Vandalism, and Other
        3.	parameters:
            a.	location – Latitude and Longitude of Map (Northing, Easting).
            b.	zoom_start – Initial zoom level for the map.
            c.  tiles – Map tileset to use.
            d.	control_scale – Whether to add a control scale on the map.
            e.	data – List of points of the form [lat, lng] or [lat, lng, weight].
            f.	max_val – Maximum point intensity.
            g.	min_opacity – The minimum opacity the heat will start at.
            h.	radius – Radius of each “point” of the heatmap.
            i.	blur – Amount of blur.
            j.	gradient – Color gradient config.
            k.	max_zoom – Zoom level where the points reach maximum intensity (as intensity scales with zoom).
    2. hotspot_withtime.py
    This script is used to analyze crime hotspots of a number of days. A dynamic heat map layer with time slider will be created.
        1.	package: pandas, folium
        2.	variables that can be changed:
            a.	input_file – input file path.
            b.	output_file – output file path.
            c.	crime_type – the type of crime, including Total, Arrest, Arson, Assault, Burglary, Robbery, Shooting, Theft, Vandalism, and Other
        3.	parameters:
            a.	location – Latitude and Longitude of Map (Northing, Easting).
            b.	zoom_start – Initial zoom level for the map.
            c.	tiles – Map tileset to use.
            d.	control_scale – Whether to add a control scale on the map.
            e.	data – list of list of points of the form [lat, lng] or [lat, lng, weight].
            f.	index – Index giving the label (or timestamp) of the elements of data.
            g.	max_opacity – The maximum opacity for the heatmap.
            h.	min_opacity – The minimum opacity the heat will start at.
            i.	radius – Radius of each “point” of the heatmap.
            j.	auto_play – Automatically play the animation across time.
            k.	display_index – Zoom level where the points reach maximum intensity (as intensity scales with zoom).

8.	Lasso.R  getting an error
This script is used to build a Lasso logistic regression model and export the coefficient of independent variables.
    1.	package: glmnet
    2.	variables that can be changed
        a.	setwd – current working path.
        b.	loadx – input file name with independent variables.
        c.	loady - input file name with dependent variable.
    3.	parameters:
        a.	x – matrix of predictor variables
        b.	y – the response or outcome variable, which is a binary variable.
        c.	family – the response type. Use “binomial” for a binary outcome variable.
        d.	alpha – the elasticnet mixing parameter. Allowed values include:
            -	“1”: for lasso regression
            -	“0”: for ridge regression
            -	a value between 0 and 1 (say 0.3) for elastic net regression.
        e.	type.measure – the loss used for cross-validation.
        f.	lambda – a numeric value defining the amount of shrinkage. Should be specify by analyst.
