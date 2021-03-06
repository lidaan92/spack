# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Xvinfo(AutotoolsPackage):
    """xvinfo prints out the capabilities of any video adaptors associated
    with the display that are accessible through the X-Video extension."""

    homepage = "http://cgit.freedesktop.org/xorg/app/xvinfo"
    url      = "https://www.x.org/archive/individual/app/xvinfo-1.1.3.tar.gz"

    version('1.1.3', '6890a19226c07344ae12e7a2ef12f2c6')

    depends_on('libxv')
    depends_on('libx11')

    depends_on('xproto@7.0.25:', type='build')
    depends_on('pkgconfig', type='build')
    depends_on('util-macros', type='build')
