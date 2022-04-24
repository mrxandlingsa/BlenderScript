bl_info = {
	"name": "CQScripts",
	"author": "ChenQiong",
	"blender": (3, 0, 0),
    "category": "CQ",
	}


import bpy
import importlib
from CQtools import CQExportFbx,ResetPosition


modules = (CQExportFbx,ResetPosition)


def register():
 for m in modules:
        m.register()
      
def unregister():
    for m in modules:
            m.unregister()

if __name__ == "__main__":
    register()

