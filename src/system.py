from src.library import library


class SystemValidity:

    @staticmethod
    def validate(pre_system_data, next_system_data):
        # TODO
        return True


class SystemState:

    def __init__(self):
        self._system_data = None
        self._previous_system_data = None

    def get(self):
        return self._system_data

    def commit(self, previous_system_data, next_system_data):
        system_data_before_update = self._system_data
        if not SystemValidity.validate(previous_system_data, next_system_data):
            raise SystemError("The system data to be committed is not valid!")
        self._system_data = next_system_data
        self._previous_system_data = system_data_before_update

    def undo_last_mutate(self):
        self._system_data = self._previous_system_data


def add_member(system_state, member):
    pre_system_data = system_state.get()
    next_system_data = library.add_member(pre_system_data, member)
    system_state.commit(pre_system_data, next_system_data)
