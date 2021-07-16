# Menu Elements

> Author: [@elleqt](https://github.com/elleqt)
>
> Name: `Menu Elements`
>
> Description: `Custom menu element creation`

```lua
local our_checkbox      = Menu.Switch("neverlose.cc", "Toggle me!", false)           --    Create a new checkbox in our script's tab
local our_slider        = Menu.SliderInt("neverlose.cc", "Slide me!", 50, 0, 100)      --    Create a new slider in our script's tab

local ui_callback       = function()
    local new_state     = our_checkbox:GetBool()    --  The new value of our checkbox

    print("Our new value is "..tostring(our_checkbox:GetBool()))

    our_slider:SetVisible(new_state)                --  If our checkbox is enabled, the slider will be visible
                                                    --  If our checkbox is disabled, the slider won't be visible
end

ui_callback()   --  Run the change callback once to set the slider's visibility at script start

our_checkbox:RegisterCallback(ui_callback)  -- Set the menu item change callback on our checkbox
--  Now the callback will be ran whenever the item changes its value
```
