import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="focus-time",
    version="1.0.5",
    author="Philip Shamash",
    author_email="philip.shamash.17@ucl.ac.uk",
    description="Focus time is an application in python to help you focus for a set amount of time",
    license = "GNU General Public License",
    url = "https://github.com/philshams/focus-time",
    packages=["focus"],
    package_dir={'focus':'focus'},
    package_data={'focus': ['../data/*.mp3']},
    install_requires=['DateTime>=4.3',
                      'numpy>=1.20.2',
                      'playsound>=1.2.2'                
                      ],
    entry_points={
        "console_scripts": [
            "focus = focus.__session__:session",
            "focus-time = focus.__session__:session",
            "focus-session = focus.__session__:session",
            "focus-day = focus.__day__:day"
        ]
    }
)