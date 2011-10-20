"""args.py a mieru CLI processor
- it gets the commandline arguments and decides what to do
"""
import argparse

class Startup():
  def __init__(self):
    parser = argparse.ArgumentParser(description="A flexible manga and comix reader.")
    parser.add_argument('-u', help="specify user interface type", default="pc",
                        action="store", metavar="--ui", choices=["pc","hildon", "harmattan", "QML"])
    parser.add_argument('-o', help="specify path to a manga or comic book to oopen", default=None,
                        action="store", metavar="--open",)
    self.args = parser.parse_args()

