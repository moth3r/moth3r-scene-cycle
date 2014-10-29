bl_info = {
    "name": "Moth3r Scene Cycle",
    "author": "Ivan Santic, Stanislav Blinov",
    "version": (1, 0),
    "blender": (2, 72, 0),
    "location": "",
    "description": "Cycle through scenes via keys",
    "warning": "",
    "wiki_url": "",
    "category": ""
}

import bpy

def iterate(operator, context):
    # get the cycle direction from the property that got parsed to the class
    direction = operator.direction

class SceneCycle(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "moth3r.scene_cycle"
    bl_label = "Cycle through scenes via keys"
    direction = bpy.props.IntProperty()

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        scenes = bpy.data.scenes

        for i, s in enumerate(scenes):
            if s == context.scene:
                 context.screen.scene = scenes[(i+self.direction) % len(scenes)]
                 break

        return {'FINISHED'}

########## REGISTER ############

def register():
    bpy.utils.register_class(SceneCycle)


def unregister():
    bpy.utils.unregister_class(SceneCycle)


if __name__ == "__main__":
    register()
