from setuptools import setup

setup(
    name="my_project",
    version="0.1.0",
    packages=["App"],
    entry_points={
        "console_scripts": [
            "my_app = App.__main__:main"
        ]
    }
)