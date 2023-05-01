from src.library import library
from src.library.data.library import library_data


class SystemValidity:

    @staticmethod
    def validate(pre_system_data, next_system_data):
        pass


class SystemState:

    def __init__(self, system_data):
        self._system_data = system_data
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


class System:

    def __init__(self):
        self._system_state = SystemState(library_data)

    def add_member(self, member):
        pre_system_data = self._system_state.get()
        next_system_data = library.add_member(pre_system_data, member)
        self._system_state.commit(next_system_data)
