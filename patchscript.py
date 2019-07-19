'''
import patch
p  = patch.fromflie('kernel/drivers/gpu/drm/vkms/v2-drm-vkms-Add-overlay-plane-support.patch')
p.apply()
'''


import os
import subprocess

#patch_path = "~/kernel/drivers/gpu/drm/vkms/v2-drm-vkms-Add-overlay-plane-support.patch"
#cmd = "patch <kernel/drivers/gpu/drm/vkms/v2-drm-vkms-Add-overlay-plane-support.patch"

cmd = "perl kernel/scripts/checkpatch.pl -f kernel/drivers/gpu/drm/vkms/*"
returned_value = subprocess.call(cmd, shell=True)  # returns the exit code in unix
print('returned value:', returned_value)

cmd2  ="make C=2  kernel/drivers/gpu/drm/vkms/ "
returned_value2 = subprocess.call(cmd2, shell=True)
print('returned value:', returned_value2)


cmd3 ="clang kernel/scripts/checkpatch.pl -f kernel/drivers/gpu/drm/vkms/*"
returned_value3 = subprocess.call(cmd3, shell=True)
print('returned value:', returned_value3)


cmd4 ="valgrind --leak-check=yes  kernel/drivers/gpu/drm/vkms/*"
returned_value4 = subprocess.call(cmd4, shell=True)
print('returned value:', returned_value4)
