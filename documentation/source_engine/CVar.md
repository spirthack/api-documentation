# CVar

## Functions

## FindVar

### Parameters:

| Name | Type | Description |
| :--- | :--- | :--- |
| name | string | ConVar name |

### Return value:

| Name | Type | Description |
| :--- | :--- | :--- |
| value | ConVar\* | ConVar pointer |

```lua
local cheats = CVar.FindVar("sv_cheats")
```

## RegisterConVar

### Parameters:

| Name | Type | Description | Required |
| :--- | :--- | :--- | :--- |
| name | string | Console var name | + |
| value | string | Console var default value | + |
| flags | int | [Convar flags](../other/source_engine_enums.md#cvar-flags) | + |
| description | string | Console var description | + |
| callback | function | Callback | - |

### Return value:

| Name | Type | Description |
| :--- | :--- | :--- |
| value | ConVar | Registered console var instance |

```lua
local cvar = CVar.RegisterConVar('meme_var', '1', 8, 'Testing stuff', function(cvar, old, new)
    print('meme_var value was changed from ' .. old .. ' to ' .. new)
end)
print(cvar:GetString())
```

## RegisterConCommand

### Parameters:

| Name | Type | Description | Required |
| :--- | :--- | :--- | :--- |
| name | string | Console command name | + |
| flags | int | [Convar flags](../other/source_engine_enums.md#cvar-flags) | + |
| description | string | Console command description | + |
| callback | function | Callback | + |

### Return value:

| Name | Type | Description |
| :--- | :--- | :--- |
| value | ConVar | Registered console command instance |

```lua
local cmd = CVar.RegisterConCommand('meme_cmd', 8, 'Testing stuff', function(cvar)
    print("it's wednesday, my dudes")
end)
```