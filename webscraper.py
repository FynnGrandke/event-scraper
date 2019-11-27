from event_modules.meetup_module import getMeetupEvents
from event_modules.eventbrite_module import getEventbriteEvents
from event_modules.alleventsin_module import getAlleventsinEvents
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser("event scraper")
    parser.add_argument("website", help="The website from which to get events.", type=str)
    args = parser.parse_args()

    # Check for the event
    if args.website == 'meetup':
        getMeetupEvents()
    else:
        if args.website == 'eventbrite':
            getEventbriteEvents()
        else:
            if args.website == 'alleventsin':
                getAlleventsinEvents()
            else:
                # If argument equals no event
                print('NO EVENTS FOR', args.website)
    print('END for', args.website)
