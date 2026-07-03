from pathlib import Path
import runpy


APP_FILE = Path(__file__).with_name("Biohacker_Habit_&_Sleep.py")
runpy.run_path(str(APP_FILE), run_name="__main__")
