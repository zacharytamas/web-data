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
  if file_type == "post":
    directory_name = "%04d-%02d-%02d-%s" % (
      today.year, today.month, today.day, slug
    )
    os.makedirs("posts/" + directory_name)
    file_name = "%s.md" % slug
    path = "posts/%s/%s" % (directory_name, file_name)
  elif file_type == "book":
    file_name = "%04d-%02d-%02d-%s" % (today.year, today.month, today.day, slug)
    path = "books/" + file_name + ".json"

  with open(path, "w") as f:
    f.write(content)
    return path


def _openInAtom(path):
  call(["atom", path])


def new(file_type):
  if file_type == "post":
    print
    print "So you'd like to start a new post, eh?"
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
  elif file_type == "book":
    print
    print "So you read a new book?"
    print

    title = raw_input("Book title: ")
    tentative_slug = title.lower().replace(" ", "-")
    slug = raw_input(" Book slug: [%s] " % tentative_slug)
    author = raw_input("Author: ")
    category = raw_input("Category: ")
    comments = raw_input("Comments: ")

    if slug == "":
      slug = tentative_slug

    template = _getTemplate("book.json")
    body = (template.replace("$TITLE", title)
                    .replace("$AUTHOR", author)
                    .replace("$CATEGORY", category)
                    .replace("$COMMENTS", comments))
    path = _createFile("book", slug, body)
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
