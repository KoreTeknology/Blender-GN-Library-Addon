# Geometry Nodes User Library Addon for Blender
A simple script addon for Blender 3.1+ to access your **personal Geometry nodes presets**, from the Add menu. It includes **several library paths and categories settings** in the addon preferences panel. **"Quick access to your geometry nodegroups using the shortcut MAJ+A"**, located on top of your geometry node editor area.

## Acknowledgments

> *If you are using the node-presets.py addon, you may have found out that it includes all types of nodes in only one single category. The asset manager is a cool option too, but as it doesnt require a parent object, an image preview or any tags, why not getting our favorite geometry node presets directly from the Geometry nodes editor itself?! ;)*

<img src="https://img.shields.io/badge/Blender-3.1.0-green" /> <img src="https://img.shields.io/badge/Python-3.7-blue" /> <img src="https://img.shields.io/badge/Addon-1.4.1-orange" />

<img src="https://github.com/KoreTeknology/Blender-GN-Library-Addon/blob/main/media/gnlib_preview_web_141.jpg" width=100%>

## Installation

1. Download the [Geometry Nodes User Library Addon](https://github.com/KoreTeknology/Blender-GN-Library-Addon/blob/main/GN_Library_Addon_v141.py) (Latest Release)
2. If you decide to download the full repository (.zip), unzip the Addon folder first!
3. Go to Blender, Preferences > Addons
4. Click on "Install" to select the python file "GN_Library_Addon_xxx.py" (xxx is the version number)
5. When it is done, you can activate the addon!
6. Set your first "path to library folder" in the addon-preferences panel
7. Go to the Geometry Nodes Editor, and open the Add Menu, enjoy!

## Updates Instructions

```diff
- This addon doesn´t include an integrated update system :(
+ If you want to update this addon, uninstall the previous version first! 
```

## Features
- [x] Custom user menus **ONLY in Geometry Nodes Editor** context window
- [x] Read .blend files **from custom folder path**
- [x] Show **ONLY nodegroups from Geometry nodesgroups type**
- [x] Up to **3 user categories** can be set with indexed sub-menu 
- [x] A single **project category** is added for convenience
- [x] **Category Paths settings** in addon-preferences
- [x] **Category Name settings** in addon-preferences
- [x] User library **structure and contents samples**

## Settings

<img src="https://github.com/KoreTeknology/Blender-GN-Library-Addon/blob/main/media/geonode_addon_web_prefs_141b.jpg" width=100%>

## What´s Next?
- [x] Append/link options (Y)
- [ ] Add infinite categories?
- [x] more libraries? 3+1? or Projects Path must be re-designed?
- [x] more samples?


## **Proposal for Release 1.4.5 - 05/22:**

<ul>
  <li><b>Update Addon settings</b>
    <ul>
      <li>add INIT file for good practices</li>
      <li>GUI design: Add "Link" (/Append) button for each path</li>
      <li>General User Library Paths (3/type)</li>
      <li>Structural design change: Project independant setup (2)</li>
      <li>Final Samples Library</li>
      <li>Add Panel(N) in 3D View for Project path and buttons(Import Presets)</li>
    </ul>
  </li>
  <li><b>Update Geometry nodegroups</b>
    <ul>
      <li>Code Cleaning/comments</li>
    </ul>
  </li>
</ul>

```diff
+ NOTE: Project needs to include one main folderpath, and maybe a temp folder?! 
```

## **Proposal for Release 1.5.0 - 06/22:**

<ul>
  <li><b>Add User Libraries from path</b> (ONLY in 3D View area)
    <ul>
      <li>pre-made Scenes</li>
      <li>Images as Plane (References)</li>
      <li>pre-made Objects(/per typeof: mesh, Curve,...?)</li>
    </ul>
  </li>
</ul>

- **Add Code Snippets** in Text Editor (merged with my other script:([Snippets Library Addon](https://github.com/KoreTeknology/python-codes-library-addon-for-Blender))

```diff
- NOTE: Add tutorials on workflows?! 
```

## **Proposal for Release 1.6.0 - 07/22:**

<ul>
  <li><b>Add Shader nodegroups</b> (ONLY in Shading nodes area)
    <ul>
      <li>Basic Materials</li>
      <li>Advanced Materials</li>
      <li>User Templates</li>
    </ul>
  </li>
  <li><b>Add Compositor nodegroups</b> (ONLY in compositor nodes area)
    <ul>
      <li>Pre-made filters</li>
      <li>Pre-configured Ouputs</li>
      <li>Project Templates</li>
    </ul>
  </li>
  <li><b>Add Texture nodegroups</b> (Only in texture nodes area)
    <ul>
      <li>User Favorite Images</li>
      <li>Color Correction Presets</li>
    </ul>
  </li>
</ul>

> ### Implementation Strategy
>
> - Each type of user favorites will come in its own window area.
> - Basic user libraries and Projects ones parameters (path).
>
>  *Tutorial must be ready* for the next release  **1.5 A1**.

---

## History

> **Release 1.4.1** - [09/04/2022]: Fix custom name update in UI

> **Release 1.4.0** - [09/04/2022]: Fix UI, add icons, set custom name in preferences

> **Release 1.3.2** - [08/04/2022]: Re-Draw Addon preferences, add sample files

> **Release 1.3.1** - [07/04/2022]: Re-Define Project library + user libraries

> **Release 1.2.1** - [06/04/2022]: Clearing addon, ONLY geometry nodes context

> **Release 1.0.1** - [04/04/2022]: Add addon preferences to set the paths

> **Release 0.5.1** - [02/04/2022]: Rewriting of the complete code structure, categories, paths

> **Release 0.1.1** "First Release" - [Date: 015/03/2022]: Development and analyse "node_presets.py

---

## Infos

* Author: **Uriel Deveaud** - [Kore Teknology](https://github.com/KoreTeknology) 

<img src="https://img.shields.io/badge/CG Art-1995-red" /> <img src="https://img.shields.io/badge/3D Blender-2002-red" /> <img src="https://img.shields.io/badge/Python Dev-2005-red" /> <img src="https://img.shields.io/badge/3D Trainer-2008-red" /> <img src="https://img.shields.io/badge/Coding Trainer-2010-red" /> <img src="https://img.shields.io/badge/GE-2015-darkorange" /> <img src="https://img.shields.io/badge/VR-2017-darkorange" />

* License: This project is released under the GPL License.
* This work is dedicated to all Blender users ;)
