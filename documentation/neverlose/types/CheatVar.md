# CheatVar

{% hint style="info" %}
You can access `CheatVar` instance through [Menu.FindVar](../Menu.md)
{% endhint %}

## Functions

## Get

### Return value:

| Name | Type | Description |
| :--- | :--- | :--- |
| value | depends on menu item | CheatVar value |

```lua
local val = var:Get()
```

## Set

### Parameters:

| Name | Type | Description |
| :--- | :--- | :--- |
| value | depends on menu item | CheatVar value |

```lua
local val = var:Set(Color.new(1.0, 1.0, 1.0, 1.0))
```

## GetColor

### Return value:

| Name | Type | Description |
| :--- | :--- | :--- |
| value | Color | CheatVar value as Color |

```lua
local val = var:GetColor()
```

## SetColor

### Parameters:

| Name | Type | Description | Required |
| :--- | :--- | :--- | :--- |
| value | Color | New Color value | + |

```lua
var:SetColor(Color.new(1, 1, 1, 1))
```

## RegisterCallback

### Parameters:

| Name | Type | Description | Required |
| :--- | :--- | :--- | :--- |
| value | function | Callback | + |

```lua
var:RegisterCallback(function()
    print("callback!")
end)
```

## SetVisible

### Parameters:

| Name | Type | Description | Required |
| :--- | :--- | :--- | :--- |
| value | bool | Item visibility | + |

```lua
var:SetVisible(false)
```

## DestroyItem

{% hint style="warning" %}
DestroyItem was previously incorrectly listed here. It has been moved to to the [Menu API](../other/menuapi.md#destroyitem)
{% endhint %}

## SetTooltip

### Parameters:

| Name | Type | Description | Required |
| :--- | :--- | :--- | :--- |
| value | string | Tooltip content | + |

```lua
var:SetTooltip("Tooltip")
```

## GetName

### Return value:

| Name | Type | Description |
| :--- | :--- | :--- |
| Cheatvar name | string | Returns control's name |

```lua
local bodyAim = Menu.FindVar("Aimbot", "Ragebot", "Misc", "Body Aim")
local name = bodyAim:GetName()

print(name)
```

## UpdateList

### Parameters:

| Name | Type | Description | Required |
| :--- | :--- | :--- | :--- |
| new combo items | table | Combo Items | + |

```lua
local combo = Menu.Combo("Neverlose", "Combo", {"Element 1", "Element 2", "Element 3"}, 0, "Tooltip")
Menu.Button("neverlose", "update"):RegisterCallback(function()
    combo:UpdateList({"el1", "el2"})
end)
```

## GetList

### Return value:

| Name | Type | Description |
| :--- | :--- | :--- |
| Combo elements | table | Returns all elements in combo |

```lua
local bodyAim = Menu.FindVar("Aimbot", "Ragebot", "Misc", "Body Aim")
local list = bodyAim:GetList()

for _, item in ipairs(list) do
  print(item)
end
```
