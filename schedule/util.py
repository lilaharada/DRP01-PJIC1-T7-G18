# coding: utf-8
import json


def date_handler(obj):
    """
    Handles JSON serialization for datetime values
    """
    return obj.isoformat() if hasattr(obj, 'isoformat') else obj


def convert_field_names(event_list):
    """
    Converts atribute names from Python code convention to the
    attribute names used by FullCalendar 
    """
<<<<<<< HEAD
<<<<<<< HEAD
=======
    print(event_list)
>>>>>>> 16093fb (created app schedule, config and tests)
=======
>>>>>>> 7a3b3ad (new corrections apps base)
    # for event in event_list:
    #     for key in event.keys():
    #         event[key] = event.pop(key)

    return event_list


def snake_to_camel_case(s):
    """
    Converts strings from 'snake_case' (Python code convention)
    to CamelCase
    """
    new_string = s

    leading_count = 0
    while new_string.find('_') == 0:
        new_string = new_string[1:]
        leading_count += 1

    trailing_count = 0
    while new_string.rfind('_') == len(new_string) - 1:
        new_string = new_string[:-1]
        trailing_count += 1

    new_string = ''.join([word.title() for word in new_string.split('_')])
    leading_underscores = '_' * leading_count
    trailing_underscores = '_' * trailing_count
    return leading_underscores + new_string[0].lower() + new_string[1:] + trailing_underscores


def events_to_json(events_queryset):
    """
    Dumps a CalendarEvent queryset to the JSON expected by FullCalendar
    """
    events_values = list(events_queryset.values(
        'id', 'title', 'start', 'end', 'all_day'))
    events_values = convert_field_names(events_values)
<<<<<<< HEAD
<<<<<<< HEAD

    return json.dumps(events_values, default=date_handler)


def calendar_options(event_url, default_view, options):
<<<<<<< HEAD
=======
    print(events_values)
=======

>>>>>>> ac9891b (corrections apps)
    return json.dumps(events_values, default=date_handler)


def calendar_options(event_url, initial_grid, options):
>>>>>>> 16093fb (created app schedule, config and tests)
=======
>>>>>>> 98c1c6d (corrects on apps)
    """
    Builds the Fullcalendar options array

    This function receives two strings. event_url is the url that returns a JSON array containing
    the calendar events. options is a JSON string with all the other options.
    """
<<<<<<< HEAD
<<<<<<< HEAD
    default_view = default_view
    event_url_option = 'events: "/%s", plugins: ["interaction", "dayGrid", "timeGrid", "core", "list", "luxon", "moment", "moment-timezone", "rrule"], defaultView: "%s"' % (
        event_url, default_view)
=======
    event_url_option = 'events: "/%s", initialView: "%s" ' % (
        event_url, initial_grid)
>>>>>>> 16093fb (created app schedule, config and tests)
=======
    default_view = default_view
    event_url_option = 'events: "/%s", plugins: ["interaction", "dayGrid", "timeGrid", "core", "list", "luxon", "moment", "moment-timezone", "rrule"], defaultView: "%s"' % (
        event_url, default_view)
>>>>>>> 98c1c6d (corrects on apps)
    s = options.strip()
    if s is not None and '{' in s:
        pos = s.index('{') + 1
    else:
        return '{%s}' % (event_url_option)
    return s[:pos] + event_url_option + ', ' + s[pos:]
