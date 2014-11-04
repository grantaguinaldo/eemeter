from eemeter.computations import annualized_mean_usage
from eemeter.computations import weather_normalize

from eemeter.usage import Usage
from eemeter.usage import electricity
from eemeter.units import kWh
from eemeter.units import BTU

import arrow

import pytest

EPSILON = 10e-6

##### Fixtures #####

@pytest.fixture
def usage_one_year_electricity():
    return [Usage(1000,kWh,electricity,arrow.get(2012,1,1).datetime,arrow.get(2012,2,1).datetime),
            Usage(1100,kWh,electricity,arrow.get(2012,2,1).datetime,arrow.get(2012,3,1).datetime),
            Usage(1200,kWh,electricity,arrow.get(2012,3,1).datetime,arrow.get(2012,4,1).datetime),
            Usage(1300,kWh,electricity,arrow.get(2012,4,1).datetime,arrow.get(2012,5,1).datetime),
            Usage(1400,kWh,electricity,arrow.get(2012,5,1).datetime,arrow.get(2012,6,1).datetime),
            Usage(1500,kWh,electricity,arrow.get(2012,6,1).datetime,arrow.get(2012,7,1).datetime),
            Usage(1400,kWh,electricity,arrow.get(2012,7,1).datetime,arrow.get(2012,8,1).datetime),
            Usage(1300,kWh,electricity,arrow.get(2012,8,1).datetime,arrow.get(2012,9,1).datetime),
            Usage(1200,kWh,electricity,arrow.get(2012,9,1).datetime,arrow.get(2012,10,1).datetime),
            Usage(1100,kWh,electricity,arrow.get(2012,10,1).datetime,arrow.get(2012,11,1).datetime),
            Usage(1000,kWh,electricity,arrow.get(2012,11,1).datetime,arrow.get(2012,12,1).datetime),
            Usage(900,kWh,electricity,arrow.get(2012,12,1).datetime,arrow.get(2013,1,1).datetime)]

@pytest.fixture
def usage_one_summer_electricity():
    return [Usage(1600,kWh,electricity,arrow.get(2012,6,1).datetime,arrow.get(2012,7,1).datetime),
            Usage(1700,kWh,electricity,arrow.get(2012,7,1).datetime,arrow.get(2012,8,1).datetime),
            Usage(1800,kWh,electricity,arrow.get(2012,8,1).datetime,arrow.get(2012,9,1).datetime)]

@pytest.fixture
def degrees_f_one_year():
    return [20,15,20,35,55,65,80,80,60,45,40,30]

##### Tests #####

def test_annualized_mean_usage(usage_one_year_electricity):
    assert (1200 - annualized_mean_usage(usage_one_year_electricity,kWh)) < EPSILON

def test_annualized_mean_usage(usage_one_summer_electricity):
    assert (1700 - annualized_mean_usage(usage_one_summer_electricity,kWh)) < EPSILON

def test_weather_normalize_usage(usage_one_year_electricity_with_degrees_f):
    normals = None
    F = None
    normalized_usage = weather_normalize(usage_one_year_electricity_with_degrees_f,F,normals)
    assert normalized_usage is not None

def test_coefficient_of_variance_of_root_mean_square_error(usage_one_year_electricity_with_degrees_f):
    assert False