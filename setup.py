import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="focus-time",
    version="1.0.0",
    author="Philip Shamash",
    author_email="philip.shamash.17@ucl.ac.uk",
    description="A small example package",
    packages=["focus"],
    install_requires=['DateTime>=4.3',
                      'numpy>=1.20.2',
                      'playsound>=1.2.2'                
                      ],
    entry_points={
        "console_scripts": [
            "focus = focus.__main__:main"
        ]
    }
)