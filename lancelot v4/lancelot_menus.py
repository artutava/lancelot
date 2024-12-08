import bpy
import os
import bpy.utils.previews
from bpy.types import Menu

#West, East, South, North, Northwest, Northeast Southwest Southeast, separators should be added if you want to skip a position pie.separator()

#import bpy.utils.previews
preview_collections = {}
pcoll = bpy.utils.previews.new()
my_icons_dir = os.path.join(os.path.dirname(__file__), "icons")

# load a preview thumbnail of a file and store in the previews collection
pcoll.load("my_icon", os.path.join(my_icons_dir, "logo384.png"), 'IMAGE')
pcoll.load("fingers_l", os.path.join(my_icons_dir, "hand_l.png"), 'IMAGE')
pcoll.load("fingers_r", os.path.join(my_icons_dir, "hand_r.png"), 'IMAGE')
preview_collections["main"] = pcoll



class PIE_MT_IkFingersMenu(Menu):
    """Pie Menu for IK Fingers"""
    bl_label = "Lancelot Select"

    def draw(self, context):

        pcoll = preview_collections["main"]
        fingers_l = pcoll["fingers_l"]
        fingers_r = pcoll["fingers_r"]

        layout = self.layout
        pie = layout.menu_pie()

        # Right Option: IK Fingers R
        op = pie.operator("lct3.select_bone_collection", text="IK Fingers R", icon_value=fingers_r.icon_id)
        op.collection_name = "IK Fingers R"


        # Left Option: IK Fingers L
        op = pie.operator("lct3.select_bone_collection", text="IK Fingers L", icon_value=fingers_l.icon_id)
        op.collection_name = "IK Fingers L"
        
        # Right Option: Control Head
        op = pie.operator("lct3.select_bone_collection", text="Mocap Head")
        op.collection_name = "MOCAP HEAD"
        
        # Right Option: Control Spine
        op = pie.operator("lct3.select_bone_collection", text="Mocap Spine")
        op.collection_name = "MOCAP SPINE"


        # Right Option: Control Arms R
        op = pie.operator("lct3.select_bone_collection", text="Mocap Arms R")
        op.collection_name = "MOCAP ARMS R"

        # Right Option: Control Arms L
        op = pie.operator("lct3.select_bone_collection", text="Mocap Arms L")
        op.collection_name = "MOCAP ARMS L"

        

        # Right Option: Control Legs R
        op = pie.operator("lct3.select_bone_collection", text="Mocap Legs R")
        op.collection_name = "MOCAP LEGS R"

        # Right Option: Control Legs L
        op = pie.operator("lct3.select_bone_collection", text="Mocap Legs L")
        op.collection_name = "MOCAP LEGS L"



        

      
        
