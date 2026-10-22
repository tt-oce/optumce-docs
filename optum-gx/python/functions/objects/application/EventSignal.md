# EventSignal

Signal delivering server-pushed events (listen_events server-streaming RPC).

Connect a callback to be invoked whenever the application raises one of the
event kinds this signal listens to. The callback receives the stage in
focus when the event was raised, or None when the change is global rather
than stage-related (e.g. material or report-settings edits).

## Notes

Callbacks run on a background listener thread, not on the main thread.

## Examples

```python
def on_changed(stage):
    print(f'GX changed! Stage: {stage.name}')
gx.on_changed.connect(on_changed)
```

Object without properties.

## Methods

<a id="connect"></a>
### connect()

Connect a callback to this signal.

#### Parameters

<dl>
<dt>callback : callable</dt>
<dd>Called as callback(stage) whenever the event is raised.</dd>
</dl>

<a id="disconnect"></a>
### disconnect()

Remove a previously connected callback.
