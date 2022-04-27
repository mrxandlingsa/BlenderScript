import bpy
from bpy.props import (StringProperty,
                       PointerProperty,
                       )
                       
from bpy.types import (Panel,
                       PropertyGroup,
                       )


class CQFbxProperties(PropertyGroup):     
        Path: StringProperty(
        name="Path",
        description=":",
        default="",
        maxlen=1024,
        subtype="FILE_PATH"
        )



class CQExportFbxPanel(bpy.types.Panel):
    bl_label = "CQSaveFbx"
    bl_idname = "cq.savefbx"
    bl_space_type = "VIEW_3D"   
    bl_region_type = "UI"
    bl_category = "CQTool" 

    def draw(self, context):
        layout = self.layout

        scene = context.scene
        mytool = scene.my_tool

        layout.prop(mytool, "Path")
        layout.operator("cq.exportfbxoperator")






class ExportFbxAction(bpy.types.Operator):
    bl_idname = "cq.exportfbxoperator"
    bl_label = "CQ Export FBX"
    
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        FolderPath = mytool.Path
        objects = bpy.context.selected_objects
        if mytool is not None and len(objects) == 1 and objects is not None:
            ObjectName = objects[0].name
            PathName = FolderPath + ObjectName +'.fbx'
            bpy.ops.export_scene.fbx(
            filepath = PathName,
            check_existing = False,
            filter_glob = "*.fbx",
            global_scale = 1,
            apply_unit_scale = True,
            use_space_transform = True,
            bake_space_transform = False,
            use_mesh_modifiers = True,
            use_mesh_modifiers_render = True,
            mesh_smooth_type = 'OFF',
            use_subsurf = False,
            use_mesh_edges = False,
            use_tspace = False,
            use_custom_props = False,
            add_leaf_bones = False,
            use_selection = True,
            use_active_collection = False,
            object_types = {"MESH"},
            primary_bone_axis = 'Y',
            secondary_bone_axis = 'X',
            use_armature_deform_only = False,
            armature_nodetype = 'NULL',
            # animation setting
            bake_anim= False,
            bake_anim_use_all_bones= False,
            bake_anim_use_nla_strips= False,
            bake_anim_use_all_actions= False,
            bake_anim_force_startend_keying = False,
            bake_anim_step = 1.0,
            bake_anim_simplify_factor = 1.0,
            path_mode = 'AUTO',
            embed_textures = False,
            batch_mode = 'OFF',
            use_batch_own_dir = True,
            use_metadata = True,
            axis_forward = '-Z',
            axis_up = 'Y'
            )
        return {'FINISHED'}

classes = [ExportFbxAction,CQExportFbxPanel,CQFbxProperties]


def menu_func(self, context):
    self.layout.operator(ExportFbxAction.bl_idname, text=ExportFbxAction.bl_label)

# Register and add to the "object" menu (required to also use F3 search "Simple Object Operator" for quick access)
def register():
    bpy.types.VIEW3D_MT_object.append(menu_func)
    for cls in classes:
        bpy.utils.register_class(cls)
        
    bpy.types.Scene.my_tool = bpy.props.PointerProperty(type=CQFbxProperties)
        
        
def unregister():
    bpy.types.VIEW3D_MT_object.remove(menu_func)
    for cls in classes:
        bpy.utils.unregister_class(cls)
    del bpy.types.Scene.mytool
    
    
if __name__ == "__main__":
    register()
