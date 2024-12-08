import bpy

from bpy.types import Operator



class LCT3_OT_FK_Layer(Operator):
    bl_idname = "lct3.fklayer"
    bl_label = "FK"
    bl_description= "Fk Controls for Traditional Animation"
 
    
    def execute (self,context):
        obj = context.object
        if bpy.context.object.type == 'ARMATURE':
            arm = bpy.context.object.data

            if arm.collections['FK'].is_visible == False:
                arm.collections['FK'].is_visible = True
            else:
                arm.collections['FK'].is_visible = False

            return {'FINISHED'}
        else:
            def draw(self, context):
                self.layout.label(text="No Armature selected!")

            bpy.context.window_manager.popup_menu(draw, title="Error", icon='ERROR')
            return {'FINISHED'}


class LCT3_OT_Stretch_Layer(Operator):
    bl_idname = "lct3.stretchlayer"
    bl_label = "Stretch"
    bl_description= "Stretch Layer"
 
    
    def execute (self,context):
        obj = context.object
        if bpy.context.object.type == 'ARMATURE':
            arm = bpy.context.object.data

            if arm.collections['STRETCH'].is_visible == False:
                arm.collections['STRETCH'].is_visible = True
            else:
                arm.collections['STRETCH'].is_visible = False
                

            return {'FINISHED'}
        else:
            def draw(self, context):
                self.layout.label(text="No Armature selected!")

            bpy.context.window_manager.popup_menu(draw, title="Error", icon='ERROR')
            return {'FINISHED'}





class LCT3_OT_IK_Layer(Operator):
    bl_idname = "lct3.iklayer"
    bl_label = "IK"
    bl_description= "Ik controls for Traditional Animation"

     
    def execute (self,context):
        obj = context.object
        if bpy.context.object.type == 'ARMATURE':
            arm = bpy.context.object.data

            if arm.collections['IK'].is_visible == False:
                arm.collections['IK'].is_visible = True
            else:
                arm.collections['IK'].is_visible = False

            return {'FINISHED'}
        else:
            def draw(self, context):
                self.layout.label(text="No Armature selected!")

            bpy.context.window_manager.popup_menu(draw, title="Error", icon='ERROR')
            return {'FINISHED'}

  

class LCT3_OT_MOCAP_Layer(Operator):
    bl_idname = "lct3.mocaplayer"
    bl_label = "MOCAP"
    bl_description= "Control Mocap Handles, used for refining Mocap (Keyframes should be added, when manipulating the handles"

    def execute (self,context):
        obj = context.object
        if bpy.context.object.type == 'ARMATURE':
            arm = bpy.context.object.data

            if arm.collections['MOCAP'].is_visible == False:
                arm.collections['MOCAP'].is_visible = True
            else:
                arm.collections['MOCAP'].is_visible = False
               

            return {'FINISHED'}
        else:
            def draw(self, context):
                self.layout.label(text="No Armature selected!")

            bpy.context.window_manager.popup_menu(draw, title="Error", icon='ERROR')
            return {'FINISHED'}



class LCT3_OT_MOCAP_RAW_Layer(Operator):
    bl_idname = "lct3.mocaprawlayer"
    bl_label = "MOCAP RAW"
    bl_description= "Raw Mocap Animation, Used for reference"

    def execute (self,context):
        obj = context.object
        if bpy.context.object.type == 'ARMATURE':
            arm = bpy.context.object.data

            if arm.collections['MOCAP RAW'].is_visible == False:
                arm.collections['MOCAP RAW'].is_visible = True
            else:
                arm.collections['MOCAP RAW'].is_visible = False
                

            return {'FINISHED'}
        else:
            def draw(self, context):
                self.layout.label(text="No Armature selected!")

            bpy.context.window_manager.popup_menu(draw, title="Error", icon='ERROR')
            return {'FINISHED'}

class LCT3_OT_FINGERS_Layer(Operator):
    bl_idname = "lct3.fingerslayer"
    bl_label = "FINGERS LAYER"
    bl_description= "FK Finger Controls"

    def execute (self,context):
        obj = context.object
        if bpy.context.object.type == 'ARMATURE':
            arm = bpy.context.object.data

            if arm.collections['FK Fingers'].is_visible == False:
                arm.collections['FK Fingers'].is_visible = True
            else:
                arm.collections['FK Fingers'].is_visible = False
               

            return {'FINISHED'}
        else:
            def draw(self, context):
                self.layout.label(text="No Armature selected!")

            bpy.context.window_manager.popup_menu(draw, title="Error", icon='ERROR')
            return {'FINISHED'}


class LCT3_OT_FINGERS_IK(Operator):
    bl_idname = "lct3.fingersik"
    bl_label = "FINGERS IK LAYER"
    bl_description= "IK Finger Controls"

    def execute (self,context):
        obj = context.object
        if bpy.context.object.type == 'ARMATURE':
            arm = bpy.context.object.data

            if arm.collections['IK Fingers'].is_visible == False:
                arm.collections['IK Fingers'].is_visible = True
            else:
                arm.collections['IK Fingers'].is_visible = False
               

            return {'FINISHED'}
        else:
            def draw(self, context):
                self.layout.label(text="No Armature selected!")

            bpy.context.window_manager.popup_menu(draw, title="Error", icon='ERROR')
            return {'FINISHED'}

class LCT3_OT_EYES_Layer(Operator):
    bl_idname = "lct3.eyeslayer"
    bl_label = "EYES LAYER"
    bl_description= "Eye Controls"

    def execute (self,context):
        obj = context.object
        if bpy.context.object.type == 'ARMATURE':
            arm = bpy.context.object.data

            if arm.collections['EYES'].is_visible == False:
                arm.collections['EYES'].is_visible = True
            else:
                arm.collections['EYES'].is_visible = False
                

            return {'FINISHED'}
        else:
            def draw(self, context):
                self.layout.label(text="No Armature selected!")

            bpy.context.window_manager.popup_menu(draw, title="Error", icon='ERROR')
            return {'FINISHED'}


class LCT3_OT_Select_L_Fingers(Operator):
    bl_idname = "lct3.fk_l_fingers"
    bl_label = "Select Left Hand Fingers"
    bl_description= "Select all controls for fingers in Left Hand"

    def execute (self,context):
        if bpy.context.object.type == 'ARMATURE':
            obj = context.object
            arm = bpy.context.object.data
            #get to pose mode
            bpy.ops.object.mode_set(mode='POSE')
            #deselect previous bone group
            
            #select bone group in menu
            arm.collections['FK Fingers L'].is_visible = True
            arm.collections.active = arm.collections['FK Fingers L']
            bpy.ops.armature.collection_select()
            return {'FINISHED'}
        else:
            def draw(self, context):
                self.layout.label(text="No Armature selected!")

            bpy.context.window_manager.popup_menu(draw, title="Error", icon='ERROR')
            return {'FINISHED'}

class LCT3_OT_Select_R_Fingers(Operator):
    bl_idname = "lct3.fk_r_fingers"
    bl_label = "Select Right Hand Fingers"
    bl_description= "Select all controls for fingers in Right Hand"

    def execute (self,context):
        if bpy.context.object.type == 'ARMATURE':
            obj = context.object
            arm = bpy.context.object.data
            #get to pose mode
            bpy.ops.object.mode_set(mode='POSE')
            #deselect previous bone group
            
            #select bone group in menu
            arm.collections['FK Fingers R'].is_visible = True
            arm.collections.active = arm.collections['FK Fingers R']
            bpy.ops.armature.collection_select()
            return {'FINISHED'}
        else:
            def draw(self, context):
                self.layout.label(text="No Armature selected!")

            bpy.context.window_manager.popup_menu(draw, title="Error", icon='ERROR')
            return {'FINISHED'}


class LCT3_OT_Clear_bone_transform(Operator):
    bl_idname = "lct3.clear_bone_transform"
    bl_label = "Clear Transforms"
    bl_description= "Clear transform of selected bones, so they get back to original state"

    def execute (self,context):
        if bpy.context.object.type == 'ARMATURE':
            print("hey")
            if bpy.context.selected_pose_bones is not None: 
                print("hey2")
                obj = context.object
                #get to pose mode
                bpy.ops.object.mode_set(mode='POSE')
                bpy.ops.pose.transforms_clear()
                print("hey3")
            else:
                def draw(self, context):
                    self.layout.label(text="No Bone selected!")

                bpy.context.window_manager.popup_menu(draw, title="Error", icon='ERROR')

            
            return {'FINISHED'}
        else:
            def draw(self, context):
                self.layout.label(text="No Armature selected!")

            bpy.context.window_manager.popup_menu(draw, title="Error", icon='ERROR')
            return {'FINISHED'}



class LCT3_OT_Clear_all_bone_transform(Operator):
    bl_idname = "lct3.clear_all_bone_transform"
    bl_label = "Clear All Transforms"
    bl_description= "Clear all transform in selected armature, so they get back to original state"

    def execute(self, context):
        # Ensure an armature is selected
        if bpy.context.active_object and bpy.context.active_object.type == 'ARMATURE':
            armature = bpy.context.active_object
            
            # Clear pose transforms for all bones in the selected armature
            for bone in armature.pose.bones:
                # Store the original rotation mode
                original_rotation_mode = bone.rotation_mode
                
                bone.location.zero()
                bone.rotation_quaternion.identity()
                bone.rotation_euler.zero()
                bone.scale = (1, 1, 1)
                bone.rotation_axis_angle[0] = 0
                bone.rotation_axis_angle[1] = 1
                bone.rotation_axis_angle[2] = 0
                bone.rotation_axis_angle[3] = 0

                # Set the rotation mode back to its original value
                bone.rotation_mode = original_rotation_mode

            # Update the viewport
            bpy.context.view_layer.update()
        return {'FINISHED'}

class LCT3_OT_STR_Reset_Length(Operator):
    bl_idname = "lct3.reset_length"
    bl_label = "Stretch Length Reset"
    bl_description= "Stretch Length Reset"
 
    def execute (self,context):
        obj = context.object
        if bpy.context.object.type == 'ARMATURE':
            bpy.ops.object.mode_set(mode='POSE')
             # Iterate through the pose bones
            for bone in obj.pose.bones:
                # Iterate through the constraints of the bone
                for constraint in bone.constraints:
                    # Check if the constraint is of type "STRETCH_TO"
                    if constraint.type == 'STRETCH_TO':
                        # Reset the Stretch To constraint
                        constraint.rest_length = 0
            # Return to Object mode (optional)
            bpy.ops.object.mode_set(mode='OBJECT')
            return {'FINISHED'}
        else:
            def draw(self, context):
                self.layout.label(text="No Armature selected!")

            bpy.context.window_manager.popup_menu(draw, title="Error", icon='ERROR')
            return {'FINISHED'}


class LCT3_OT_Create_AK_Shapekeys(Operator):
    bl_idname = "lct3.create_ak_shapekeys"
    bl_label = "Create ARKIT Shapekeys"
    bl_description= "Create Arkit Shapekeys"
 
    def execute (self,context):
        obj = bpy.context.object
        shapelist = [ "Key 1", "browInnerUp", "browDown_L", "browDown_R", "browOuterUp_L", "browOuterUp_R", "eyeLookUp_L", "eyeLookUp_R", "eyeLookDown_L", "eyeLookDown_R", "eyeLookIn_L", "eyeLookIn_R", "eyeLookOut_L", "eyeLookOut_R", "eyeBlink_L", "eyeBlink_R", "eyeSquint_L", "eyeSquint_R", "eyeWide_L", "eyeWide_R", "cheekPuff", "cheekSquint_L", "cheekSquint_R", "noseSneer_L", "noseSneer_R", "jawOpen", "jawForward", "jawLeft", "jawRight", "mouthFunnel", "mouthPucker", "mouthLeft", "mouthRight", "mouthRollUpper", "mouthRollLower", "mouthShrugUpper", "mouthShrugLower", "mouthClose", "mouthSmile_L", "mouthSmile_R", "mouthFrown_L", "mouthFrown_R", "mouthDimple_L", "mouthDimple_R", "mouthUpperUp_L", "mouthUpperUp_R", "mouthLowerDown_L", "mouthLowerDown_R", "mouthPress_L", "mouthPress_R", "mouthStretch_L", "mouthStretch_R", "tongueOut"]
        if obj:
            if obj.type == 'MESH':
                if not obj.data.shape_keys:
                    obj.shape_key_add(name="Basis", from_mix=False)
                for each in shapelist:
                    if each not in obj.data.shape_keys.key_blocks:
                        print(f"Creating shape key: {each}")
                        obj.shape_key_add(name=each, from_mix=False)
                        
                    else:
                        print(f"Shape key already exists: {each}")
                        def draw(self, context):
                            self.layout.label(text="Shape key already exist!")
                        
                        
            else:
                print("Selected object is not a mesh")
                def draw(self, context):
                            self.layout.label(text="Selected object is not a mesh")
                
                
        else:
            print("No object selected")
            def draw(self, context):
                            self.layout.label(text="No object selected")
           
        return {'FINISHED'}




class LCT3_OBJECT_OT_SelectBoneCollection(Operator):
    """Operator to select a bone collection"""
    bl_idname = "lct3.select_bone_collection"
    bl_label = "Select Bone Collection"
    bl_description = "Select all controls for a specific bone collection"

    collection_name: bpy.props.StringProperty()

    def execute(self, context):
        if bpy.context.object and bpy.context.object.type == 'ARMATURE':
            obj = context.object
            arm = obj.data

            # Ensure the bone collection exists
            bone_collection = arm.collections_all.get(self.collection_name)
            if not bone_collection:
                self.report({'ERROR'}, f"No collection named '{self.collection_name}'")
                return {'CANCELLED'}

            # Switch to Pose Mode
            bpy.ops.object.mode_set(mode='POSE')

            # Make the collection visible
            bone_collection.is_visible = True

            # Set the active bone collection
            arm.collections.active = bone_collection

            # Select all bones in the collection
            bpy.ops.armature.collection_select()

            self.report({'INFO'}, f"Selected bones in collection: {self.collection_name}")
            return {'FINISHED'}
        else:
            # Popup error message if no armature is selected
            def draw(self, context):
                self.layout.label(text="No Armature selected!")

            bpy.context.window_manager.popup_menu(draw, title="Error", icon='ERROR')
            return {'CANCELLED'}
