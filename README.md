### Info
This is a repository I made for myself so I could save all native Win32 API functions in one place. 
The table includes the name of the function, and the link for documentation.
```tool.py``` parses exports from the ```dumpbin``` command into a markdown file.

### Running the tool
You can run ```tool.py``` with the command line. ```tool.py``` takes 3 arguments:
1. [in]            File to read from and parse
2. [in]            File to write all parsed output
3. [in] [optional] The name of the dll these functions are exported from.

An example:
```py tool.py ntexports.txt nt.md ntdll.dll```

Made this script in like 30 minutes, don't expect production quality. Wasn't even gonna post the script.