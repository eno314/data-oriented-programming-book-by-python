from src import system
from src.library.data.library import library_data
from src.library.data.user_management import user_management_data
from src.system import SystemState


def test_add_member():
    system_state = SystemState()
    system_state.commit(None, library_data)

    new_member = {
        "email": "new@hoge.com",
        "encryptedPassword": "dGVzdAo=",
    }
    system.add_member(system_state, new_member)

    expected = {
        "catalog": library_data["catalog"],
        "user_management": {
            "librariansByEmail": user_management_data["librariansByEmail"],
            "membersByEmail": {
                "samantha@hoge.com": user_management_data["membersByEmail"]["samantha@hoge.com"],
                "new@hoge.com": new_member,
            }
        }
    }
    assert expected == system_state.get()
