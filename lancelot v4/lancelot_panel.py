import os

import bpy
import bpy.utils.previews
from bpy.types import Panel

#import bpy.utils.previews
preview_collections = {}
pcoll = bpy.utils.previews.new()
my_icons_dir = os.path.join(os.path.dirname(__file__), "icons")

# load a preview thumbnail of a file and store in the previews collection
pcoll.load("my_icon", os.path.join(my_icons_dir, "logo384.png"), 'IMAGE')
pcoll.load("fingers_l", os.path.join(my_icons_dir, "hand_l.png"), 'IMAGE')
pcoll.load("fingers_r", os.path.join(my_icons_dir, "hand_r.png"), 'IMAGE')
preview_collections["main"] = pcoll


class LCT3_PT_Panel_Main(Panel):
    bl_space_type="VIEW_3D"
    bl_region_type= "UI"
    bl_idname="LCT3_PT_Panel_Main"
    bl_label = "Lancelot Rig V4.2"
    bl_category = "Lancelot V4.2"
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
            row.prop(obj, "name")

            row = layout.row()
            row.label(text="Motion Capture")

            row = layout.row()
            row.prop(obj, '["MOCAP"]',slider=True)

            

        

            
            

            

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
            rowsc.template_icon(my_icon.icon_id, scale=7)
            col= rowsc.column()
            layout = self.layout
            row = layout.row()
            row.label(text="No Armature Selected.", icon='ERROR', icon_value=2)


           
            #boxsc.menu(text="TEXTO")
            

        # row = layout.row()
        # row.label(text="Test icon")
        # col = row.column()
        # col.operator("object.duplicate_move", text="Custom Icon", icon_value=pcoll["ICON"].icon_id)
        # col.operator("object.duplicate_move", text="Built-in Icon", icon="OUTPUT")


class LCT3_PT_Panel_Root_Spine(Panel):
    bl_space_type="VIEW_3D"
    bl_region_type= "UI"
    bl_idname= "LCT3_PT_Panel_Root_Spine"
    bl_label = "Mocap Overlays"
    bl_category = "Lancelot Rig"
    bl_parent_id = "LCT3_PT_Panel_Main"
    
    def draw(self, context):

        layout = self.layout

        obj = context.object
        if bpy.context.object.type == 'ARMATURE':
            row = layout.row()
            row.label(text="Root")

            row = layout.row()
            row.prop(obj, '["Root Loc Priority"]',slider=True)
            row.prop(obj, '["Root Rot Priority"]',slider=True)
            
            layout.separator()

            row = layout.row()
            row.label(text="Spine")

            row = layout.row()
            row.prop(obj, '["Spine 1 Priority"]',slider=True)
            row.prop(obj, '["Spine 2 Priority"]',slider=True)

            row = layout.row()
            row.prop(obj, '["Spine 3 Priority"]',slider=True)
            row.prop(obj, '["Spine 4 Priority"]',slider=True)


class LCT3_PT_Panel_Limbs(Panel):
    bl_space_type="VIEW_3D"
    bl_region_type= "UI"
    bl_idname= "LCT3_PT_Panel_Limbs"
    bl_label = "Limbs Switches"
    bl_category = "Lancelot Rig"
    bl_context= "posemode"
    bl_parent_id = "LCT3_PT_Panel_Main"

    
    
    def draw(self, context):
        
        layout = self.layout

        obj = context.object
        if bpy.context.object.type == 'ARMATURE':
            row = layout.row()
            row.label(text="Arms IK")

            row = layout.row()
            row.prop(obj, '["IK Arm L"]',slider=True)
            row.prop(obj, '["IK Arm R"]',slider=True)
            
            layout.separator()

            row = layout.row()
            row.label(text="Arms FK")
            row = layout.row()
            row.prop(obj, '["Arm L Priority"]',slider=True)
            row.prop(obj, '["Arm R Priority"]',slider=True)

            layout.separator()

            row = layout.row()
            row.label(text="Fingers")
            row = layout.row()
            row.prop(obj, '["Fingers L Priority"]',slider=True)
            row.prop(obj, '["Fingers R Priority"]',slider=True)
            
            
            layout.separator()
            row = layout.row()
            row.label(text="Legs")

            row = layout.row()
            row.prop(obj, '["Leg L Priority"]',slider=True)
            row.prop(obj, '["Leg R Priority"]',slider=True)
            row = layout.row()
            row.label(text="Eye Mode")
            row = layout.row()
            row.prop(obj, '["Manual/Tracking"]',slider=True)



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
        arm = bpy.context.object.data

        if bpy.context.object.type == 'ARMATURE':

           

            if arm.collections['MOCAP'].is_visible == True:
                mocap_icon ="HIDE_OFF"
                mocap_txt="Mostrar MOCAP"
            else:
                mocap_icon="HIDE_ON"
                mocap_txt="Esconder MOCAP"

            

            #Trocar icone mocap original----------------------

            if arm.collections['MOCAP RAW'].is_visible == True:
                mocap_raw_icon ="HIDE_OFF"
                mmocap_raw_txt="Mostrar MOCAP"
            else:
                mocap_raw_icon="HIDE_ON"
                mocap_raw_txt="Esconder MOCAP"


            #Trocar icone STRETCH----------------------
            if arm.collections['STRETCH'].is_visible == True:
                stretch_icon ="HIDE_OFF"
                stretch_txt="Mostrar Stretch"
            else:
                stretch_icon="HIDE_ON"
                stretch_txt="Esconder Stretch"



            #Trocar icone FK--------------------------
            

            if arm.collections['FK'].is_visible == True:
                fk_icon ="HIDE_OFF"
                fk_txt="Mostrar FK"
            else:
                fk_icon="HIDE_ON"
                fk_txt="Esconder FK"

            #Trocar icone IK---------------------------
           

            if arm.collections['IK'].is_visible == True:
                ik_icon ="HIDE_OFF"
                ik_txt="Mostrar IK"
            else:
                ik_icon="HIDE_ON"
                ik_txt="Esconder IK"
            
            #Trocar icone EYES---------------------------
           

            if arm.collections['EYES'].is_visible == True:
                eyes_icon ="HIDE_OFF"
                eyes_txt="Mostrar EYES"
            else:
                eyes_icon="HIDE_ON"
                eyes_txt="Esconder EYES"
            
            #Trocar icone FINGERS---------------------------
            

            if arm.collections['FK Fingers'].is_visible == True:
                fingers_icon ="HIDE_OFF"
                fingers_txt="Mostrar FINGERS FK"
            else:
                fingers_icon="HIDE_ON"
                fingers_txt="Esconder FINGERS FK"

                #Trocar icone FINGERS IK---------------------------
            
            
            if arm.collections['IK Fingers'].is_visible == True:
                fingers_ik_icon ="HIDE_OFF"
                fingers_ik_txt="Mostrar FINGERS IK"
            else:
                fingers_ik_icon="HIDE_ON"
                fingers_ik_txt="Esconder FINGERS IK"
            
            
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
            col.operator("lct3.fingersik", icon=fingers_ik_icon, text="FINGERS IK")
            col = row.column()
            col.operator("lct3.fingerslayer", icon=fingers_icon, text="FINGERS FK")
            
            row = layout.row()
            
            col = row.column()
            col.operator("lct3.eyeslayer", icon=eyes_icon, text="EYES")
            col = row.column()
            col.operator("lct3.stretchlayer", icon=stretch_icon, text="STRETCH")
        
        
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
        
        if bpy.context.object.type == 'ARMATURE':
            row = layout.row()

            col = row.column()
            col.operator("lct3.fk_l_fingers", text="Left Fingers", icon_value=fingers_l.icon_id)

            col = row.column()
            col.operator("lct3.fk_r_fingers", text="Right Fingers", icon_value=fingers_r.icon_id)
            
            row = layout.row()
            row.label(text="Clear")
            row = layout.row()
            col = row.column()
            col.operator("lct3.clear_bone_transform", text="Selected", icon="CON_ARMATURE")

            col = row.column()
            col.operator("lct3.clear_all_bone_transform", text="All", icon="OUTLINER_OB_ARMATURE")
            
            row= layout.row ()
            col = row.column()
            col.operator("lct3.reset_length", text="Reset St. Length", icon="OUTLINER_OB_GREASEPENCIL")
        
        

        
    
class LCT3_PT_Panel_Char_Options(Panel):
    bl_space_type="VIEW_3D"
    bl_region_type= "UI"
    bl_idname= "LCT3_PT_Panel_Char_Options"
    bl_label = "Character Options"
    bl_category = "Lancelot Rig"
    bl_parent_id = "LCT3_PT_Panel_Main"

    def draw(self, context):

        layout = self.layout
        row = layout.row()
        obj = context.object
        if bpy.context.object.type == 'ARMATURE':
            row = layout.row()
            row.label(text="Mocap Arms Offset")

            row = layout.row()
            row.prop(obj, '["Arm Offset"]',slider=True)

            row = layout.row()
            row.label(text="Bendy Bones Options")
            row = layout.row()
            row.prop(obj, '["Ease"]',slider=True)
    

class LCT3_PT_Panel_Mocap_Col(Panel):
    bl_space_type="VIEW_3D"
    bl_region_type= "UI"
    bl_idname= "LCT3_PT_Panel_Mocap_Col"
    bl_label = "Mocap Collisions"
    bl_category = "Lancelot Rig"
    bl_parent_id = "LCT3_PT_Panel_Main"

    def draw(self, context):

        layout = self.layout
        row = layout.row()
        obj = context.object
        if bpy.context.object.type == 'ARMATURE':
            row = layout.row()
            row.label(text="Collisions Setup")

            row = layout.row()
            row.prop(obj, '["Collision"]',slider=True)
            row = layout.row()
            row.prop(obj, '["Collision Head"]',slider=True)
            row = layout.row()
            row.prop(obj, '["Collision Top"]',slider=True)
            row = layout.row()
            row.prop(obj, '["Collision Bottom"]',slider=True)
            row = layout.row()
            row.prop(obj, '["Collision Legs"]',slider=True)


class LCT3_PT_Panel_AK_Shapekeys(Panel):
    bl_space_type="VIEW_3D"
    bl_region_type= "UI"
    bl_idname= "LCT3_PT_Panel_AK_Shapekeys"
    bl_label = "Arkit Shapekeys"
    bl_category = "Lancelot Rig"
    bl_parent_id = "LCT3_PT_Panel_Main"

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        obj = context.object
        if bpy.context.object.type == 'MESH':
            row = layout.row()
            col = row.column()
            col.operator("lct3.create_ak_shapekeys", text="Generate ARKIT Shapekeys", icon="MESH_MONKEY")



        

        

        

     

        