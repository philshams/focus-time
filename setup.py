import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="focus-time",
    version="1.2.0",
    author="Philip Shamash",
    author_email="philip.shamash.17@ucl.ac.uk",
    description="Focus time is an Python application that can help you focus for a set amount of time",
    license = "GNU General Public License",
    url = "https://github.com/philshams/focus-time",
    packages=["focus"],
    package_dir={'focus':'focus'},
    package_data={'focus': ['../data/*.mp3']},
    install_requires=['DateTime>=4.3',
                      'numpy>=1.19',
                      'playsound>=1.2.2'                
                      ],
    entry_points={
        "console_scripts": [
            "focus = focus.terminal_commands:run_focus_session",
            "focus-time = focus.terminal_commands:run_focus_session",
            "focus-session = focus.terminal_commands:run_focus_session",
            "focus-day = focus.terminal_commands:run_focus_day"
        ]
    }
)