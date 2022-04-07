# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####


#----------------------------------------------------------------------
# DEV RELEASES
# Complete Name script: Geometry Nodes User Library
# Author: uriel Deveaud
# Start Date: 03/2022
#----------------------------------------------------------------------
###  HISTORY

# Release 1.4
# ///////////
# Date: 08/04/2022
# Details: Re-wrap addon Preferences 
#/////////////////////////////

# Release 1.3
# ///////////
# Date: 07/04/2022
# Details: Re-Define Project library + user libraries
#/////////////////////////////

# Release 1.2
# ///////////
# Date: 06/04/2022
# Details: Clearing addon, ONLY geometry nodes context
#/////////////////////////////

# Release 1.0
# Date: 04/04/2022
# Details: Add addon preferences to set the paths
#/////////////////////////////

# Release 0.5
# Date: 02/04/2022
# Details: Rewriting of the complete code structure, categories, paths
#/////////////////////////////

# Release 0.1 "First Release"
# Date: 015/03/2022
# Details: Development and analyse "node_presets.py
#/////////////////////////////


#----------------------------------------------------------------------
bl_info = {
    "name": "Geometry Node User Libraries",
    "description": "Geometry Nodes User Library with simple settings",
    "author": "uriel Deveaud (inspired by node_presets.py)",
    "version": (1, 4, 0),
    "blender": (3, 0, 0),
    "location": "Geometry Node Editor > Add > User Library",
    "warning": "",
    "tracker_url": "https://github.com/KoreTeknology/Blender-GN-Library-Addon",
    "support": "COMMUNITY",
    "category": "Node",
}

import os
import bpy
from bpy.types import (
    Operator,
    Menu,
    Panel,
    AddonPreferences,
)

from bpy.props import (
    StringProperty,
    BoolProperty,
)

# ##################################
# ADD Presets
# ##################################

def gn_node_center(context):
    from mathutils import Vector
    loc = Vector((0.0, 0.0))
    node_selected = context.selected_nodes
    if node_selected:
        for node in node_selected:
            loc += node.location
        loc /= len(node_selected)
    return loc


def gn_node_library_add(context, filepath, node_group, ungroup, report):
    """ Main function
    """

    space = context.space_data
    node_tree = space.node_tree
    node_active = context.active_node
    node_selected = context.selected_nodes

    if node_tree is None:
        report({'ERROR'}, "No node tree available")
        return

    with bpy.data.libraries.load(filepath, link=False) as (data_from, data_to):
        assert(node_group in data_from.node_groups)
        data_to.node_groups = [node_group]
    node_group = data_to.node_groups[0]

    # add node!
    center = gn_node_center(context)

    for node in node_tree.nodes:
        node.select = False

    node_type_string = {
        "GeometryNodeTree": "GeometryNodeGroup",
    }[type(node_tree).__name__]

    node = node_tree.nodes.new(type=node_type_string)
    node.node_tree = node_group

    is_fail = (node.node_tree is None)
    if is_fail:
        report({'WARNING'}, "Incompatible node type")

    node.select = True
    node_tree.nodes.active = node
    node.location = center

    if is_fail:
        node_tree.nodes.remove(node)
    else:
        if ungroup:
            bpy.ops.node.group_ungroup()


# ##################################
# DEFINE Paths
# ##################################

def gn_userlib_category1_path(context):
    preferences = context.preferences
    addon_prefs = preferences.addons[__name__].preferences
    dirpath = addon_prefs.userlib_cat1_path
    return dirpath

def gn_userlib_category2_path(context):
    preferences = context.preferences
    addon_prefs = preferences.addons[__name__].preferences
    dirpath2 = addon_prefs.userlib_cat2_path
    return dirpath2

def gn_userlib_category3_path(context):
    preferences = context.preferences
    addon_prefs = preferences.addons[__name__].preferences
    dirpath3 = addon_prefs.userlib_cat3_path
    return dirpath3
    
def gn_userlib_project__path_1(context):
    preferences = context.preferences
    addon_prefs = preferences.addons[__name__].preferences
    dirpathproject1 = addon_prefs.userlib_pro1_path
    return dirpathproject1    

# ##################################
# Addon Preferences
# ##################################

class GnNodeLibraryPrefs(AddonPreferences):
    bl_idname = __name__

    userlib_cat1_path: StringProperty(name="User Category 1 Path",subtype='DIR_PATH',)
    userlib_cat2_path: StringProperty(name="User Category 2 Path",subtype='DIR_PATH',)
    userlib_cat3_path: StringProperty(name="User Category 3 Path",subtype='DIR_PATH',)
    userlib_pro1_path: StringProperty(name="Project Path",subtype='DIR_PATH',)
    
    categoryname: StringProperty(name="Name",description="Category of Geometry Nodegroups",default="Generators",
            #update=update_panel
            )
    
    categoryname2: StringProperty(name="Name",description="Category of Geometry Nodegroups",default="Transform",
            #update=update_panel
            )
    
    categoryname3: StringProperty(name="Name",description="Category of Geometry Nodegroups",default="Math",
            #update=update_panel
            )
    
    categorynamepro1: StringProperty(name="Name",description="Category of Geometry Nodegroups",default="my Project folder...",
            #update=update_panel
            )
    
    # SHOW sliding menu 1
    show_menu_list : BoolProperty(
        name="Need more ?",
        description="Show/Hide the Add Menu items",
        default=False
    )
    
    # SHOW sliding menu 2
    show_menu_list_projectpath : BoolProperty(
        name="Directories of Project Nodes Groups",
        description="Show/Hide the Add Menu items",
        default=False
    )

    def draw(self, context):
        layout = self.layout
        
        
        box = layout.box()
        box.label(text="Directories of User Geometry Nodes Groups")
        
        col = layout.column(align=True)
        split = col.split(factor=0.35)
        name_col = split.column()
        path_col = split.column()
        
        row = name_col.row(align=True)  # Padding
        row.label(text="Category Name")
        row = path_col.row(align=True)  # Padding
        row.label(text="Path")
        
        row = name_col.row(align=True)
        row.enabled = False
        row.prop(self, "categoryname", text="")
        row = path_col.row(align=True)
        row.prop(self, "userlib_cat1_path", text="")

            
        row = name_col.row(align=True)
        row.enabled = False
        row.prop(self, "categoryname2", text="")
        row = path_col.row(align=True)
        row.prop(self, "userlib_cat2_path", text="")

            
        row = name_col.row(align=True)
        row.enabled = False
        row.prop(self, "categoryname3", text="")
        row = path_col.row(align=True)
        row.prop(self, "userlib_cat3_path", text="")
                
        row = layout.row()
        row.label(text="INFO: The name cannot be changed at this time, not implemented yet (v1.3.2)",icon="INFO")

        
        # BLOC user paths
        #icon_1 = "TRIA_RIGHT" if not self.show_menu_list else "TRIA_DOWN"
        #box = layout.box()
        #box.prop(self, "show_menu_list", emboss=False, icon=icon_1)
        
        #if self.show_menu_list:           
            #col = box.column(align=True)
            #col.label(text="Text")
            

        
        # BLOC project path
        icon_2 = "TRIA_RIGHT" if not self.show_menu_list_projectpath else "TRIA_DOWN"
        box = layout.box()
        box.prop(self, "show_menu_list_projectpath", emboss=False, icon=icon_2)
        
        if self.show_menu_list_projectpath:
            row = box.row(align=True)
            row.prop(self, "userlib_pro1_path")
            row.separator()
            subrow = row.row()
            subrow.label(text="", icon="APPEND_BLEND")

        #for i, library in enumerate(paths.asset_libraries):
            #row = name_col.row()
            #row.alert = not library.name
            #row.prop(library, "name", text="")

            #row = path_col.row()
            #subrow = row.row()
            #subrow.alert = not library.path
            #subrow.prop(library, "path", text="")

            #row.operator("preferences.asset_library_remove", text="", icon='X', emboss=False).index = i

            row = box.row()
            row.enabled = False
            row.alignment = 'RIGHT'
            row.operator("preferences.asset_library_add", text="", icon='ADD', emboss=False)
        
        #row = box.row()
        #row.label(text="INFO",icon="INFO")
        #row = box.row()
        #row.label(text="Important! Paths are absolute! ",icon="LAYER_USED")


        #BLOC info
        #col = layout.column(align=True)
        #colbox = col.box()
        #colboxrow = colbox.row(align=True)
        #colboxrow.label(text="INFO",icon="INFO")
        #colboxrow = colbox.row()
        #colboxrow.label(text="Important! Paths are absolute! ",icon="LAYER_USED")


class NODE_OT_library_add(Operator):
    """Add a Node Library"""
    bl_idname = "node.library_add"
    bl_label = "Add Geometry node library"
    bl_description = "Add archived GN"
    bl_options = {'REGISTER', 'UNDO'}

    filepath: StringProperty(
        subtype='FILE_PATH',
    )
    group_name: StringProperty()

    def execute(self, context):
        gn_node_library_add(context, self.filepath, self.group_name, True, self.report)

        return {'FINISHED'}

    def invoke(self, context, event):
        gn_node_library_add(context, self.filepath, self.group_name, event.shift, self.report)

        return {'FINISHED'}


# ##################################
# Node Paths Cache
# ##################################

def gn_node_library_cache(context, *, reload=False):
    dirpath = gn_userlib_category1_path(context)

    if gn_node_library_cache._node_cache_path != dirpath:
        reload = True

    node_cache = gn_node_library_cache._node_cache
    if reload:
        node_cache = []
    if node_cache:
        return node_cache

    for fn in os.listdir(dirpath):
        if fn.endswith(".blend"):
            filepath = os.path.join(dirpath, fn)
            with bpy.data.libraries.load(filepath) as (data_from, data_to):
                for group_name in data_from.node_groups:
                    if not group_name.startswith("_"):
                        node_cache.append((filepath, group_name))

    gn_node_library_cache._node_cache = node_cache
    gn_node_library_cache._node_cache_path = dirpath

    return node_cache

gn_node_library_cache._node_cache = []
gn_node_library_cache._node_cache_path = ""

def gn_node_library_cat2_cache(context, *, reload=False):
    dirpath2 = gn_userlib_category2_path(context)

    if gn_node_library_cat2_cache._node_cache_path != dirpath2:
        reload = True

    node_cache = gn_node_library_cat2_cache._node_cache
    if reload:
        node_cache = []
    if node_cache:
        return node_cache

    for fn in os.listdir(dirpath2):
        if fn.endswith(".blend"):
            filepath = os.path.join(dirpath2, fn)
            with bpy.data.libraries.load(filepath) as (data_from, data_to):
                for group_name in data_from.node_groups:
                    if not group_name.startswith("_"):
                        node_cache.append((filepath, group_name))

    gn_node_library_cat2_cache._node_cache = node_cache
    gn_node_library_cat2_cache._node_cache_path = dirpath2

    return node_cache

gn_node_library_cat2_cache._node_cache = []
gn_node_library_cat2_cache._node_cache_path = ""

def gn_node_library_cat3_cache(context, *, reload=False):
    dirpath3 = gn_userlib_category3_path(context)

    if gn_node_library_cat3_cache._node_cache_path != dirpath3:
        reload = True

    node_cache = gn_node_library_cat3_cache._node_cache
    if reload:
        node_cache = []
    if node_cache:
        return node_cache

    for fn in os.listdir(dirpath3):
        if fn.endswith(".blend"):
            filepath = os.path.join(dirpath3, fn)
            with bpy.data.libraries.load(filepath) as (data_from, data_to):
                for group_name in data_from.node_groups:
                    if not group_name.startswith("_"):
                        node_cache.append((filepath, group_name))

    gn_node_library_cat3_cache._node_cache = node_cache
    gn_node_library_cat3_cache._node_cache_path = dirpath3

    return node_cache

gn_node_library_cat3_cache._node_cache = []
gn_node_library_cat3_cache._node_cache_path = ""

def gn_node_library_pro1_cache(context, *, reload=False):
    dirpathproject1 = gn_userlib_project__path_1(context)

    if gn_node_library_pro1_cache._node_cache_path != dirpathproject1:
        reload = True

    node_cache = gn_node_library_pro1_cache._node_cache
    if reload:
        node_cache = []
    if node_cache:
        return node_cache

    for fn in os.listdir(dirpathproject1):
        if fn.endswith(".blend"):
            filepath = os.path.join(dirpathproject1, fn)
            with bpy.data.libraries.load(filepath) as (data_from, data_to):
                for group_name in data_from.node_groups:
                    if not group_name.startswith("_"):
                        node_cache.append((filepath, group_name))

    gn_node_library_pro1_cache._node_cache = node_cache
    gn_node_library_pro1_cache._node_cache_path = dirpathproject1

    return node_cache

gn_node_library_pro1_cache._node_cache = []
gn_node_library_pro1_cache._node_cache_path = ""

# ##################################
# Menu
# ##################################

class NODE_MT_ButtonsSub_cat1(bpy.types.Menu):
    bl_label = 'Generators'
    bl_idname = 'node.library_submenu'
    bl_icon='NODETREE'

    def draw(self, context):
        layout = self.layout

        dirpath = gn_userlib_category1_path(context)
        if dirpath == "":
            layout.label(text="Set search dir in the addon-prefs")
            return
            
        try:
            node_items = gn_node_library_cache(context)
        except Exception as ex:
            node_items = ()
            layout.label(text=repr(ex), icon='ERROR')

        for filepath, group_name in node_items:
            props = layout.operator(
                NODE_OT_library_add.bl_idname,
                text=group_name,
            )
            props.filepath = filepath
            props.group_name = group_name

class NODE_MT_ButtonsSub_cat2(bpy.types.Menu):
    bl_label = 'Transform'
    bl_idname = 'node.library_submenu2'
    bl_icon='NODETREE'

    def draw(self, context):
        layout = self.layout

        dirpath2 = gn_userlib_category2_path(context)
        if dirpath2 == "":
            layout.label(text="Set search dir 2 in the addon-prefs")
            return
            
        try:
            node_items = gn_node_library_cat2_cache(context)
        except Exception as ex:
            node_items = ()
            layout.label(text=repr(ex), icon='ERROR')

        for filepath, group_name in node_items:
            props = layout.operator(
                NODE_OT_library_add.bl_idname,
                text=group_name,
            )
            props.filepath = filepath
            props.group_name = group_name

class NODE_MT_ButtonsSub_cat3(bpy.types.Menu):
    bl_label = 'Math'
    bl_idname = 'node.library_submenu3'
    bl_icon='NODETREE'

    def draw(self, context):
        layout = self.layout

        dirpath3 = gn_userlib_category3_path(context)
        if dirpath3 == "":
            layout.label(text="Set search dir 3 in the addon-prefs")
            return
            
        try:
            node_items = gn_node_library_cat3_cache(context)
        except Exception as ex:
            node_items = ()
            layout.label(text=repr(ex), icon='ERROR')

        for filepath, group_name in node_items:
            props = layout.operator(
                NODE_OT_library_add.bl_idname,
                text=group_name,
            )
            props.filepath = filepath
            props.group_name = group_name

class NODE_MT_ButtonsSub_pro1(bpy.types.Menu):
    bl_label = 'Project'
    bl_idname = 'node.library_submenupro1'
    bl_icon='NODETREE'

    def draw(self, context):
        layout = self.layout

        dirpathproject1 = gn_userlib_project__path_1(context)
        if dirpathproject1 == "":
            layout.label(text="Set search dir 3 in the addon-prefs")
            return
            
        try:
            node_items = gn_node_library_pro1_cache(context)
        except Exception as ex:
            node_items = ()
            layout.label(text=repr(ex), icon='ERROR')

        for filepath, group_name in node_items:
            props = layout.operator(
                NODE_OT_library_add.bl_idname,
                text=group_name,
            )
            props.filepath = filepath
            props.group_name = group_name

class NODE_MT_library_add(Menu):
    bl_label = "Node Library"

    def draw(self, context):
        layout = self.layout
        
        # Sub-menu > Category 1
        dirpath = gn_userlib_category1_path(context)
        if dirpath != "":
            layout.menu(NODE_MT_ButtonsSub_cat1.bl_idname, icon="NODETREE")
        else:
            layout.label(text="Set directory in the addon-prefs")
        
        # Sub-menu > Category 2
        dirpath2 = gn_userlib_category2_path(context)
        if dirpath2 != "":
            layout.menu(NODE_MT_ButtonsSub_cat2.bl_idname, icon="NODETREE")
            
        # Sub-menu > Category 3
        dirpath3 = gn_userlib_category3_path(context)
        if dirpath3 != "":
            layout.menu(NODE_MT_ButtonsSub_cat3.bl_idname, icon="NODETREE")
           
        layout.separator()
        
        # Sub-menu > Category 3
        dirpathproject1 = gn_userlib_project__path_1(context)
        if dirpathproject1 != "":
            layout.menu(NODE_MT_ButtonsSub_pro1.bl_idname, icon="NODETREE")

def add_gn_node_button(self, context):
    tnode = context.space_data
    # IF the window space type is Geometry Nodes
    if tnode.tree_type == 'GeometryNodeTree':
        self.layout.menu(
            NODE_MT_library_add.__name__,
            text="User Library",
            icon='ASSET_MANAGER',
    )


# ##################################
# REGISTRY
# ##################################

classes = (
    NODE_OT_library_add,
    NODE_MT_library_add,
    GnNodeLibraryPrefs,
    NODE_MT_ButtonsSub_cat1,
    NODE_MT_ButtonsSub_cat2,
    NODE_MT_ButtonsSub_cat3,
    NODE_MT_ButtonsSub_pro1,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.NODE_MT_add.append(add_gn_node_button)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

    bpy.types.NODE_MT_add.remove(add_gn_node_button)


if __name__ == "__main__":
    register()
