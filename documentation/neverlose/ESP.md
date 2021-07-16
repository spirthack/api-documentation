# ESP

## Functions

## CustomText

### Parameters:

| Name | Type | Description |
| :--- | :--- | :--- |
| name | string | Element name |
| classname | string | Class name |
| preview | string | Value on ESP Preview |
| callback | function | Callback function |

{% hint style="info" %}
Possible class names:

- **enemies**
- **mates**
- **local**
- **weapon**
- **grenade**
  {% endhint %}

### Callback:

1 argument passed to callback - [C_BaseEntity](../classes/C_BaseEntity.md).

In callback you can return 1 argument.

| Name | Type | Description | Required |
| :--- | :--- | :--- | :--- |
| text | string | Text to draw | + |

```lua
ESP.CustomText("Test", "enemies", "preview", function(ent)
    return "Testing"
end)
```

## CustomBar

### Parameters:

| Name | Type | Description |
| :--- | :--- | :--- |
| name | string | Element name |
| classname | string | Class name |
| callback | function | Callback function |

{% hint style="info" %}
Possible class names:

- **enemies**
- **mates**
- **local**
- **weapon**
- **grenade**
  {% endhint %}

### Callback:

1 argument passed to callback - [C_BaseEntity](../classes/C_BaseEntity.md).

In callback you can return 1 argument

| Name | Type | Description | Required |
| :--- | :--- | :--- | :--- |
| value | int | Bar amount (0-100) | + |

```lua
ESP.CustomBar("Test", "enemies", function(ent)
    return 90
end)
```
