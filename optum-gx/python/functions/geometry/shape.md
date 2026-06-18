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

<dl>
<dt>vertices()</dt>
<dt>edges()</dt>
<dt>faces()</dt>
<dt>volumes()</dt>
<dt>set_2d_to_3d_settings()</dt>
<dd>Set 2D to 3D extrusion settings for this shape.</dd>
<dt>get_2d_to_3d_settings()</dt>
<dd>Get 2D to 3D extrusion settings for this shape.</dd>
</dl>
