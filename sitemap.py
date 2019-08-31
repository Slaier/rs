#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import glob
import os
import time

os.chdir("docs")

def main():
    baseurl = "https://slaier.github.io/rs/#/"
    sitemap = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
    ]

    for md in [p for p in glob.glob('**/*.md', recursive=True) if not p.startswith("_")]:
        mtime = os.stat(md).st_mtime
        lastmod = time.strftime("%Y-%m-%d", time.localtime(mtime))
        url = baseurl + md[:-3]
        sitemap.append("\t<url>")
        sitemap.append("\t\t<loc>{}</loc>".format(url))
        sitemap.append("\t\t<lastmod>{}</lastmod>".format(lastmod))
        sitemap.append("\t</url>")

    sitemap.append("</urlset>")
    with open("sitemap.xml", "w") as f:
        f.write("\n".join(sitemap))


if __name__ == '__main__':
    main()