from setuptools import setup, find_packages

setup(
    name='PyEqCloud',
    version='0.1.1',
    description='Gather Data via a REST-Connection from the Kontron AIS GmbH EquipmentCloud',
    author='Patrick Thiem',
    author_email='Patrick.Thiem@kontron-ais.com',
    py_modules=["PyEqCloud"],
    package_dir={'': 'PyEqCloud'},
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',],
    keywords='equipment cloud',
    packages=find_packages(exclude=['docs','tests*']),
    install_requires=[
        'requests>=2.22.0,<2.23.0',
        'pandas>=0.25.3,<1.0.3',
        'tqdm>=4.39.0,<4.46.0',
        ],
    data_files=None,
    python_requires='>=3.6',
)