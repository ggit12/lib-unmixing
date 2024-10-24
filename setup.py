from setuptools import setup, find_packages

setup(
    name='lib_unmixing',
    version='0.1',
    packages=find_packages(),
    description='lib_unmixing, made into a pip-installable package, forked from https://github.com/etienne-monier/lib-unmixing',
    author='ggit12',
    # author_email='your.email@example.com',
    license='BSD-3-Clause',
    install_requires=[
        # list of packages this package depends on
        'numpy==1.26.4',
        'scipy==1.14.1',
        'matplotlib==3.9.2'
    ],
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.org/classifiers/
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
    ],
)