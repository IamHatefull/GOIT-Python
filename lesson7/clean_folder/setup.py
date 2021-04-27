from setuptools import setup, find_namespace_packages

setup(
    name='clean-folder',
    version='1',
    description='Very useful code',
    author='Borysman',
    packages=find_namespace_packages(),
    install_requires=['markdown'],
    entry_points={'console_scripts': ['clean-folder = clean_folder.clean:main']}
)
