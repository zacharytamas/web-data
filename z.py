#!/usr/bin/env python

import optparse
from datetime import date
import os
from subprocess import call


def _getTemplate(file_name):
  with open("_templates/" + file_name, "r") as f:
    return f.read()


def _createFile(file_type, slug, content):
  today = date.today()
  directory_name = "%04d-%02d-%02d-%s" % (
    today.year, today.month, today.day, slug
  )
  os.makedirs("posts/" + directory_name)
  file_name = "%s.md" % slug
  path = "posts/%s/%s" % (directory_name, file_name)

  with open(path, "w") as f:
    f.write(content)
    return path


def _openInAtom(path):
  call(["atom", path])


def new(file_type):
  if file_type == "post":
    print
    print "So you'd like to start a new post, eh?"
    print "We'll start with a draft you can publish later using z.py publish."
    print

    title = raw_input("Post title: ")
    tentative_slug = title.lower().replace(" ", "-")
    slug = raw_input(" Post slug: [%s] " % tentative_slug)

    if slug == "":
      slug = tentative_slug

    template = _getTemplate("post.md")
    body = template.replace("$POST_TITLE", title).replace("$POST_SLUG", slug)

    path = _createFile("post", slug, body)
    _openInAtom(path)
  else:
    print "Unknown type to create. :("


def main():
  p = optparse.OptionParser()
  # p.add_option('--person', '-p', default="world")
  options, arguments = p.parse_args()

  if len(arguments):
    if arguments[0] == "new":
      new(arguments[1])


if __name__ == '__main__':
  main()
