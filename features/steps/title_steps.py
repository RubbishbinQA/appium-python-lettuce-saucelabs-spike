from lettuce import step, world
from nose.tools import assert_equal

@step('Given I navigate to the Python Home page')
def step_impl(step):
    world.driver.get('http://www.python.org')

@step('Then I see the page title is Welcome to Python.org')
def step_impl(step):
    assert_equal(world.driver.title, 'Welcome to Python.org')
