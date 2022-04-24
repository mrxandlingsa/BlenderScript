import bpy 
from bpy.types import Menu


class CQPieMenu(Menu):
    # label is displayed at the center of the pie menu.
    bl_label = "cq tools"
    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()
        pie.operator("object.resetpos")
      
    
    
    
class ResetPositionOrigin(bpy.types.Operator):
   bl_idname = "object.resetpos"
   bl_label = "Reset position to origin"
   bl_options = {'REGISTER', 'UNDO'}

   def execute(self, context):
       objects = bpy.context.selected_objects
       if objects is not None and len(objects) == 1:
           bpy.ops.object.transform_apply(location=False,rotation=False,scale=True)
           objects[0].location[0] = 0
           objects[0].location[1] = 0
           objects[0].location[2] = 0
           objects[0].rotation_euler[0]=0
           objects[0].rotation_euler[1]=0
           objects[0].rotation_euler[2]=0
       return { 'FINISHED' }
   
   
   
class CQEvent(bpy.types.Operator):
   bl_label = "Push pie ui"
   bl_idname = "cq.shortcut"

def execute(self, context):
       objects = bpy.context.selected_objects
       # if objects is not None:
       return { 'FINISHED' }


def invoke(self, context, event): 
   wm = context.window_manager
   return wm.invoke_props_dialog(self)

addon_keymaps = []

classes = [CQPieMenu,ResetPositionOrigin,CQEvent]


def menu_func(self, context):
   self.layout.operator(CQEvent.bl_idname)


def register():
   for cls in classes:
        bpy.utils.register_class(cls)
   wm = bpy.context.window_manager
   kc = wm.keyconfigs.addon
   if kc:
       km = kc.keymaps.new(name='3D View',space_type='VIEW_3D')
       kmi = km.keymap_items.new("wm.call_menu_pie",type = 'F',value = 'PRESS',shift=True)
       addon_keymaps.append((km,kmi))


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
    for km,kmi in addon_keymaps:
       km.addon_keymaps.remove(kmi)
       addon_keymaps.clear()

if __name__ == "__main__":
   register() 
   