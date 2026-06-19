# Shape

A single geometric entity (vertex, edge, face or volume) within a model.

Returned by selection and query methods such as select, get_shape_by_id
and get_shapes. Which numeric properties are populated depends on the shape
type (length for edges, area for faces, volume for volumes).

## Properties

<dl>
<dt>id : int</dt>
<dd>Unique identifier of the shape within its stage.</dd>
<dt>type : ShapeType</dt>
<dd>Geometry kind of the shape: vertex, edge, face or volume.</dd>
<dt>length : float</dt>
<dd>Length of the shape; populated for edges, otherwise None.</dd>
<dt>area : float</dt>
<dd>Surface area of the shape; populated for faces, otherwise None.</dd>
<dt>volume : float</dt>
<dd>Volume of the shape; populated for volumes, otherwise None.</dd>
<dt>location : list[float]</dt>
<dd>Representative coordinates of the shape when available, otherwise None.</dd>
</dl>

## Methods

### vertices()

*No docstring yet — add one in source to populate this section.*

### edges()

*No docstring yet — add one in source to populate this section.*

### faces()

*No docstring yet — add one in source to populate this section.*

### volumes()

*No docstring yet — add one in source to populate this section.*

### set_2d_to_3d_settings()

Set 2D to 3D extrusion settings for this shape.

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

Get 2D to 3D extrusion settings for this shape.

#### Returns

<dl>
<dt>dict</dt>
<dd>Dictionary containing extrusion settings: - depth_in: Extrusion depth inward - depth_out: Extrusion depth outward - repetition: Whether repetition is enabled - repetition_spacing: Spacing between repetitions - repetition_out: Number of repetitions outward - repetition_in: Number of repetitions inward - fill: Whether fill is enabled - fill_in: Fill depth inward - fill_out: Fill depth outward - as_face: Whether to treat as face</dd>
</dl>
