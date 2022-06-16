import os

import xr

# Turn on extra debugging messages in the OpenXR Loader
# os.environ["XR_LOADER_DEBUG"] = "all"
# os.environ["LD_BIND_NOW"] = "1"

foo_layer = xr.SteamVrLinuxDestroyInstanceLayer()

print(os.environ["XR_API_LAYER_PATH"])
print(*xr.enumerate_api_layer_properties())
print(foo_layer.name)

# 1) Setting/clearing the environment from python does affect the layers
os.environ.pop("XR_API_LAYER_PATH", None)
start_count = len(xr.enumerate_api_layer_properties())
print(start_count)

print(*xr.enumerate_api_layer_properties())
xr.expose_packaged_api_layers()

# 2) The choice of layers can be specified in the instance constructor
instance_handle = xr.create_instance(create_info=xr.InstanceCreateInfo(
    enabled_api_layer_names=[
        foo_layer.name,
        # xr.api_layer.XR_APILAYER_LUNARG_core_validation_NAME,
        # xr.api_layer.XR_APILAYER_LUNARG_api_dump_NAME,
    ],))

xr.destroy_instance(instance_handle)
