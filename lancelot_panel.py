import os

import bpy
import bpy.utils.previews
from bpy.types import Panel

#import bpy.utils.previews
preview_collections = {}
pcoll = bpy.utils.previews.new()
my_icons_dir = os.path.join(os.path.dirname(__file__), "icons")

# load a preview thumbnail of a file and store in the previews collection
pcoll.load("my_icon", os.path.join(my_icons_dir, "icon.png"), 'IMAGE')
pcoll.load("fingers_l", os.path.join(my_icons_dir, "hand_l.png"), 'IMAGE')
pcoll.load("fingers_r", os.path.join(my_icons_dir, "hand_r.png"), 'IMAGE')
preview_collections["main"] = pcoll


class LCT3_PT_Panel_Main(Panel):
    bl_space_type="VIEW_3D"
    bl_region_type= "UI"
    bl_idname="LCT3_PT_Panel_Main"
    bl_label = "Lancelot Rig v3"
    bl_category = "Lancelot v3"
    #bl_context= "posemode"

    

    def draw(self, context):

        # preview_collections = {}
        # dir = os.path.dirname(bpy.data.filepath)

        # pcoll = bpy.utils.previews.new()

        # for entry in os.scandir(dir):
        #     if entry.name.endswith(".png"):
        #         name = os.path.splitext(entry.name)[0]
        #         pcoll.load(name.upper(), entry.path, "IMAGE")
        pcoll = preview_collections["main"]
        my_icon = pcoll["my_icon"]
        layout = self.layout
        obj = context.object
        if bpy.context.object.type == 'ARMATURE':
            rowsc = layout.row()
            col= rowsc.column()
            rowsc.template_icon(my_icon.icon_id, scale=6)
            col= rowsc.column()

            

            
            row = layout.row()
            row.label(text="Character: " + obj.name)
            
            row = layout.row()
            row.prop(obj, "name")

            row = layout.row()
            row.label(text="Motion Capture")

            row = layout.row()
            row.prop(obj, '["MOCAP"]',slider=True)

            row = layout.row()
            row.label(text="Root")

            row = layout.row()
            row.prop(obj, '["Root Loc Priority"]',slider=True)
            row.prop(obj, '["Root Rot Priority"]',slider=True)

            row = layout.row()
            row.label(text="Spine")

            row = layout.row()
            row.prop(obj, '["Spine 1 Priority"]',slider=True)
            row.prop(obj, '["Spine 2 Priority"]',slider=True)

            row = layout.row()
            row.prop(obj, '["Spine 3 Priority"]',slider=True)
            row.prop(obj, '["Spine 4 Priority"]',slider=True)

            row = layout.row()
            row.label(text="Arms")

            row = layout.row()
            row.prop(obj, '["IK Arm L"]',slider=True)
            row.prop(obj, '["IK Arm R"]',slider=True)

            row = layout.row()
            row.label(text="Arms priority")
            row = layout.row()
            row.prop(obj, '["Arm L Priority"]',slider=True)
            row.prop(obj, '["Arm R Priority"]',slider=True)

            row = layout.row()
            row.label(text="Fingers")
            row = layout.row()
            row.prop(obj, '["Fingers L Priority"]',slider=True)
            row.prop(obj, '["Fingers R Priority"]',slider=True)

            row = layout.row()
            row.label(text="Legs")

            
            row = layout.row()
            row.label(text="Legs priority")
            row = layout.row()
            row.prop(obj, '["Leg L Priority"]',slider=True)
            row.prop(obj, '["Leg R Priority"]',slider=True)
            row = layout.row()
            row.label(text="Eye Mode")
            row = layout.row()
            row.prop(obj, '["Manual/Tracking"]',slider=True)
            

            

            # row = layout.row()
            # row.label(text="New Layers")

            # box = layout.box()
            # box.label (text="Box")
            # boxrow = box.row()
            # boxrow.label(text="New Layers")

            # boxsc = layout.box()
            # boxsc.label (text="Box")
            # boxscrow = box.row()
            # boxscrow.label(text="New Layers")
        else:
            rowsc = layout.row()
            col= rowsc.column()
            rowsc.template_icon(my_icon.icon_id, scale=8)
            col= rowsc.column()
           
            #boxsc.menu(text="TEXTO")
            

        # row = layout.row()
        # row.label(text="Test icon")
        # col = row.column()
        # col.operator("object.duplicate_move", text="Custom Icon", icon_value=pcoll["ICON"].icon_id)
        # col.operator("object.duplicate_move", text="Built-in Icon", icon="OUTPUT")

        

class LCT3_PT_Panel_Layers(Panel):
    bl_space_type="VIEW_3D"
    bl_region_type= "UI"
    bl_idname= "LCT3_PT_Panel_Layers"
    bl_label = "Rig Layers"
    bl_category = "Lancelot Rig"
    bl_context= "posemode"
    bl_parent_id = "LCT3_PT_Panel_Main"
    

    def draw(self, context):

        layout = self.layout

        obj = context.object

        #Trocar icone mocap----------------------
        status_mocap= obj["LT MOCAP"]

        if status_mocap == 1:
            mocap_icon ="HIDE_OFF"
            mocap_txt="Mostrar MOCAP"
        else:
            mocap_icon="HIDE_ON"
            mocap_txt="Esconder MOCAP"

        #Trocar icone mocap original----------------------
        status_mocap_raw = obj["LT MOCAP RAW"]

        if status_mocap_raw == 1:
            mocap_raw_icon ="HIDE_OFF"
            mmocap_raw_txt="Mostrar MOCAP"
        else:
            mocap_raw_icon="HIDE_ON"
            mocap_raw_txt="Esconder MOCAP"


        #Trocar icone FK--------------------------
        status_fk= obj["LT FK"]

        if status_fk == 1:
            fk_icon ="HIDE_OFF"
            fk_txt="Mostrar FK"
        else:
            fk_icon="HIDE_ON"
            fk_txt="Esconder FK"

        #Trocar icone IK---------------------------
        status_ik= obj["LT IK"]

        if status_ik == 1:
            ik_icon ="HIDE_OFF"
            ik_txt="Mostrar IK"
        else:
            ik_icon="HIDE_ON"
            ik_txt="Esconder IK"
        
         #Trocar icone EYES---------------------------
        status_eyes= obj["LT EYES"]

        if status_eyes == 1:
            eyes_icon ="HIDE_OFF"
            eyes_txt="Mostrar EYES"
        else:
            eyes_icon="HIDE_ON"
            eyes_txt="Esconder EYES"
        
         #Trocar icone FINGERS---------------------------
        status_fingers= obj["LT FINGERS"]

        if status_fingers == 1:
            fingers_icon ="HIDE_OFF"
            fingers_txt="Mostrar FINGERS"
        else:
            fingers_icon="HIDE_ON"
            fingers_txt="Esconder FINGERS"
        
        
        row = layout.row()

        row.label(text="IK / FK")
        row = layout.row()

        col= row.column()
        col.operator("lct3.fklayer", icon=fk_icon)
        
       
        col = row.column()
        col.operator("lct3.iklayer", icon=ik_icon)
        
        row = layout.row()
        row.label(text="MOCAP")
        row = layout.row()
        col = row.column()
        col.operator("lct3.mocaplayer", icon=mocap_icon, text="CONTROL")
        
        col = row.column()
        col.operator("lct3.mocaprawlayer", icon=mocap_raw_icon, text="RAW")

        row = layout.row()
        row.label(text="EXTRA")
        row = layout.row()
        col = row.column()

        col.operator("lct3.eyeslayer", icon=eyes_icon, text="EYES")
        
        col = row.column()
        col.operator("lct3.fingerslayer", icon=fingers_icon, text="FINGERS")
        
        
class LCT3_PT_Panel_Select(Panel):
    bl_space_type="VIEW_3D"
    bl_region_type= "UI"
    bl_idname= "LCT3_PT_Panel_Select"
    bl_label = "Select Elements"
    bl_category = "Lancelot Rig"
    #bl_context= "posemode"
    bl_parent_id = "LCT3_PT_Panel_Main"
    

    def draw(self, context):
        pcoll = preview_collections["main"]
        fingers_l = pcoll["fingers_l"]
        fingers_r = pcoll["fingers_r"]

        layout = self.layout

        obj = context.object
        
        row = layout.row()

        col = row.column()
        col.operator("lct3.fk_l_fingers", text="Left Fingers", icon_value=fingers_l.icon_id)

        col = row.column()
        col.operator("lct3.fk_r_fingers", text="Right Fingers", icon_value=fingers_r.icon_id)
        
        row = layout.row()
        row.label(text="Cleaning Tools")
        row = layout.row()
        col = row.column()
        col.operator("lct3.clear_bone_transform", text="Clear Selected", icon="CON_ARMATURE")
        row = layout.row()
        col = row.column()
        col.operator("lct3.clear_bone_transform", text="Clear All", icon="OUTLINER_OB_ARMATURE")
        
        row = layout.row()
        col = row.column()
        col.operator("lct3.set_inverse_all", text="Cleanup Controls", icon="SPHERE")
        
        

        
    




        

        

        

     

        