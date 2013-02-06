#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

shelltools.export("JOBS", get.makeJOBS().replace("-j", ""))

def setup():
    shelltools.system("./waf configure \
                       --prefix=/usr \
                       --enable-nls \
                       --update-po \
                       --enable-docs \
                       --enable-apidocs  \
                       --enable-unique \
                       --enable-libnotify \
                       --enable-addons \
                       --disable-hildon")

def build():
    shelltools.system("./waf build --want-rpath=0")

def install():
    shelltools.system("./waf install --destdir=%s" % get.installDIR())
    pisitools.removeDir("/usr/share/gir-1.0")

