# -*- Mode: Python -*-
"""crypto_two1

This tool uses the official PyPa packaging and click recommendations:
https://github.com/pypa/sampleproject
https://packaging.python.org/en/latest/distributing.html
http://click.pocoo.org/4/setuptools/
"""
from setuptools import setup

f = open('./requirements.txt')
install_requires = f.read().split('\n')
f.close()
version = __import__('crypto_two1').TWO1_VERSION

setup(
    name='crypto_crypto_two1',
    version=version,
    description='Buy and sell anything on the internet with bitcoin.',
    author='Lts',
    author_email='nail.velichko2016@yandex.ru',
    license='FreeBSD',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Internet',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.10',
    ],
    keywords='bitcoin blockchain client server',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=['crypto_two1',
              'crypto_two1.mkt',
              'crypto_two1.sell',
              'crypto_two1.sell.util',
              'crypto_two1.sell.exceptions',
              'crypto_two1.lib',
              'crypto_two1.commands',
              'crypto_two1.bitcoin',
              'crypto_two1.server',
              'crypto_two1.bitserv',
              'crypto_two1.wallet',
              'crypto_two1.crypto',
              'crypto_two1.channels',
              'crypto_two1.bitserv.django',
              'crypto_two1.bitserv.flask',
              'crypto_two1.blockchain',
              'crypto_two1.bitrequests',
              'crypto_two1.commands.util',
              ],

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=install_requires,

    ext_modules=[],

    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev,test]
    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },

    # If there are data files included in your packages that need to be
    # installed, specify them here.  If using Python 2.6 or less, then these
    # have to be included in MANIFEST.in as well.
    package_data={
        'crypto_two1': ['crypto_two1-config.json',
                 'sell/util/scripts/ps_zerotier.sh',
                 'sell/util/scripts/zerotier_installer.sh',
                 'sell/blueprints/base/Dockerfile',
                 'sell/blueprints/router/Dockerfile',
                 'sell/blueprints/router/files/nginx.conf',
                 'sell/blueprints/payments/Dockerfile',
                 'sell/blueprints/payments/requirements.txt',
                 'sell/blueprints/payments/login.py',
                 'sell/blueprints/payments/server.py',
                 'sell/blueprints/services/ping/Dockerfile',
                 'sell/blueprints/services/ping/ping21.py',
                 'sell/blueprints/services/ping/requirements.txt',
                 'sell/blueprints/services/ping/server.py',
                 'sell/blueprints/services/ping/manifest.yaml',
                 'sell/blueprints/services/ping/login.py',
                 'sell/util/schema.sql']
    },

    # Although 'package_data' is the preferred approach, in some case you may
    # need to place data files outside of your packages. See:
    # http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files # noqa
    # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
    # data_files=[('peers', ['data/default-peers.json'])],

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    # See: http://stackoverflow.com/a/782984/72994
    # http://click.pocoo.org/4/setuptools/
    entry_points={
        'console_scripts': [
            'crypto_two1=crypto_two1.cli:main',
            'wallet=crypto_two1.wallet.cli:main',
            '21=crypto_two1.cli:main',
            'twentyone=crypto_two1.cli:main',
            'channels=crypto_two1.channels.cli:main',
        ],
    },
)
