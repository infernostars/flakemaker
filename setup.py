from distutils.core import setup

setup(
    name='flakemaker',
    packages=['flakemaker'],
    version='0.0.1',
    license='MIT',
    description='Create snowflakes with encoded data in them.',
    author='infernostars',  # Type in your name
    author_email='infernity@infernity.dev',
    url='https://github.com/infernostars/flakemaker',
    download_url='https://github.com/infernostars/flakemaker/archive/-.tar.gz',  # change this on update
    keywords=['SNOWFLAKE', 'ID'],
    install_requires=[],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
)
