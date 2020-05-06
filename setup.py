from setuptools import setup, find_packages

setup(
    name='PyEqCloud',
    version='0.1.0',
    description='Gather Data via a REST-Connection from the Kontron AIS GmbH EquipmentCloud',
    author='Patrick Thiem',
    author_email='Patrick.Thiem@kontron-ais.com'
    py_modules=["PyEqCloud"],
    package_dir={'': 'PyEqCloud'},
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Data Scientists, Developers',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    keywords='equipment cloud',
    packages=find_packages(exclude=['docs','tests*']),
    install_requires=['requests','pandas','getpass','tqdm'],
    data_files=None
)