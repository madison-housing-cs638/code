import pandas as pd
import numpy as np

inflation_map = {
  1900:26.83, 1901:30.62, 1902:30.27, 1903:29.58, 1904:29.24, 1905:29.58, 1906:28.92, 1907:27.69, 1908:28.29, 1909:28.60,
  1910:27.40, 1911:27.40, 1912:26.83, 1913:26.25, 1914:25.99, 1915:25.73, 1916:23.85, 1917:20.31, 1918:17.21, 1919:15.02,
  1920:13.00, 1921:14.52, 1922:15.47, 1923:15.20, 1924:15.20, 1925:14.85, 1926:14.68, 1927:14.94, 1928:15.20, 1929:15.20,
  1930:15.56, 1931:17.10, 1932:18.97, 1933:19.99, 1934:19.40, 1935:18.97, 1936:18.70, 1937:18.05, 1938:18.43, 1939:18.70,
  1940:18.57, 1941:17.68, 1942:15.59, 1943:15.02, 1944:14.77, 1945:14.44, 1946:13.33, 1947:11.66, 1948:10.78, 1949:10.92,
  1950:10.78, 1951:10.00, 1952:9.81, 1953:9.73, 1954:9.66, 1955:9.70, 1956:9.56, 1957:9.25, 1958:8.99, 1959:8.93,
  1960:8.78, 1961:8.69, 1962:8.61, 1963:8.49, 1964:8.38, 1965:8.25, 1966:8.02, 1967:7.78, 1968:7.47, 1969:7.08,
  1970:6.70, 1971:6.42, 1972:6.22, 1973:5.85, 1974:5.27, 1975:4.83, 1976:4.57, 1977:4.29, 1978:3.99, 1979:3.58,
  1980:3.15, 1981:2.86, 1982:2.69, 1983:2.61, 1984:2.50, 1985:2.42, 1986:3.37, 1987:2.29, 1988:2.20, 1989:2.10,
  1990:1.99, 1991:1.91, 1992:1.85, 1993:1.80, 1994:1.75, 1995:1.71, 1996:1.66, 1997:1.62, 1998:1.59, 1999:1.56,
  2000:1.51, 2001:1.47, 2002:1.44, 2003:1.41, 2004:1.38, 2005:1.33, 2006:1.29, 2007:1.25, 2008:1.21, 2009:1.21,
  2010:1.19, 2011:1.16, 2012:1.13, 2013:1.12, 2014:1.10, 2015:1.10, 2016:1.08, 2017:1.06, 2018:1.04, 2019:1.02,
  2020:1.00,
}


def inflate(amount, year, to=2020):
  if(year < 1900 or year > 2020):
    return 0

  if(to != 2020):
    inflation_factor = inflation_map[year]
    return inflation_factor * amount
  else:
    assert year <= to
    inflation_factor_from = inflation_map[year]
    inflation_factor_to = inflation_map[to]

    return (inflation_factor_from / inflation_factor_to) * amount

