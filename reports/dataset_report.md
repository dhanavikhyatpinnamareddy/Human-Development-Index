# Dataset Quality Report

**Dimensions:** 6798 rows, 33 columns

### Data Types
```
Unnamed: 0                     int64
iso3                             str
country                          str
hdicode                          str
hdi_rank_2022                float64
gii_rank_2022                float64
year                           int64
hdi                          float64
life_expectancy              float64
pop_millions                 float64
hdi_f                        float64
hdi_m                        float64
life_expec_f                 float64
life_expec_m                 float64
expec_yr_school              float64
expec_yr_school_f            float64
expec_yr_school_m            float64
mean_yr_school               float64
mean_yr_school_f             float64
mean_yr_school_m             float64
gross_inc_percap             float64
gross_inc_percap_f           float64
gross_inc_percap_m           float64
gender_development           float64
gender_inequality            float64
secondary_education_f_%      float64
secondary_education_m_%      float64
seats_in_parliament_f_%      float64
seats_in_parliament_m_%      float64
labour_participation_f_%     float64
labour_participation_m_%     float64
co2_emission_tons            float64
mat_footprint_percap_tons    float64
dtype: object
```

### Missing Values
```
Unnamed: 0                      0
iso3                            0
country                         0
hdicode                       429
hdi_rank_2022                 429
gii_rank_2022                1320
year                            0
hdi                           627
life_expectancy                 0
pop_millions                    0
hdi_f                        1784
hdi_m                        1784
life_expec_f                    0
life_expec_m                    0
expec_yr_school               248
expec_yr_school_f             528
expec_yr_school_m             528
mean_yr_school                544
mean_yr_school_f              634
mean_yr_school_m              634
gross_inc_percap              139
gross_inc_percap_f           1506
gross_inc_percap_m           1506
gender_development           1784
gender_inequality            2087
secondary_education_f_%       981
secondary_education_m_%       981
seats_in_parliament_f_%       529
seats_in_parliament_m_%       529
labour_participation_f_%     1488
labour_participation_m_%     1488
co2_emission_tons              85
mat_footprint_percap_tons    1454
dtype: int64
```

### Duplicate Records: 0

### Country Count: 206

### Year Range: 1990 to 2022

### Summary Statistics
```
        Unnamed: 0  hdi_rank_2022  gii_rank_2022         year          hdi  \
count  6798.000000    6369.000000    5478.000000  6798.000000  6171.000000   
mean   3399.500000      96.854922      83.500000  2006.000000     0.670293   
std    1962.557897      55.771006      47.923577     9.522605     0.164414   
min       1.000000       1.000000       1.000000  1990.000000     0.212000   
25%    1700.250000      49.000000      42.000000  1998.000000     0.546500   
50%    3399.500000      97.000000      83.500000  2006.000000     0.692000   
75%    5098.750000     145.000000     125.000000  2014.000000     0.797000   
max    6798.000000     193.000000     166.000000  2022.000000     0.967000   

       life_expectancy  pop_millions        hdi_f        hdi_m  life_expec_f  \
count      6798.000000   6798.000000  5014.000000  5014.000000   6798.000000   
mean         68.544884    122.703025     0.671530     0.713682     71.189861   
std           9.501335    561.825531     0.166486     0.143888      9.911176   
min          14.098000      0.009182     0.191917     0.274102     15.663000   
25%          62.687250      1.989805     0.552527     0.611195     65.038500   
50%          70.491500      7.914909     0.694996     0.728110     73.684000   
75%          75.419894     28.194687     0.804586     0.817185     78.549500   
max          86.895000   7940.608797     0.957148     0.977383     88.881000   

       ...  gender_development  gender_inequality  secondary_education_f_%  \
count  ...         5014.000000        4711.000000              5817.000000   
mean   ...            0.931731           0.390031                49.855594   
std    ...            0.075246           0.192830                29.853427   
min    ...            0.383000           0.009000                 0.420000   
25%    ...            0.898000           0.224000                23.369720   
50%    ...            0.954000           0.404000                49.100111   
75%    ...            0.982000           0.547500                76.408417   
max    ...            1.072000           0.838000               100.000000   

       secondary_education_m_%  seats_in_parliament_f_%  \
count              5817.000000              6269.000000   
mean                 56.345271                16.507989   
std                  27.272712                10.928861   
min                   2.050000                 0.010000   
25%                  33.802000                 8.333333   
50%                  54.533215                14.545455   
75%                  81.527327                22.727273   
max                 100.000000                57.547170   

       seats_in_parliament_m_%  labour_participation_f_%  \
count              6269.000000               5310.000000   
mean                 83.492011                 49.318145   
std                  10.928861                 15.797188   
min                  42.452830                  5.610000   
25%                  77.272727                 40.552500   
50%                  85.454545                 50.780000   
75%                  91.666667                 58.235000   
max                  99.990000                 94.400000   

       labour_participation_m_%  co2_emission_tons  mat_footprint_percap_tons  
count               5310.000000        6713.000000                5344.000000  
mean                  72.360992           4.520991                  12.769886  
std                    9.196551           6.241956                  12.359313  
min                   29.630000           0.019352                   0.000100  
25%                   66.720000           0.624496                   4.137650  
50%                   73.020000           2.340953                   8.523550  
75%                   78.600000           6.221754                  17.442200  
max                  100.000000          76.612949                 140.815700  

[8 rows x 30 columns]
```
