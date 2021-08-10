from setuptools import setup

setup(
    name="detecion_fraudes",
    version='0.1',
    py_modules=['cli'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        detecion_fraudes=cli:main
    ''',
)