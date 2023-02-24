---
title: Ansible Community Strategy 2023
author: Greg Sutcliffe
date: 2023-02-24
format:
  html:
    toc: true
    theme: cerulean
    embed-resources: true
---

In the
[last article](https://ansible.github.io/community/posts/state_of_the_community_2023.html)
we covered metrics describing the community today, as well as some reasoning
into why that might be. In this article, I'll lay out my view of how to go
about fixing it.

## Communities as "neighbourhoods"

Let me start with an analogy, to try to illustrate what I think is missing in
our community. For many people, the word "community" will conjure up an idea of
a locality - perhaps a village or small town - which works to improve the place
the people live in. This often looks like the following (at least where I live,
in the UK :P)

- Most residents will agree that improving the community is worth doing - but
  they might not all agree on how. That's mostly fine because people can
  specialise (you might organise maintenance of paths, etc; I'll get funding for
  the new sports ground), so we can get lots done for the community as a whole.
  The mission is pretty clear, and it'll only matter when there is opportunity
  cost of doing something.
- It's clear that (in most countries, anyway) what goes on **inside** a house
  is largely their business. So long as they're not playing overly-loud music
  or setting fire to their neighbour's fence, it's all good. Nobody wants to
  police things to that degree (and it's largely unworkable anyway).
  - However, if one house starts to have an impact on those around it, then
    there are ways to sanction those people (legal options, yes, but also
    social contracts which are often stronger), and bring them back into line.
- It's also true that while *sometimes* whole districts are planned at once,
  often development is more organic, as people buy land and build on it. A
  central planner isn't **needed** (but is sometimes present).
- They will have a way to communicate with interested residents - crucially,
  even those who might not be active right now. This would have been a town
  notice board or similar in times past (and still is in my village, actually),
  but today it might equally be a messaging chat room or social website group.
- There will be a way to debate things of interest to the community - issues,
  upcoming events, local goverance elections, etc. Typically this is a town
  hall or similar venue where regular meetings are held.

That analogy actually works pretty well for us too. If we think of each of the
[projects](https://docs.ansible.com/ecosystem) and working groups as "houses", forming
a "neighbourhood" that is the whole Ansible community, then some conclusions
naturally fall out it.

Firstly, we have a mission, and while it might be a good time to refine it, we
are generally agreed that automation is our thing. Second, the "houses"
(projects) are indeed largely independant, e.g DevTools does not tell AWX how
to run their "house". In fact, most of the projects are getting along just
fine.

Where it gets interesting is the inter-project communication (between houses,
if you will). Right now, it feels to me like the "social cost" of completely
doing your own thing isn't especially high, which leads to a wide array of
behaviours. That's fine **inside** a house/project but not when it leads to
difficulties across the whole neighbourhod.

Relating to the lack of a central planner, this is fine - but all villages need
power, water, connectivity, etc. This is usually the job of a regulator, and
that distinction is worth exploring, probably in a later post.

However, it's the last two points which are **key** to this post, as they
*directly* relate to the two ways I think we can improve things in the Ansible
community today - because **a "notice board" is a website**, and **a "town
hall" is a forum**.

## Websites, branding, and overloading

Let's start with the "notice board" for our neighbourhood. As we've already
noted, there's no single point-of-call for finding out what's going on with
Ansible today. We have no way for the community to write about interesting
things, or announce new projects, etc. We have `ansible-announce`, but the
mailing list does *not* get much traffic. We have the Bullhorn, but how widely
known is it?

Realistically, part of the problem is that the word "Ansible" means many
things, and "ansible.com" can't serve them all. It could mean:

- The language we write playbooks in
- The base package that delivers the language
- The full package with collections included
- The wider community / project
- The Red Hat product

The last two are the biggest problem. Today, ansible.com is Red Hat's product
site - that's not a criticism, just a fact. However, as a result, the pages are
product pages, the blog is a product blog, and so on. It would not be right to
simply open this up to the community for editing, as it's **not the same
Ansible we're talking about**.

The only way to resolve this is to separate the meanings. One could make the
argument that the word "Ansible" belongs to the community, and the product
should move to another site. That's not wrong, but commercial systems move
slowly, and I believe we need to fix this sooner. The lack of focus for new
community members, and the lack of a voice for existing ones, is hurting us. 

It's common for upstream projects to have their own name, and web presence. So,
**I am proposing that we create a new short text (1-3 words) to reduce the
overloading**. We can debate it, but "Ansible Community" seems a good
placeholder for now. We then use that to look at possible **new DNS domains**
(ansible.community is available to us, for example), and then we can look at
**setting up a new site**. I already have approval for this from within Red
Hat, so we can start as soon as the community approves it.

In terms of function, at least to start with, I see a fairly standard setup -
GitHub repo, static site generator, appropriate pages for contributor pathways,
events, communication etc. Obviously a blog section too. This is all
straightforward and standard practice, we just have to **do** it.

Of course, having the site be public and open to collaboration is key to
improving those tenets I described last time. Also, I can't foresee all the
usecases we'll have for this. The obvious thing to do is to **create a new
Working Group to oversee building it**, and that will also be in my proposal.

### Summary

- New short text for the community (to de-overload "Ansible")
- New DNS property for hosting the community project
- New website
- New Working Group

## Forums, fragmentation, and culture

Now to the longer, trickier part. I'm well aware that not everyone loves
forums, so let me do a rare thing, and play the ad-hominem card. I **really**
believe this will work - indeed, [I have done
this](https://community.theforeman.org/t/propsing-a-move-from-google-groups-to-discourse/7450)
for multiple other communities and [it **has**
worked](https://events19.linuxfoundation.org/wp-content/uploads/2017/12/Migrating-a-Community-Why-How-We-Moved-from-a-Mailing-List-to-a-Forum-Greg-Sutcliffe-Red-Hat.pdf).
If you find yourself unsure on this, give it a chance.

The biggest theme, by far, in all of these posts, in my discussions internally,
in discussions with the community, **everywhere** I look, is fragmentation.
Most of what we see before us today is at least partly attributable to the fact
that we *don't* have a common place to figure things out, or for new people to
ask questions. We **need** to fix this.

For clarity, I am proposing to use **[Discourse](https://discourse.org)** as
the software, as it is **by far** the best implementation I have seen. There is
no "killer feature" that I can point to for why - it is simply full of hundreds
of quality-of-life features, so many that I continue to be surprised by it even
after 5+ years as a user. I think that it is no accident that it used by
[Python](https://discuss.python.org/latest),
[Fedora](https://ask.fedoraproject.org/),
[Mozilla](https://discourse.mozilla.org),
[Ubuntu](https://discourse.ubuntu.com/),
[Nextcloud](https://help.nextcloud.com/),
[Pulp](https://discourse.pulpproject.org/),
[LetsEncypt](https://community.letsencrypt.org/),
[Sailfish](https://forum.sailfishos.org/) .... the list goes on. It has become
the de-facto standard for async discusion.

Rather than try to list features, I'll outline **some** (this is not
exhaustive) of the things Discourse could help with, and then I'll tackle some
of the criticisms I think will come up. 

### A new generation of users, but existing users too

Nearly 2 years ago, I argued for including Matrix in our community (which the
data shows to have been a good thing for our chat spaces). I did so by making
the argument that we need to reach the next generation of users and
contributors. That problem exists in more places than just chat.

Anecdotally, I have heard comments like "I wouldn't know how to sign up to a
mailing list if I wanted to", "mailing lists are newsletters", "sign-up means
web, how do I web an email list?", and so on. We need to meet people where they
are today. Discourse supports basic email registration, but also login via
GitHub, Google, Facebook, Discord, Twitter, and other SSO systems - at the
least, we would have GitHub there.

Existing users are not forgotten either, as you can interact with Discourse by
mail - other than updating your addressbook for the email to use for starting a
new topic, little changes.

### Meeting support needs

We've seen a migration to places like StackOverflow (SO), etc for support
questions. We know that the #users:ansible.com (#ansible) room is busy. There
is an unoffical Discord with many users, and multiple other Slack instances.
There is no shortage of people needing help.

However, as SO shows, sometimes long-form slower replies are more useful than a
chatroom. Chat rooms depend on the right people being online, and often
question aren't that urgent (and pastebins are less of a problem). I think the
lack of a common community site/DNS has prevented us from creating this before,
and so people went where they could (eg SO).

We can do a better job of helping our users, and building a dedicated support
community around that. The use of the Solved plugin can give us similar
behaviour to SO, but in a place where we get integration & signposting to the
rest of the community & projects. Appropriate use of tags/groups can really
help get the right people involved without overwhelming single people.

Things like support are needed by all community parts. Today knowledgable
people who help other users are fragmented across too many places which dilutes
that knowledge. A self-supporting user community is something I'd love to see
more of, and the fact that I see exactly such a group of people (a) in other
projects' forums, and (b) in our own chatrooms, on SO, and in other places
gives me hope.

### Becoming async-first

Sync meetings exclude voices - both by timezone, and because quieter folks
might not be comfortable speaking up. Also those with English as a 2nd language
might struggle, both because the speed might make it hard to keep up, and
because chat can be hard to use with a translation system. Being async-first
means we get the best possible discussion, at the expense of speed - a
worthwhile tradeoff, I think, as we tend not to move quickly anyway, and
probably shouldn't, if we want the full wisdom of the crowd (e.g. some people
may be on holiday!).

One area we called out earlier was cross-project discussion, and I think this
can *hugely* benefit from a forum. Having a place to discuss architecture,
future plans, ways to solve issues, etc is necessary, but what really shines
here is being able to include the right people, via groups & tags that actually
work across the scope of the whole community (unlike on GitHub).

I've spoken with some people internally, and there is some support for bringing
more of our internal architecture discussions upstream. This would be a perfect
place to start such a thing, rather than creating *yet another GitHub repo that
no one can find*.

### Discoverability & archival

Mailing lists have a number of problems, but here I'll focus on 2. Firstly,
they are a high barrier - a user generally won't sign up to a dev list, even
though they might have a valid input for a given technical discussion. That's a
direct loss (see Wisdom of the Crowd in the previous article). Secondly, it's
hard to get people to sign up to new lists, and hard to decommission them
later.

This translates into a particular problem with working groups. Spinning up a
new working group has a high cost because people don't know to sign up, and
then when the WG is done, you have an old list hanging around.

Contrast this to a forum. New categories are free, and can be re-organised as
well (and the URLs don't break). So creating #working-groups/website is
essentially free, and is immediately visibile to **everyone** who has a forum
account (no new signup), and later could be moved to
#working-groups/inactive/website later on. Indeed, if it becomes active again
in the future, in can be moved back. Of course, new categories can be given
incoming email addresses to function as an email list too. Much, much easier to
maintain, and will have higher participation.

Categories can also come with their own rules, such as the use of up-voting or
mark-as-solved, allowing each sub-community to act as it needs, while staying
part of the cohesive whole.

### Project record

Right now, I have an archive of 75k emails from `ansible-project` on my disk.
The only reason I could get this out of Google Groups was because of personal
contacts - Google Takeout was broken (see
https://support.google.com/groups/thread/181378162?hl=en which has not been
answered). Google has demonstrated repeatedly that Groups is unmaintained (look
for example at the recurring issues with search, which have taken *years* to
fix, and some still aren't), and I worry that we'd lose the archive of our
history, if/when Google decide to sunset it. This is very, very, *very* close
to vendor lock-in.

Similarly, we use Zodbot for our chat meetings. While I would like to see more
of that go async (see above); for now, it happens, and the logs go to
fedoraproject.org (although often copied to GitHub afterwards). Again, we don't
own that, and while I trust Fedora more than Google, it's still not ideal.

All this can be imported to Discourse, and we can also import other things such
as meeting logs and GitHub Discusions too. Just as I argued with Matrix, we
should own our project, and having the new DNS gives us the chance to do so. I
want to know that in 5 years time I'll be able to go and read these kind of
discussions on our community site.

In addition, things like better search, tagging, "similar posts" suggestions
while writing, and so on make using that record easier for people too. But such
things are powered by content, and thus work best if we bring our content
together.

### Groups

Groups have huge power in Discourse, on two levels. Public groups can be
@-mentioned in a post and the folks in that group will get a notification.
Groups can also be open to new joiners, or invite only, so for interest-based
groups (eg. @edge) we can allow anyone to add themselves and be notified - but
we can restrict access to others (eg @core) and make sure the right people are
in there.

This mitigates the burnout / dogpile problem, where a helpful person answers
users question, and then starts to get asked directly for help by more and more
people. By tagging a group, they can be notified whilst we avoid naming people
in a post, which avoids burnout. For people with high traffic, being in the
right group(s) and subscribing to the right tags should keep traffic to the
essential (and be easier to filter away from firehose of GitHub trafic, because
it's a different domain).

### Trust & Decentralising Power

Discourse has several features that improve our ability to scale with minimal
effort from the Community team, which speaks directly to the goal of
decentralising power.

Trust levels are automatic (mostly) and almost any action can be tied to them.
For example, to prevent spam a user must reach level 1 (takes about 10min)
before being able to use email to reply to topics. But this goes much further,
for example you could have a calendar category with all the community events
(meetings, public demos, conferences) and anyone of (say) trust level 2+ could
freely create events without gatekeeping. This has many applications for us.

Finally, private groups can be used to decentralise power. A group can have an
incoming email address which bypasses the spam filters listed above. That means
you can use a group to, say, register for hosting or social media, and the
members of that group would have power over password resets, etc. Even the
privacy, security, and code-of-conduct addresses could go here, and the
membership of the groups can be updated as needed. Likewise groups can be used
to democratise infrastructure support and so on.

### Accessibility

Lots of small wins here, I think. First the downside - it's true that mailing
lists are naturally screen-reader friendly, being plain text, while a web
interface can be less so. However, you can interact with Discourse by mail, and
I believe that screen-reader compatibilty for the web view is decent these days
(I don't use one, but if anyone does, please test on meta.discourse.org as it
will be up-to-date, and let me know).

On the plus, there's full keyboard-only support, we can easily support other
languages better (a category each perhaps? as discussed above, they're easy to
make), we can write modify the CSS/themes, and we'll be providing a single
place to access things that works - while a ML might work with a screen reader,
does GitHub? Does ansible.com? Does *trying* to find the right place to join
in? 

Since I *don't need accessiblity* I'm not sure what else is needed, but I'm
happy to learn, please let me know.

### Integration / Plugins

Modern forum software is web-based, which means it can integrate much more
easily with other services. Links to GitHub, webhook integrations,
single-sign-on, powering comments on blog(s) (yes, you can comment on the
Bullhorn then), this list goes on. We can, for example, do things like managing
signup for events through it, or integrating meeting agendas. I'm exploring
using webhooks between Discourse and Matrix too.

Plugins are also a big feature, and can generally be enabled per-category.
Popular things I would have from the outset are mark-solution, events &
calendar, and possibly upvoting questions & translations. See
https://meta.discourse.org/c/plugin/22 for more ideas.

## Concerns on forums

I know a forum isn't everyone's favourite thing, and I anticipate some
concerns. Many are valid, and part of the trade-off that I think is worthwhile,
others I can argue against, so let's have a look.

### I like things the way they are

I can't deny that this will shake things up - I can only hope that my data and
argument have convinced you it's worth the effort, that we *have* to shake
things up.

I'm never going to tell people what tools to use (I didn't with Matrix either),
and we go to some lengths for compatibility with existing worklows (IRC bridges
last time, Discourse supporting email workflows this time). But we have to also
ask what's right for **the community as a whole**, even if that means some
changes for some of us.

### Forums are old

They've certainly been around a while, and I don't blame anyone who used a
forum 10 years ago from being scarred by the experience - I was. But spend time
on a Discourse site, and I hope you'll be surprised. It's no accident that so
many projects are using it.

### Forums are hard to maintain

Maintenance *is* a real concern, on two levels.

Firstly, the code/servers need to exist and be kept updated - but here we can
draw on the fact that the Community Team has some budget. Much the same as when
we funded the Matrix homeserver for Matrix, we can fund the forum. Paying
another open-source company for their project feels right anyway, we should
support each other.

More importantly, we'll need moderators to run it. To start with this will be
the people building it (i.e the Red Hat Ansible Community Team) by necessity,
but we will be looking to build that group of people from the community. Such
people already do good work in chat, on SO, and so on - but recognition/reward
for that effort is hard to come by, and I think this can make it easier.

### We should standardise on GitHub

This is a bit [XKCD Standards](https://xkcd.com/927/) isn't it? GitHub is not a
bad place for discussions, I agree - definitely better than a mailing list.
However, I would counter this in a few ways.

Firstly, the fragmentation is worst on GitHub (470+ repos and counting). Do we
pick a repo and bless that as *special* in some way? If we did, would it have
rich enough tooling to cope with the scale of the project? That didn't end well
last time we tried it - we had to move everything out of ansible/ansible in
2020.

We also probably don't want user support in that hypothetical special repo -
reclaiming GitHub Issues for *actual issues* and having support in a dedicated
place seems worthwile. And if a big chunk of the community is going to be where
that support happens, don't we want to make *more* use of that?

GitHub also doesn't support @-groups across orgs, so unless we want to commit
to a lot of overhead (duplicating groups), being able to involve the right
people in discussions will be *much* harder this way.

Overall, the tooling around Discourse is *much* better for discussions,
support, and groups - and it's *ours*. We can, if we need it, develop plugins
to provide additional functions - something that is never an option with an
as-a-service platform.

### It's another place to check

I can't mitigate this, it's true. However, I would expect that the *total*
amount of notification spam should go down (unless you *choose* to subscribe to
everything, of course). Discourse can be used by web, mobile, or email, and you
can set complex levels of filters to get what you need. Plus it comes from our
own domain with decent headers so you can filter that way too. Oh, and you can
set working hours so it won't spam you at bad times - handy!

### What happens to the mailing list / GitHub Discussions / other async places

Nothing, right away. I won't sugar coat this though - if the goal is to reduce
fragmentation, then they will need to be dealt with (archived & imported, which
is entirely possible with Discourse). The timeline for that can be set as we go
forwards, and each part of the community can move as fast as it is comfortable
with. However I would like to see a critical-mass of the community adopt this
fairly quickly - I'm looking for volunteers :)

### Summary

- New forum for the community
- Hosts project-wide discussion
- Hosts support questions
- Other async discussion places get migrated over time

## Now what?

That's a lot of text, so let me recap really quickly:

- The metrics are not good
- We have structural issues that are likely contributing to that
- We need to work on our fragmentation & lack of common voice
- We should do this with new website & forum

Hopefully I've convinced you that we need to own our virtual space, set up new
things in it, and get as much of the community as possible to move to it soon.
But perhaps you have questions? Of course you do, the crowd has wisdom.

Thus, accompanying these posts will be two discussion topics in GitHub (because
we don't have the forum yet!). These are:

1. [To create a new DNS & website, and a working group to build it](https://github.com/ansible-community/community-topics/issues/201)
2. [To create a forum and look for parts of the project wantng to get onboard](https://github.com/ansible-community/community-topics/issues/202)

Please do go and let me know your thoughts! I've deliberately not included
rollout plans here (rest assured, drafts exist) because this is long enough. We
can figure that out that out in our working groups once we've agreed the goals.

See you in the comments!
