# Input files for FRESCO CRC-DWBA Calculations

## To Do
Make a python program to clean all the fort files

## 
```
Get-Content 19F_dd.fin | fresco | Out-File -FilePath 19F_dd.fro
fresco  <  <filename>.fri  >  <filename>.fro
```