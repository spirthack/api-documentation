# Cheat

## ESP API

{% hint style="info" %}
You can create your own ESP elements. More info can be found [here](ESP.md).
{% endhint %}

## Menu API

{% hint style="info" %}
You can create your menu elements. More info can be found [here](Menu.md).
{% endhint %}

## Functions

## RegisterCallback

### Parameters:

| Name | Type | Description |
| :--- | :--- | :--- |
| event_name | string | Event names |
| callback | function | Callback |

{% hint style="info" %}
You can view callbacks list [here](../other/callbacks.md).
{% endhint %}

```lua
Cheat.RegisterCallback("draw", function()
    Render.Text("Hello world, it's me", Vector2.new(10.0, 15.0), Color.new(1.0, 1.0, 1.0), 16)
end)
```

## FireBullet

### Simulates bullet with wall penetrating

### Parameters:

| Name | Type | Description |
| :--- | :--- | :--- |
| attacker | C_BasePlayer | Attacker |
| start | Vector | Simluation start pos |
| end | Vector | Simluation end pos |

### Return value:

| Name | Type |
| :--- | :--- |
| Fire Bullet Info | firebullet_t |

```lua
local trace = Cheat.FireBullet(player, Vector.new(0.0, 0.0, 0.0), Vector.new(1.0, 1.0, 1.0))
print(trace.damage)
```

## AngleToForward

### Parameters:

| Name | Type | Description |
| :--- | :--- | :--- |
| ang | QAngle | Input angle |

### Return value:

| Name | Type | Description |
| :--- | :--- | :--- |
| vec | Vector | Output vector |

```lua
local vec = Cheat.AngleToForward(QAngle.new())
```

## VectorToAngle

### Parameters:

| Name | Type | Description |
| :--- | :--- | :--- |
| vec | Vector | Input vector |

### Return value:

| Name | Type | Description |
| :--- | :--- | :--- |
| ang | QAngle | Output angle |

```lua
local ang = Cheat.VectorToAngle(Vector.new(100, 100, 100))
```

## IsMenuVisible

### Return value:

| Name | Type | Description |
| :--- | :--- | :--- |
| value | bool | Is menu opened or not |

```lua
local is_visible = Cheat.IsMenuVisible()
```

## GetMousePos

### Return value:

| Name | Type | Description |
| :--- | :--- | :--- |
| value | Vector2 | Mouse position on screen |

```lua
local mouse_pos = Cheat.GetMousePos()
```

## IsKeyDown

### Parameters:

| Name | Type | Description |
| :--- | :--- | :--- |
| key | int | Virtual key code |

### Return value:

| Name | Type | Description |
| :--- | :--- | :--- |
| value | bool | Is key down |

{% hint style="info" %}
You can find all virtual keys [here](https://docs.microsoft.com/en-us/windows/win32/inputdev/virtual-key-codes)
{% endhint %}

```lua
local is_key_pressed = Cheat.IsKeyDown(0x1)
```

## GetCheatUserName

### Return value:

| Name | Type | Description |
| :--- | :--- | :--- |
| name | string | Neverlose's account username |

```lua
local username = Cheat.GetCheatUserName()
```

## GetBinds

### Return value:

| Name | Type | Description |
| :--- | :--- | :--- |
| binds | table (`ActiveBind`s array)| Binds |

```lua
local binds = Cheat.GetBinds()
print("Name", "isActive", "Value")
for i = 1, #binds do
    print(binds[i]:GetName(), binds[i]:IsActive(), binds[i]:GetValue())
end
```

## AddEvent

### Parameters:

| Name | Type | Description |
| :--- | :--- | :--- |
| name | string | Event name |

```lua
Cheat.AddEvent("Greetings from neverlose.cc!")
```

## AddNotify

### Parameters:

| Name | Type | Description |
| :--- | :--- | :--- |
| title | string | Notification title |
| name | string | Notification name |

```lua
Cheat.AddNotify("neverlose.cc", "Greetings from elleqt!")
```
