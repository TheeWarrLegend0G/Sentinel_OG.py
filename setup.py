from setuptools import setup, find_packages

setup(
    name="sentinel_og",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "openai",
        "python-dotenv",
    ],
    entry_points={
        "console_scripts": [
            "sentinel-og=sentinel_og.main:main",
        ],
    },
)