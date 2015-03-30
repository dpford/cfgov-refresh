from behave import given, when, then
from hamcrest.core import assert_that
from hamcrest.core.core.isequal import equal_to
from hamcrest.library.text.stringcontains import contains_string
from hamcrest.library.collection.isin import is_in


@then(u'I should see "{num_events}"')
def step(context, num_events):
    actual_results = context.events.get_results_number()
    assert_that(actual_results, equal_to(num_events))

@then(u'I should see "{tag}" displayed under "{event_name}"')
def step(context, tag, event_name):
    tags = context.events.get_tags()
    assert_that(tag, is_in(tags))


@then(u'I should see "{location}" displayed under "{event_name}"')
def step(context, location, event_name):
    actual_location = context.events.get_location(event_name)
    assert_that(actual_location, equal_to(location))

@then(u'I should see "{date}" displayed under "{event_name}"')
def step(context, date, event_name):
    actual_date = context.events.get_date(event_name)
    assert_that(actual_date, equal_to(date))

@then(u'I should see "{time}" displayed under "{event_name}"')
def step(context, time, event_name):
    actual_time = context.events.get_time(event_name)
    assert_that(actual_time, equal_to(time))