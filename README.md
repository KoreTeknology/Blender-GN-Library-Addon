# Blender-GN-Library-Addon
A simple script addon to access your personal Geometry nodes presets, from the Add menu.

<img src="https://img.shields.io/badge/Blender-3.1.0-green" /> <img src="https://img.shields.io/badge/Python-3.7-blue" />

```python
bl_info = {
    "name": "Geometry Node User Libraries",
    "description": "Geometry Nodes User Library with paths and name settings",
    "author": "uriel Deveaud (inspired by node_presets.py)",
    "version": (1, 3),
    "blender": (3, 0, 0),
    "location": "Geometry Node Editor > Add > User Library",
    "description": "Add node groups directly from the Geometry Nodes Add menu",
    "warning": "",
    "category": "Node",
}
```

<img src="https://github.com/KoreTeknology/Blender-GN-Library-Addon/blob/main/media/gnlib_preview_1.jpg" width=100%>

## Features
- [x] Custom user menus in Geometry Nodes Editor context window
- [x] Read .blend files from folder path
- [x] Extract exclusively nodegroups from Geometry nodesgroups type
- [x] Up to 3 user categories can be set with indexed sub-menu 
- [x] A single project category is added for convenience
- [x] Add Path setting in preferences
- [ ] Add Name setting in preferences (in progress)

---

## History

> **Release 1.3** - [07/04/2022]: Re-Define Project library + user libraries

> **Release 1.2** - [06/04/2022]: Clearing addon, ONLY geometry nodes context

> **Release 1.0** - [04/04/2022]: Add addon preferences to set the paths

> **Release 0.5** - [02/04/2022]: Rewriting of the complete code structure, categories, paths

> **Release 0.1** "First Release" - [Date: 015/03/2022]: Development and analyse "node_presets.py

---

## Infos

* Author: **Uriel Deveaud** - [Kore Teknology](https://github.com/KoreTeknology)
* License: This project is released under the GPL License.


## Acknowledgments

* This work is dedicated to all Blender users ;)
* i will try to keep all types of codes as clear as possible using syntax highlighting and line referencing
