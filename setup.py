from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().split()

with open('requirements-tests.txt') as f:
    test_requirements = f.read().split()

setup(
    name='pywally',
    packages=find_packages(
        exclude=['tests'],
    ),
    install_requires=requirements,
    tests_require=test_requirements,
    entry_points={},
    include_package_data=True,
    message_extractors={
        '.': [('**.py', 'python', None)],
    },
)
