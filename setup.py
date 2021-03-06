from setuptools import setup, find_packages


setup(
    name="planetary-health-diet-backend",
    version="0.1.0",
    description=("Backend controlling cloud resources for user, ingredients, recipes, and meals"),
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords="planetary-health-diet-backend",
    author="Jon Robison",
    author_email="narfman0@gmail.com",
    license="LICENSE",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=True,
    install_requires=[],
    test_suite="tests",
)
