from setuptools import setup, find_packages

setup(
    name="spycam",
    version="0.1.0",
    description="CV Project",
    author="Mike",
    author_email="mwstuck99@gmail.com",
    packages=find_packages(),
    install_requires=[
        # Add your dependencies here, e.g.:
        # "opencv-python",
    ],
    python_requires=">=3.7",
    entry_points={
        "console_scripts": [
            # Example: "spycam=spycam.cli:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
)