# EDA and Statistical Justification

## Pearson Correlation Matrix
|                      |   life_expectancy |   expec_yr_school |   mean_yr_school |   log_gross_inc_percap |      hdi |
|:---------------------|------------------:|------------------:|-----------------:|-----------------------:|---------:|
| life_expectancy      |          1        |          0.801981 |         0.738343 |               0.838168 | 0.917285 |
| expec_yr_school      |          0.801981 |          1        |         0.827035 |               0.802339 | 0.920008 |
| mean_yr_school       |          0.738343 |          0.827035 |         1        |               0.774279 | 0.899698 |
| log_gross_inc_percap |          0.838168 |          0.802339 |         0.774279 |               1        | 0.940563 |
| hdi                  |          0.917285 |          0.920008 |         0.899698 |               0.940563 | 1        |

## Multicollinearity Analysis (VIF)
|    | feature              |       VIF |
|---:|:---------------------|----------:|
|  0 | const                | 117.338   |
|  1 | life_expectancy      |   4.0055  |
|  2 | expec_yr_school      |   4.43781 |
|  3 | mean_yr_school       |   3.5618  |
|  4 | log_gross_inc_percap |   4.27711 |

## Discussion
The variables show strong positive correlations with HDI. Since HDI is a composite index built from these exact indicators, multicollinearity is fundamentally expected and conceptually sound.
