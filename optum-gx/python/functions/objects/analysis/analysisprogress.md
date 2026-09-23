# AnalysisProgress

Live progress handle for an asynchronous analysis run.

Returned by Project.run_analysis_async. Use it as a context manager and
poll is_running while reading incremental output with read_log(),
read_solver() and read_message(). Each read returns only the text
produced since the previous read of the same stream.

## Examples

```python
import time
with prj.run_analysis_async() as progress:
    while progress.is_running:
        print(progress.read_log(), end='')
        print(progress.read_solver(), end='')
        time.sleep(1)
```

## See also

- [run_analysis_async](/python/functions/project/analysis/run_analysis_async)

## Properties

<dl>
<dt>is_running : bool</dt>
<dd>True while the analysis is still running, False once it completes or aborts.</dd>
</dl>

## Methods

### read_log()

Return the run-log text accumulated since the previous read_log() call.

### read_solver()

Return the solver-output text accumulated since the previous read_solver() call.

### read_message()

Return the messages (warnings/errors) accumulated since the previous read_message() call.
