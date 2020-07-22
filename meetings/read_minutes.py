#!/usr/bin/env python3
import argparse

import requests


TEMPLATE = """
{date}
==========
{content}

Logs
----

{logs}
"""

LOG_MAP = [
    ("Minutes:", "html"),
    ("Minutes (text):", "txt"),
    ("Log:", "log.html"),
]


def read(url):
    date = url.split("/")[-2]
    minutes = requests.get(url).text
    sections = minutes.split("\n\n\n\n")

    topics = format_topics(sections[1])
    actions = format_actions(sections[2])

    content = topics
    if actions:
        content += f"\n\n{actions}"

    logs = []
    for prefix, extension in LOG_MAP:
        mangled_url = url.rsplit(".", 1)[0]
        logs.append(f"{prefix} {mangled_url}.{extension}")

    print(TEMPLATE.format(date=date, content=content, logs="\n".join(logs)))


def format_topics(summary):
    topics = []
    for line in summary.split("\n"):
        if not line.strip():
            continue

        if line[0] == "*":
            topics.append((clean_line(line), []))
        elif line.startswith("  *"):
            topics[-1][1].append(line)
        elif line.startswith("   "):
            topics[-1][1][-1] += f" {line.strip()}"

    topics_text = []
    for topic_name, items in topics:
        items = [clean_line(item) for item in items]
        if not any(items):
            continue

        topics_text.extend(["", topic_name, '-' * len(topic_name), ""])
        for item in items:
            if item:
                topics_text.append(f"* {item}")

    return "\n".join(topics_text)


def format_actions(action_items):
    actions = []
    last_action = None
    for line in action_items.split("\n"):
        if line.startswith("* "):
            assignee, action = line[2:].split(" ", 1)
            last_action = len(actions)
            actions.append(f"- [ ] @{assignee} {action}")
        elif line.startswith("  ") and last_action is not None:
            actions[last_action] += f" {line[2:]}"
        else:
            last_action = None

    if any(actions):
        actions = ["Actions", "-------", ""] + actions

    return "\n".join(actions)


def clean_line(line):
    trimmed = line.strip()[2:]
    if trimmed.startswith("ACTION:"):
        # Actions get handled later
        return ""

    trimmed = trimmed.replace("AGREED:", ":+1:")
    trimmed = trimmed.replace("IDEA:", "💡")
    trimmed = trimmed.replace("LINK:", "")
    return trimmed.rsplit(" (", 1)[0].strip()


def txt_url(string):
    if string[-4:] != ".txt":
        raise argparse.ArgumentTypeError("URL must end in `.txt`")
    return string


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fetches MeetBot minutes and generates a Markdown summary for adding to GitHub")
    parser.add_argument("url", type=txt_url, help="URL to 'Minutes (text)' log. Must end with `.txt`")
    args = parser.parse_args()

    read(args.url)
