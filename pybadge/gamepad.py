import keypad as _keypad

ShiftRegisterKeys = _keypad.ShiftRegisterKeys
Event = _keypad.Event


class GamepadDriver:
    def __init__(self, keypad: ShiftRegisterKeys):
        self.__event = Event()
        self.__keypad = keypad

    def next_event(self) -> Event or None:
        """

        :return:
        """
        if self.__keypad.events.get_into(self.__event):
            return self.__event
        else:
            return None


class GamepadEventHandler:
    def on_b_pressed(self):
        """The 'B' button was pressed."""
        pass

    def on_b_released(self):
        """The 'B' button was released."""
        pass

    def on_a_pressed(self):
        """The 'A' button was pressed."""
        pass

    def on_a_released(self):
        """The 'A' button was released."""
        pass

    def on_start_pressed(self):
        """The 'Start' button was pressed."""
        pass

    def on_start_released(self):
        """The 'Start' button was released."""
        pass

    def on_select_pressed(self):
        """The 'Select' button was pressed."""
        pass

    def on_select_released(self):
        """The 'Select' button was released."""
        pass

    def on_right_pressed(self):
        """The 'Right' button was pressed."""
        pass

    def on_right_released(self):
        """The 'Right' button was released."""
        pass

    def on_down_pressed(self):
        """The 'Down' button was pressed."""
        pass

    def on_down_released(self):
        """The 'Down' button was released."""
        pass

    def on_up_pressed(self):
        """The 'Up' button was pressed."""
        pass

    def on_up_released(self):
        """The 'Up' button was released."""
        pass

    def on_left_pressed(self):
        """The 'Left' button was pressed."""
        pass

    def on_left_released(self):
        """The 'Left' button was released."""
        pass

    def on_event_received(self, event: Event):
        key_number = event.key_number
        is_pressed = event.pressed

        if key_number == 0:
            if is_pressed:
                self.on_b_pressed()
            else:
                self.on_b_released()
        elif key_number == 1:
            if is_pressed:
                self.on_a_pressed()
            else:
                self.on_a_released()
        elif key_number == 2:
            if is_pressed:
                self.on_start_pressed()
            else:
                self.on_start_released()
        elif key_number == 3:
            if is_pressed:
                self.on_select_pressed()
            else:
                self.on_select_released()
        elif key_number == 4:
            if is_pressed:
                self.on_right_pressed()
            else:
                self.on_right_released()
        elif key_number == 5:
            if is_pressed:
                self.on_down_pressed()
            else:
                self.on_down_released()
        elif key_number == 6:
            if is_pressed:
                self.on_up_pressed()
            else:
                self.on_up_released()
        else:
            if is_pressed:
                self.on_left_pressed()
            else:
                self.on_left_released()
