# get_model

Get model or models by name.

## Parameters

<dl>
<dt>name : str</dt>
</dl>

## Examples

```python
prj.create_model('Model 1') #create model
prj.create_model('Model 2') #create another model
m = model2d.get_model('Model 1') #get 'Model 1'
m = model2d.get_model(['Model 1', 'Model 2']) #get 'Model 1' and 'Model 2'
```

