# AnsibleFest Contributor Summit

FULL DAY AGENDA AND INFORMATION
London, Wednesday 21 June 2017


Notes on organization / agenda planning:
Original planning etherpad: https://public.etherpad-mozilla.org/p/ansible-summit-june-2017
Each meeting has its own etherpad; for breakout (multi-track) parts of day, each etherpad indicates individual IRC channels and bluejeans sessions.
BUCKET LIST: Things we didn't get to, things we wished we had more time for, things that came up that we didn't realize were things to talk about it until then? BUCKET LIST. Bottom of this etherpad. (Or the individual etherpads.)


ABOUT THE SCHEDULE AND PESKY TIME ZONES:
Note: All times listed are in BST (UTC+1). Because we are in London, this time.
To convert to your time zone, use
http://www.timeanddate.com/worldclock/converter.html
Or, to determine when the day begins in your area more easily: https://www.timeanddate.com/worldclock/fixedtime.html?msg=AnsibleFest+Contributor+Summit&iso=20170621T09&p1=136&ah=7 (SOMEONE TEST THIS PLZ: Seems to work)

GENERAL SCHEDULE:
Morning: Main track. 9:00am - 12:00pm
9:00am - 9:30am-ish: Breakfast / General Discussion / Intro
9:30am - 10:30am: Core Update
10:30am -11:00am:  Contributor Involvement
11:00am - 12:00pm: PR and Issue Backlog + Metrics

Lunch: Noon - 1pm, follow the leader to the food

Afternoon: Main track: 1:00pm - 2:30pm: Testing.

Afternoon Snack time and health break: 2:30pm - 2:45pm.
For the health and safety of those around you.

Afternoon Breakout Tracks: 2:45pm - 3:45pm.
Track 1: Windows Working Group
Track 2:  Zuul deep dive & how to fix some of the hacks
Track 3: Ansible + Containers

Contributor Summit Wrap-up: 3:45pm - 4:00pm.


EXPANDED DETAILED SCHEDULE:
Note: Each track has its own etherpad; all the magical suggestions were condensed / aggregated into those etherpads. Super-high-level topics are provided here, along with links to etherpads, containing video, irc, etc. information.

## THINGS TO NOTE AT BEGINNING OF DAY:
* Deets about lunch & cocktails (the cocktails are not at lunchtime. to be clear.). and swag
* Remind ppl about Microphone stuff, IRC stuff, if you also want to be on bluejeans mute yourself because microphones (assuming they set them up that way), any other logistics?
* Ensure we have Laptops + Moderator codes for each room
* Esp. note the #ansible-meeting-2 detail
* Robyn & Greg to actually set up and configure bluejeans for their sessions and remember to hit the record button :) (And robyn to download the things at the end of the day!)
* Remind people of the bucket list at the bottom of page.
* Get everyone to "sign in" at the end of the page
* IRC in $channel; Bluejeans on $channel

## MAIN TRACK: Morning

* 9:00am Breakfast and general discussion and saying hello (maybe "Progress since last Contributors Summit (brief update, everybody)" here?)
* 9:30am: Core update. https://public.etherpad-mozilla.org/p/ansible-summit-june-2017-core

  * General topics:
  
    * Progress: 10 minute summary of what action items were accomplished from last contributor summit
    * Python 3 status
    * Possibly: core vs. supported vs. other futures discussion
    * Other core update things? Please add to etherpad https://public.etherpad-mozilla.org/p/ansible-summit-june-2017-core

* 10:30 - 11:00am: Contributor Involvement https://public.etherpad-mozilla.org/p/ansible-summit-june-2017-contributor-involvement

    * General topics:
    * Greg will have things to discuss.

* 11:00am - 12:00pm: PR and Issue Backlog + Metrics: https://public.etherpad-mozilla.org/p/ansible-summit-june-2017-backlog

  * PR / Issue Backlog topics:
  * Current status: Show me the numbers!
  * Suggestions for improvement
  * Improving communication amongst maintainers
  * Improving triage
  * Ansibot: How to leverage?
  * Lack of tests, automerge fails, general discouragement
  * Metrics Topics:

    * What should we count?

* LUNCHTIME: 12:00pm - 1:00pm

## AFTERNOON MAIN TRACK (everyone):

* 1:00pm - 2:30pm: Testing: https://public.etherpad-mozilla.org/p/ansible-summit-june-2017-testing

  * Condensed Testing topics:
  * Mini-Zuul Update. No more than 10 minutes.
  * Note: Beat Monty with Squirrels if he goes over time (Like seriously, 10 minutes. tops.)
  * Gundalow to present on 1y of Testing Working Group
  * Core support vs. Community support + futures here
  * Increasing test coverage / integration tests
  * Dealing with partner test infrastructure
  * Testing + module maintainers
  * Shippable: Making it less ...crappable.
  * Windows 10 / Windows 2016 testing (could move to windows, may need to stay here; will defer to windows experts to pipe up)

## AFTERNOON SNACK BREAK: ~2:30pm - 2:45pm

Snacks will be in hallway, grab your things and a bio break and pollute your lungs if needed, then come on back

## AFTERNOON BREAKOUT TRACKS: 2:45-3:45

(Note: Each breakout track may be in its own room, or area, but each should have its own irc channel, etherpad, and bluejeans / video information (recorded, plz!). Details should be in sub-etherpads.

### Afternoon Track 1: Windows Working Group: https://public.etherpad-mozilla.org/p/ansible-summit-june-2017-Windows

Condensed Windows WG topics

* Have a submeeting at Fest. HEY, DONE! Woot.
* Open Items: https://public.etherpad-mozilla.org/p/Ansible_Windows_Community_Plan
* Wiki for progress tracking?
* New meeting times
* Powershell:

  * Coding standards
  * Support for new versions (5.0+)

* WSL to get more windows users
* DSC Support plan
* Review committers list
* Testing. May overlap with testing from the testing session prior also.

### Afternoon Track 2: Zuul deep dive & how to fix some of the hacks:  https://public.etherpad-mozilla.org/p/ansible-summit-june-2017-Zuul

NOTE: NEED SOME CORE TEAM FOLKS HERE. DESPERATELY. Save jlk from being sad at weird hacky things. Please!
Bluejeans/video: https://bluejeans.com/2413805790/

Condensed Zuul Topics:

* Deeper (probably) discussion about upcoming next-steps for starting to run Zuul v3 jobs against ansible/ansible. Possible quick overview of status/shape - but more focused on "things potentially likgely to happen in the next month or two" (mordred) (jlk)
Zuul Automerge
* Deeper Dive and All the DIrty hacks. SSIA.

### Afternoon Track 3: Ansible & Containers: https://public.etherpad-mozilla.org/p/ansible-summit-june-2017-ansible-and-containers

IRC: #ansible-container ?

Bluejeans/video: https://bluejeans.com/3008457278/

Containerized, err, ahem, condensed container topics: Ansible-container, Ansible + containers, Ansible + Kubernetes, Helm

## WRAP-UP:  3:45pm - 4:00pm

* Note about "always more time":
* Anything we didn't get to that we want to discuss on Thursday? Haz room, can chat. Need to know rooms. $fixme
* Reminder about boat.
* Reminder: bring a camera so we can sing the song.
* Reminders about IRC logs, video posting: Please put those in the appropriate places. If nobody remembered to make a spot to put them, be bold!

## BUCKET LIST

https://www.ihasabucket.com/images/walrus_bucket.jpg
(aka: Things from the original list that didn't seem to have a place to live by the end of trying to square away the agenda in combo with known attendees)

Maybe
Big Proposal review (List and get votes on list of proposals)

## Not doing

* Web frontend - Is this just Tower?
* No discussion around Python 3 (apart from anything relevant in Testing)
* Docs - Doesn't sounds there is anything there to talk about outside of Windows
* Cloud + "Cloud agnostic VM management module" + "Kubernetes support of some sort"
* Networking (Possibly move to Networking Hub), not sure who is attending that is interested

  * Not as many votes as other sections. Gundalow wonders if we can arrange a dedicated online meeting at somepoint

## Who is here

It would be really helpful if anyone that attended (physically or virtually) signed in

* Name, IRC, GitHub
* John Barker, gundalow, gundalow
* Andrea Tartaglia, shaps, shaps
* Dag Wieers, dag, dagwieers
* Monty Taylor, mordred, emonty
* Will Thames, willthames, willthames
* Yanis Guenane, spredzy, Spredzy
* Ryan Brown, ryansb, ryansb (remote)
* Michael Scherer, misc, mscherer (remote)
* Jordan Borean, jborean93 (remote)
* Toshio Kuratomi, abadger1999, abadger
* Sloane Hertel, shertel, s-hertel (remote)
* Jon Hawkesworth (jhawkesworth)
* Tomas Tomecek, ttomecek, TomasTomecek
* Frédéric Lepied, flepied, fredericlepied

