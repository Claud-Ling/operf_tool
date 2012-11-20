import distribute_setup
distribute_setup.use_setuptools()

from setuptools import setup, find_packages

setup(
    name = 'operf_tool',
    version = '0.1',
    packages = find_packages(),

    # metadata for upload to PyPI
    author = 'Austin Bingham',
    author_email = 'austin.bingham@gmail.com',
    description = 'Tool for analyzing operf output.',
    license = 'MIT',
    keywords = 'profiling',
    url = 'http://github.com/abingham/operf_tool',
    # downloadurl = 'http://pypi.python.org/pypi/eagertools',
    # long_description
    # zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Profiling'
        ],
    platforms='any',
    include_package_data=True,

    entry_points = {
        'console_scripts': [
            'operf_tool = operf_tool.app:main',
            ],
        },

    install_requires=[
        'baker',
    ],
)
