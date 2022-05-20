from setuptools import setup, find_packages

setup(
    name='disk_usage',
    description='check the size (bytes) of directories and create csv file',
    packages=find_packages(),
    author='Me',
    entry_points="""
    [console_scripts]
    diskReport=disk_report
    """,
    install_requires=['pandas'],
    version='0.0.1',
   
)
