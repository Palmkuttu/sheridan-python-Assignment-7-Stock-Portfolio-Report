from setuptools import setup

setup(
    name="portfolio-report",
    version="1.0",
    py_modules=["portfolio_report"],   
    install_requires=[
        "requests"
    ],
    entry_points={
        "console_scripts": [
            "portfolio_report=portfolio_report:main"   
        ]
    },
    author="Your Name",
    description="Stock Portfolio Performance Report Generator"
)
