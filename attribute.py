import maya.cmds as cmds

class Attribute:

    def __init__(self):

    # Create layer instance in Maya
    # @params
    # _name: Name for the layer
    # int: The position the layer is in
    def create_layer(_name, int):
        exists = cmds.objExists(_name)

        if exists is False:
            cmds.createDisplayLayer(name = _name, number = int, nr = True)

    # Change the layer visibility
    # @params
    # layer_name: Name of layer
    # visibility: Must be 0 or 1. 0 = hide, 1 = visible
    def change_visibility(layer_name, visibility):
        cmds.setAttr(concat(layer_name, ".visibility", sep = ","),  visibility)

    def randomize_attributes(list):
        layer = [..] # need category list getter here. To hardcode or to not hardcode?
        for layer_name in layer:

    def get_random_attribute(layer):
        global current_material

        temp_list = layer.children[:] + layer.objects[:]
        selected_name =
