# run_analysis_async

Start the analysis without blocking and return a progress handle.

Unlike run_analysis (which blocks until the analysis finishes),
this returns immediately so the run log and solver output can be
polled while the analysis is in progress. The returned object is a
context manager exposing is_running, read_log() and read_solver().

Returns
-------
AnalysisProgress
    Live progress handle for the running analysis.

## See also

- [run_analysis](/python/functions/project/run_analysis)

## Examples

```python
import time
with prj.run_analysis_async() as progress:
...     while progress.is_running:
...         log = progress.read_log()        # run log since last call
...         if log:
...             print(log, end='')
...         solver = progress.read_solver()  # solver output since last call
...         if solver:
...             print(solver, end='')
...         time.sleep(1)                    # throttle polling
```
