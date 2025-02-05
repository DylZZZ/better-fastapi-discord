from setuptools import find_packages, setup

readme = open("README.md", "r").read()

setup(
    name="better_fastapi_discord",
    packages=find_packages(),
    version="0.2.5",
    description="Discord OAuth FastAPI extension for APIs",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="Tert0",
    license="MIT",
    install_requires=["fastapi==0.101.0", "aiohttp==3.8.5", "aiocache==0.12.2"],
    python_requires=">=3.5",
    url="https://github.com/Tert0/fastapi-discord",
)
