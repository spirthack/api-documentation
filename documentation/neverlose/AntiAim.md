# AntiAim

{% hint style="info" %}
Override\* functions can be called only from pre-createmove [callbacks](../other/callbacks.md) (`pre_prediction`, `prediction`).
{% endhint %}

## Functions

## OverrideInverter

### Parameters:

| Name | Type | Description |
| :--- | :--- | :--- |
| value | bool | A new value for inverter |

```lua
AntiAim.OverrideInverter(false)
```

## OverrideLimit

### Parameters:

| Name | Type | Description |
| :--- | :--- | :--- |
| value | float | A new desync limit value (0 - 58) |

```lua
AntiAim.OverrideLimit(30)
```

## OverrideYawOffset

### Parameters:

| Name | Type | Description |
| :--- | :--- | :--- |
| value | float | A new yaw offset value (-180 - 180) |

```lua
AntiAim.OverrideYawOffset(90)
```

## OverrideLBYOffset

### Parameters:

| Name | Type | Description |
| :--- | :--- | :--- |
| value | float | A new lby offset value (-58 - 58) |

```lua
AntiAim.OverrideLBYOffset(58)
```

## OverridePitch

### Parameters:

| Name | Type | Description |
| :--- | :--- | :--- |
| value | float | A new pitch value |

```lua
AntiAim.OverridePitch(90) -- UP
```

## GetInverterState

### Return value:

| Type | Description |
| :--- | :--- |
| bool | Current inverter state |

```lua
local inverter_state = AntiAim.GetInverterState()
```

## GetMinDesyncDelta

### Return value:

| Type | Description |
| :--- | :--- |
| float | Minimal desync delta |

```lua
local min_desync_delta = AntiAim.GetMinDesyncDelta()
```

## GetMaxDesyncDelta

### Return value:

| Type | Description |
| :--- | :--- |
| float | Max desync delta |

```lua
local max_desync_delta = AntiAim.GetMaxDesyncDelta()
```

## GetFakeRotation

### Return value:

| Type | Description |
| :--- | :--- |
| float | Fake rotation |

```lua
local desync_rotation = AntiAim.GetFakeRotation()
```

## OverrideDesyncOnShot

### Parameters:

| Type | Description |
| :--- | :--- |
| int | 0 - disable override, 1 - left, 2 - right, 3 - overlap on shot with fake, 4 - opposite to fake |

```lua
AntiAim.OverrideDesyncOnShot(4)
```

## GetCurrentRealRotation

### Return value:

| Type | Description |
| :--- | :--- |
| float | Real rotation |

```lua
local real_rotation = AntiAim.GetCurrentRealRotation()
```
