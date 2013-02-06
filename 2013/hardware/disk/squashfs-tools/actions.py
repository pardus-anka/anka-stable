#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

#WorkDir = "%s_%s" % (get.srcNAME(), get.srcVERSION())

def build():
    shelltools.cd("squashfs-tools")
    autotools.make('RPM_OPT_FLAGS="%s"' % get.CFLAGS())

def install():
    shelltools.cd("squashfs-tools")
    autotools.install("INSTALL_DIR='%s/usr/sbin'" % get.installDIR())
