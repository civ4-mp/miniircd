from setuptools import setup

setup(
    name="miniircd",
    python_requires=">=3.5",
    scripts=["miniircd"],
    install_requires=["prometheus_client"],
)
