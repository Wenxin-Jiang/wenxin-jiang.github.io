#!/usr/bin/env python3
# Publications markdown generator for academicpages
# Data format: JSON, see publications.json for examples
# Caution: Overwrites ../auto-publications.md

import json
import sys

PUBFILE = sys.argv[1]
print("Pubfile: " + PUBFILE)

JOURNAL_PUB = "journal"
CONFERENCE_PUB = "conference"
WORKSHOP_PUB = "workshop"
ARXIV_PUB = "arxiv"
DISSERTATION_PUB = "dissertation"
PATENT_PUB = "patent"
POSTER_PUB = "poster"

def writeOutPrefix(handle):
    handle.write("""---
layout: single
title: "Publications"
permalink: /publications/
author_profile: true
---

Here are the publications to which I have contributed.
To see them organized by project, see [here](/research).
""")

FILE_PATH = "{{ site.url }}/{{ site.baseurl }}/{{ site.filesurl }}/publications"

def makeLink(url):
    if 'http' in url:
        return url 
    else:
        return "{}/{}".format(FILE_PATH, url)

def pub2md(pub):
    links = []
    if 'paperBasename' in pub and pub['paperBasename']:
        links.append('<a href="{}"><i class="fas fa-file-pdf"></i></a>'.format(
            makeLink(pub['paperBasename'])
        ))
    if 'slidesBasename' in pub and pub['slidesBasename']:
        links.append('<a href="{}"><i class="fas fa-file-powerpoint"></i></a>'.format(
            makeLink(pub['slidesBasename'])
        ))
    if 'artifactURL' in pub and pub['artifactURL']:
        links.append('<a href="{}"><i class="fas fa-file-code"></i></a>'.format(
            makeLink(pub['artifactURL'])
        ))
    if 'videoURL' in pub and pub['videoURL']:
        links.append('<a href="{}"><i class="fas fa-video"></i></a>'.format(
            makeLink(pub['videoURL'])
        ))
    if 'blogURL' in pub and pub['blogURL']:
        links.append('<a href="{}"><i class="fab fa-medium"></i></a>'.format(
            makeLink(pub['blogURL'])
        ))
    if 'bestPaperAward' in pub and pub['bestPaperAward']:
        links.append('[Best Paper Award](){: .btn}')
    
    if len(pub['authors']) == 1:
        authList = pub['authors'][0]
    elif len(pub['authors']) == 2:
        authList = ' and '.join(pub['authors'])
    else:
        authList = ', '.join(pub['authors'][:-1])
        authList += ", and " + pub['authors'][-1]

    cite = "*{}*.  \n {}.  \n {} {}.  ".format(
        pub['title'],
        authList,
        pub['venue'], pub['year'],
    )
    return cite + "\n " + ' '.join(links)

def writePubs(handle, headingTitle, pubs):
    handle.write('\n## {}\n\n'.format(headingTitle))
    for i, pub in enumerate(pubs):
        handle.write("{}. {}\n".format(i+1, pub2md(pub)))

with open(PUBFILE, 'r') as infile, open('../auto-publications.md', 'w') as outfile:
    writeOutPrefix(outfile)
    pubs = json.load(infile)['publications']
    pubs = sorted(pubs, key=lambda p: p['year'], reverse=True)

    confPubs = [ pub for pub in pubs if pub['type'] == CONFERENCE_PUB ]
    journalPubs = [ pub for pub in pubs if pub['type'] == JOURNAL_PUB ]
    workshopPubs = [ pub for pub in pubs if pub['type'] == WORKSHOP_PUB ]
    arxivPubs = [ pub for pub in pubs if pub['type'] == ARXIV_PUB ]
    patentPubs = [ pub for pub in pubs if pub['type'] == PATENT_PUB ]
    posterPubs = [ pub for pub in pubs if pub['type'] == POSTER_PUB ]
    dissertationPubs = [ pub for pub in pubs if pub['type'] == DISSERTATION_PUB ]

    if confPubs:
        print("Writing the {} conference pubs".format(len(confPubs)))
        writePubs(outfile, "Peer-reviewed conference papers (full and short)", confPubs)
    if journalPubs:
        print("Writing the {} journal pubs".format(len(journalPubs)))
        writePubs(outfile, "Peer-reviewed journal papers", journalPubs)
    if workshopPubs:
        print("Writing the {} workshop pubs".format(len(workshopPubs)))
        writePubs(outfile, "Peer-reviewed workshop papers", workshopPubs)
    if arxivPubs:
        print("Writing the {} arxiv pubs".format(len(arxivPubs)))
        writePubs(outfile, "arXiv papers", arxivPubs)
    if patentPubs:
        print("Writing the {} patents".format(len(patentPubs)))
        writePubs(outfile, "US Patents", patentPubs)
    if posterPubs:
        print("Writing the {} posters".format(len(posterPubs)))
        writePubs(outfile, "Posters", posterPubs)
    if dissertationPubs:
        print("Writing the {} dissertations".format(len(dissertationPubs)))
        writePubs(outfile, "Dissertation", dissertationPubs)
    outfile.write('\n')