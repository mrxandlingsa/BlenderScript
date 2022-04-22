bl_info = {
	"name": "CQScripts",
	"author": "CQ",
	"blender": (3, 1, 0),
    "category": "CQ",
	}


import bpy
import importlib

# if "ResetPosition" not in locals():
#     from . import properties, operators, app_handlers, ui 
#     print("ResetPosition missed")
# else:
#     import importlib

# import modoel scripts
ResetPosition = importlib.reload(ResetPosition)

def register():
    ResetPosition.register()



def unregister():
    ResetPosition.unregister()

if __name__ == "__main__":
    register()