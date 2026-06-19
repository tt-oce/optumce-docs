# get_material

Get material(s) from the current project.

Args:
        name: The name of the material to retrieve. If None, returns all materials.

Returns:
        If name is provided: The appropriate Remote material object.
        If name is None: A list of all Remote material objects.

Raises:
        Exception: If the material is not found or has an unknown type.
