# ShapeList

An ordered collection of Shape objects from a single stage.

Returned by selection and query methods. The scalar properties (id, type,
length, area, volume, location) return the value of the single contained
shape when the list holds exactly one shape, and None otherwise. Supports
indexing, len(), merge() and remove(); the raw list is available via values.

## Properties

<dl>
<dt>values : list[Shape]</dt>
<dd>The underlying list of Shape objects.</dd>
<dt>id : int</dt>
<dd>Id of the single contained shape, or None if not exactly one shape.</dd>
<dt>type : ShapeType</dt>
<dd>Type of the single contained shape, or None if not exactly one shape.</dd>
<dt>length : float</dt>
<dd>Length of the single contained shape, or None if not exactly one shape.</dd>
<dt>area : float</dt>
<dd>Area of the single contained shape, or None if not exactly one shape.</dd>
<dt>volume : float</dt>
<dd>Volume of the single contained shape, or None if not exactly one shape.</dd>
<dt>location : list[float]</dt>
<dd>Location of the single contained shape, or None if not exactly one shape.</dd>
<dt>settings_3d : ExtrudeTo3dSettings or None</dt>
<dd>Remote 2D-to-3D extrusion feature for these shapes, whose properties can be read and written directly; None if not applicable.</dd>
</dl>

## Methods

### vertices()

List of all the vertices bounding the shape. Designed for a single Shape in the shapelist.

#### Returns

<dl>
<dt>ShapeList</dt>
<dd>List of vertices</dd>
</dl>

#### Examples

```python
shapes = model.get_shapes()
shapes[26].vertices()
```

### edges()

List of all the edges bounding the shape. Designed for a single Shape in the shapelist.

#### Returns

<dl>
<dt>ShapeList</dt>
<dd>List of edges</dd>
</dl>

#### Examples

```python
shapes = model.get_shapes()
shapes[26].edges()
```

### faces()

List of all the faces bounding the shape. Designed for a single Shape in the shapelist.

#### Returns

<dl>
<dt>ShapeList</dt>
<dd>List of faces</dd>
</dl>

#### Examples

```python
shapes = model.get_shapes()
shapes[26].faces()
```

### volumes()

List with the volume shape. Designed for a single Shape in the shapelist.

#### Returns

<dl>
<dt>ShapeList</dt>
<dd>List with volume</dd>
</dl>

#### Examples

```python
shapes = model.get_shapes()
shapes[26].volumes()
```

### set_2d_to_3d_settings()

Set 2D to 3D extrusion settings for shapes.

#### Parameters

<dl>
<dt>depth_in : float, optional</dt>
<dd>Extrusion depth inward</dd>
<dt>depth_out : float, optional</dt>
<dd>Extrusion depth outward</dd>
<dt>repetition : bool, optional</dt>
<dd>Enable repetition</dd>
<dt>repetition_spacing : float, optional</dt>
<dd>Spacing between repetitions</dd>
<dt>repetition_out : float, optional</dt>
<dd>Number of repetitions outward</dd>
<dt>repetition_in : float, optional</dt>
<dd>Number of repetitions inward</dd>
<dt>fill : bool, optional</dt>
<dd>Fill between repetitions</dd>
<dt>fill_in : float, optional</dt>
<dd>Fill depth inward</dd>
<dt>fill_out : float, optional</dt>
<dd>Fill depth outward</dd>
<dt>as_face : bool, optional</dt>
<dd>Treat as face</dd>
</dl>

#### Returns

<dl>
<dt>bool</dt>
<dd>True if settings were applied successfully</dd>
</dl>

### get_2d_to_3d_settings()

Get 2D to 3D extrusion settings for the first shape in the list.

#### Returns

<dl>
<dt>dict</dt>
<dd>Dictionary containing extrusion settings: - depth_in: Extrusion depth inward - depth_out: Extrusion depth outward - repetition: Whether repetition is enabled - repetition_spacing: Spacing between repetitions - repetition_out: Number of repetitions outward - repetition_in: Number of repetitions inward - fill: Whether fill is enabled - fill_in: Fill depth inward - fill_out: Fill depth outward - as_face: Whether to treat as face</dd>
</dl>

### contains()

Check if Shape is contained in ShapeList.

#### Returns

<dl>
<dt>bool</dt>
<dd>True or False</dd>
</dl>

#### Examples

```python
shapes = model.get_shapes()
shape = model.get_shape_by_id(26)
shapes.contains(shape)
```

### find()

Find Shape contained in ShapeList.

#### Parameters

<dl>
<dt>items : Shape</dt>
<dd>shape</dd>
</dl>

#### Returns

<dl>
<dt>Shape or None.</dt>
</dl>

#### Examples

```python
shapes = model.get_shapes()
shape = model.get_shape_by_id(26)
shapes.contains(shape)
```

### remove()

Remove Shape from ShapeList.

#### Parameters

<dl>
<dt>items : Shape or ShapeList</dt>
<dd>shape or shapes.</dd>
</dl>

#### Examples

```python
shapes = model.get_shapes()
shape = model.get_shape_by_id(26)
shapes.remove(shape)
shapes.remove(model.get_shapes(['vertex']))
```

### get()

Get new Shapelist from index in Shapelist

#### Parameters

<dl>
<dt>index : int</dt>
<dd>index of shape to get new shapelist from.</dd>
</dl>

#### Returns

<dl>
<dt>ShapeList.</dt>
</dl>

#### Examples

```python
shapes = model.get_shapes()
shapes.get(10)
```

### merge()

'
Merge current ShapeList with another.

#### Parameters

<dl>
<dt>other : ShapeList</dt>
<dd>ShapeList to merge with.</dd>
</dl>

#### Returns

<dl>
<dt>ShapeList.</dt>
</dl>

#### Examples

```python
vertexList = model.get_shapes(types=['vertex'])
edgeList = model.get_shapes(types=['edge'])
vertexList.merge(edgeList)
```
