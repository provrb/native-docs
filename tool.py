# Get the documentation from https://ntdoc.m417z.com/
# Arrange the function name, oridinal, dll it was from, definition in an md file

import requests
import sys

outputPath      = ""                         # file to write all data to
inputPath       = ""                         # file to take input from. search for these function names
definition_site = "https://ntdoc.m417z.com/" # site to search for function definitions
dllExportedFrom = "exported"                 # default name

def find():
  funcNum: int = 0
  with open(inputPath) as inputFile, open(outputPath, 'w') as outputFile:
    outputFile.write(f"## Exports for {dllExportedFrom}\n\n")
    outputFile.write("| DLL        | NUM  | RVA      | NAME                                                       |\n")
    outputFile.write("|------------|------|----------|------------------------------------------------------------|\n")  
    for lineNum, line in enumerate(inputFile, 1): 
      # data to parse starts on line 14
      if lineNum < 17:
        continue

      stripped = line.rstrip("\n")
      funcName = stripped[26:]
      link     = definition_site + funcName.lower()
      rva      = stripped[17: 25]

      response = requests.get(link)

      if response.status_code == 200:
        outputFile.write(f"| {dllExportedFrom}: | {funcNum:<4} | {rva} | [{funcName}]({link}) | \n")
        outputFile.flush()
        funcNum+=1

if __name__ == "__main__":
  try:
    inputPath = sys.argv[1]
  except IndexError:
    raise SystemExit("Error. You must specify an input file.")

  try:
    outputPath = sys.argv[2]
  except IndexError:
    raise SystemExit("Error. You must specify an output file.")
  
  try: 
    dllExportedFrom = sys.argv[3]
  except IndexError:
    pass

  print(f"Parsing and processing exported from {dllExportedFrom} ({inputPath}) -> {outputPath}")
  find()
  print(f"Completed. Results for all valid native exported functions in {outputPath}")
