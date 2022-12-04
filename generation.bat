for /l %%x in (6, 1, 25) do (
   MKDIR day%%x
   CD day%%x
   echo. 2>day%%x.py
   echo. 2>input.txt
   echo. 2>test.txt
   CD ..
)