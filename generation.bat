for /l %%x in (10, 1, 12) do (
   MKDIR day%%x
   echo. 2>day%%x/day%%x.py
   echo. 2>day%%x/input.txt
   echo. 2>day%%x/test.txt
)
Pause