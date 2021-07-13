# Panorama

## Functions

## Exec

### Parameters:

| Name | Type | Description | Required |
| :--- | :--- | :--- | :--- |
| code | string | Javascript code | + |
| Panel | string | Panorama Panel | - |

### Return:

| Name | Type | Description |
| :--- | :--- | :--- |
| result | function | - |

```lua
local get_my_steamid = Panorama.LoadString([[
    return MyPersonaAPI.GetXuid()
]])

local my_steam = get_my_steamid()

print("LoadString", my_steam) -- returns 765xxxx..
```

## Open

### Return:

| Name | Type | Description |
| :--- | :--- | :--- |
| result | PanoramaHandle | Panorama opened handle |

```lua
local panorama_handle = Panorama.Open()
local my_steam_from_handle = panorama_handle.MyPersonaAPI.GetXuid()

print("Open", my_steam_from_handle) -- returns 765xxxx..
```
