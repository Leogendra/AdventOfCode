@ génère les fichiers du jour 1 au jour 25
for /l %%x in (1, 1, 25) do (
   MKDIR day%%x
   echo. 2>day%%x/day%%x.py
   echo. 2>day%%x/input.txt
   echo. 2>day%%x/test.txt
)
Pause