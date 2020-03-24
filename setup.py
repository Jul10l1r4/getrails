import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='getrails',
    version=2.7,
    author="Julio Lira",
    author_email="jul10l1r4@disroot.org",
    description="Tool of OSINT and Dork hacking that work with Google and Duckduckgo",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Jul10l1r4/getrails",
    packages=["getrails", "getrails.google", "getrails.duckduckgo", "getrails.torch"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
        ],
    )
