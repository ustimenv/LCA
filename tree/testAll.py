import glob
from subprocess import call


if __name__ == "__main__":
    for testScriptName in glob.glob('**Test.py', recursive=False):
        call(["python", testScriptName])
