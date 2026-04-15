# Run OptumGX from Python

This article outlines a helper function that checks if an instance of OptumGX is running. If not, the application is started. 
The input parameters are set to the default, but may need to be altered to match the current machine.

```python 
import socket
import subprocess
import time as pytime
from pathlib import Path

import grpc
from OptumGX import *

def startGX(
    exe_path=r"C:\Program Files\OPTUM CE\OPTUM GX\OptumGX.exe",
    api_host="127.0.0.1",
    api_port=6000,
    startup_timeout=30,
    stable_seconds=5,
):
    """
    Start Optum GX if needed and wait until its API is stable.
    Import it into other scripts before calling the application ( GX() ).
    """
    exe_path = Path(exe_path)

    def is_optumgx_running():
        result = subprocess.run(
            [
                "powershell.exe",
                "-NoProfile",
                "-Command",
                "Get-Process -Name 'OptumGX' -ErrorAction SilentlyContinue | "
                "Select-Object -First 1 -ExpandProperty ProcessName",
            ],
            capture_output=True,
            text=True,
            check=False,
        )
        return result.stdout.strip() == "OptumGX"

    def is_gx_api_ready():
        try:
            with socket.create_connection((api_host, api_port), timeout=1):
                return True
        except OSError:
            return False

    if not exe_path.exists():
        raise FileNotFoundError(f"Optum GX executable not found: {exe_path}")

    if not is_optumgx_running():
        subprocess.Popen([str(exe_path)])

    deadline = pytime.time() + startup_timeout
    stable_since = None

    while pytime.time() < deadline:
        if is_optumgx_running() and is_gx_api_ready():
            if stable_since is None:
                stable_since = pytime.time()
            elif pytime.time() - stable_since >= stable_seconds:
                return
        else:
            stable_since = None

        pytime.sleep(1)

    raise TimeoutError(
        f"Optum GX did not make its API available on {api_host}:{api_port} "
        f"for {stable_seconds} stable seconds within {startup_timeout} seconds."
    )

```

This script can then be saved in you Python scripting folder and be imported and called in other scripts.

```python
# OptumGX module
from OptumGX import *

from startGX import startGX # Importing the startGX function from startGX.py
startGX()                   # Checking if GX is running, if not it is started

# Application
gx = GX()
```
