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

<dl>
<dt>vertices()</dt>
<dt>edges()</dt>
<dt>faces()</dt>
<dt>volumes()</dt>
<dt>set_2d_to_3d_settings()</dt>
<dd>Set 2D to 3D extrusion settings for shapes.</dd>
<dt>get_2d_to_3d_settings()</dt>
<dd>Get 2D to 3D extrusion settings for the first shape in the list.</dd>
<dt>contains()</dt>
<dt>find()</dt>
<dt>remove()</dt>
<dt>get()</dt>
<dt>merge()</dt>
</dl>
