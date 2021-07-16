# Doubletap Speed

> Author: [@elleqt](https://github.com/elleqt)
>
> Name: `Doubletap speed`
>
> Description: `Doubletap speed`

```lua
local speed        = Menu.SliderInt("Doubletap", "Speed", 13, 10, 16)      --    Create a new slider in our script's tab

local ui_callback       = function()

    Exploits.OverrideDoubleTapSpeed(speed:GetInt()) -- Set new double tap speed

end


speed:RegisterCallback(ui_callback) -- Set the menu item change callback on our checkbox
--  Now the callback will be ran whenever the item changes its value
```
