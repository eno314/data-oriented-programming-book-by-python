from src.ch1.member import Member
from src.ch1.user_with_block_member_right import UserWithBlockMemberRight


class SuperMember(Member, UserWithBlockMemberRight):
    pass
