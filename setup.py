# -*- coding: utf-8 -*-
"""Setup file for freepn-gtk3-indicator."""
import ast
import codecs

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def read_file(filename):
    """
    Read a utf8 encoded text file and return its contents.
    """
    with codecs.open(filename, 'r', 'utf8') as f:
        return f.read()

for line in read_file('freepn-gtk3-indicator').splitlines():
    if line.startswith('APP_VERSION'):
        version = ast.literal_eval(line.split('=', 1)[1].strip())
        break

# make setuptools happy with PEP 440-compliant post version
#REL_TAG = FPND_VERSION.replace('-', 'p')

APP_ID      = 'freepn-gtk3-indicator'
APP_VERSION = version

APP_DOWNLOAD_URL = (
    'https://github.com/freepn/freepn-gtk3-tray/tarball/' + APP_VERSION
)

setup(
    name=APP_ID,
    version=APP_VERSION,
    license='AGPL-3.0',
    description='Freepn tray controller for fpnd.',
    long_description=read_file('README.rst'),
    url='https://github.com/freepn/freepn-gtk3-tray',
    author='Stephen L Arnold',
    author_email='nerdboy@gentoo.org',
    download_url=APP_DOWNLOAD_URL,
    keywords=['freepn', 'vpn', 'p2p'],
    scripts=['freepn-gtk3-indicator'],
    data_files=[
        ('share/man/man1', ['data/freepn-gtk3-indicator.1']),
        ('share/applications', ['data/freepn-gtk3-indicator.desktop']),
        ('share/icons/hicolor/48x48/apps', ['icons/hicolor/48x48/freepn.png']),
        ('share/icons/hicolor/scalable/apps', ['icons/hicolor/scalable/freepn.svg']),
        ('share/icons/hicolor/symbolic/apps', ['icons/hicolor/symbolic/freepn-symbolic.svg']),
        ('share/icons/hicolor/scalable/status', ['icons/hicolor/status/network-freepn-acquiring-symbolic.svg',
                                                 'icons/hicolor/status/network-freepn-connected-key-symbolic.svg',
                                                 'icons/hicolor/status/network-freepn-connected-symbolic.svg',
                                                 'icons/hicolor/status/network-freepn-error-symbolic.svg',
                                                 'icons/hicolor/status/network-freepn-no-route-symbolic.svg',
                                                 'icons/hicolor/status/network-freepn-offline-symbolic.svg',
                                                 'icons/hicolor/status/network-freepn-offline-2-symbolic.svg']),
    ],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Desktop',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3',
        'Natural Language :: English',
        'Topic :: Internet :: Proxy Servers',
        'Topic :: Security',
        'Topic :: System :: Networking',
        'Topic :: System :: Operating System Kernels :: Linux',
    ],
    install_requires=[
        'pycairo',
        'pygobject',
        'xmltodict',
    ],
)
