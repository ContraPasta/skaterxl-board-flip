#!/usr/bin/env python
# -------------------------------------------------------------------------------------
#
# This file is a Python plug-in for GIMP.
#
# It can be executed by selecting the menu option: 'Filters/Test/Invert layer'
# or by writing the following lines in the Python console (that can be opened with the
# menu option 'Filters/Python-Fu/Console'):


from gimpfu import *

def flip_board(image, layer) :
    ''' flips a SkaterXL board.
    
    Parameters:
    image : image The current image.
    layer : layer The layer of the image that is selected.
    '''

    image = gimp.image_list()[0]
    pdb.gimp_image_select_rectangle(image, 2, 0, 677, 2048, 511)
    id = pdb.gimp_image_get_selection(image)
    pdb.gimp_edit_copy_visible(image)
    layer1 = pdb.gimp_image_get_active_layer(image)
    new_layer = pdb.gimp_edit_paste(layer1, 0)
    floating_sel = pdb.gimp_image_get_floating_sel(image)
    pdb.gimp_floating_sel_to_layer(floating_sel)
    layer2 = pdb.gimp_image_get_active_layer(image)
    pdb.gimp_item_transform_flip_simple(layer2, 0, 1, 0)
    pdb.gimp_item_transform_flip_simple(layer2, 1, 1, 0)

register(
    "python_skaterxl_board_flipper",
    "Flip Board",
    "Flips SkaterXL Board",
    "ButtsMcButts",
    "Open source (BSD 3-clause license)",
    "2013",
    "<Image>/Filters/Test/SkaterXL Flip Board",
    "*",
    [],
    [],
    flip_board)

main()
