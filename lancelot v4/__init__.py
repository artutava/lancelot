# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name" : "Lancelot v4.2",
    "author" : "SirCruX Studios",
    "description" : "",
    "blender" : (4, 0, 0),
    "version" : (4, 2, 0),
    "location" : "",
    "warning" : "",
    "category" : "Rigging"
}

import os
import bpy

from . lancelot_op import LCT3_OT_FK_Layer, LCT3_OT_IK_Layer, LCT3_OT_MOCAP_Layer, LCT3_OT_MOCAP_RAW_Layer, LCT3_OT_FINGERS_Layer, LCT3_OT_FINGERS_IK, LCT3_OT_Select_L_Fingers, LCT3_OT_EYES_Layer, LCT3_OT_Select_R_Fingers, LCT3_OT_Clear_bone_transform, LCT3_OT_Clear_all_bone_transform, LCT3_OT_STR_Reset_Length, LCT3_OT_Stretch_Layer, LCT3_OT_Create_AK_Shapekeys, LCT3_OBJECT_OT_SelectBoneCollection

from . lancelot_panel import LCT3_PT_Panel_Main, LCT3_PT_Panel_Root_Spine, LCT3_PT_Panel_Limbs, LCT3_PT_Panel_Layers, LCT3_PT_Panel_Select, LCT3_PT_Panel_Char_Options, LCT3_PT_Panel_Mocap_Col, LCT3_PT_Panel_AK_Shapekeys

from . lancelot_menus import PIE_MT_IkFingersMenu

classes = (LCT3_PT_Panel_Main, LCT3_PT_Panel_Layers, LCT3_PT_Panel_Select, LCT3_PT_Panel_Limbs,  LCT3_PT_Panel_Root_Spine, LCT3_PT_Panel_Char_Options, LCT3_PT_Panel_Mocap_Col, LCT3_OT_FK_Layer, LCT3_OT_IK_Layer, LCT3_OT_MOCAP_Layer, LCT3_OT_MOCAP_RAW_Layer, LCT3_OT_FINGERS_Layer, LCT3_OT_FINGERS_IK, LCT3_OT_EYES_Layer, LCT3_OT_Clear_bone_transform, LCT3_OT_Select_L_Fingers, LCT3_OT_Select_R_Fingers,  LCT3_OT_Clear_all_bone_transform, LCT3_OT_STR_Reset_Length, LCT3_OT_Stretch_Layer, LCT3_OT_Create_AK_Shapekeys, LCT3_PT_Panel_AK_Shapekeys, LCT3_OBJECT_OT_SelectBoneCollection, PIE_MT_IkFingersMenu)




addon_keymaps = []


def register_keymap():
    wm = bpy.context.window_manager
    if wm.keyconfigs.addon:  # Ensure the addon keymap context is available
        # Create a new keymap for the 3D View
        km = wm.keyconfigs.addon.keymaps.new(name="3D View", space_type="VIEW_3D")

        # Add a new keymap entry for the pie menu
        kmi = km.keymap_items.new("wm.call_menu_pie", "Q", "PRESS", ctrl=True, shift=True)
        kmi.properties.name = "PIE_MT_IkFingersMenu"  # Reference to the pie menu class

        # Store the keymap
        addon_keymaps.append((km, kmi))


def unregister_keymap():
    wm = bpy.context.window_manager
    if wm.keyconfigs.addon:
        # Remove the registered keymaps
        for km, kmi in addon_keymaps:
            km.keymap_items.remove(kmi)
        addon_keymaps.clear()


def register():
    print("ABRIR REGISTER")
    


    print("FORA DO FOR")

    for c in classes:
        bpy.utils.register_class(c)
    #bpy.utils.register_class(LCT3_PT_Panel)
    register_keymap()
    

def unregister():

    unregister_keymap()  # Unregister the shortcut
    
    # for pcoll in preview_collections.values():
    #     bpy.utils.previews.remove(pcoll)
    # preview_collections.clear()
    
    for c in classes:
        bpy.utils.unregister_class(c)
    #bpy.utils.unregister_class(LCT3_PT_Panel)
        
