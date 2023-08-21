class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

 

    def add_group(self, group):
        self.groups.append(group)

 

    def add_user(self, user):
        self.users.append(user)

 

    def get_groups(self):
        return self.groups

 

    def get_users(self):
        return self.users

 

    def get_name(self):
        return self.name

 

 

parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

 

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

 

child.add_group(sub_child)
parent.add_group(child)

 

 

def is_user_in_group(user, group):
    if group != None:
        if user in group.get_users():
            return True
        
        for sub_group in group.get_groups():
            return is_user_in_group(user, sub_group)

    return False

 

## Add your own test cases: include at least three test cases
## and two of them must include edge cases, such as null, empty or very large values

 

## Test Case 1 - user exist in both parent group and child group
assert is_user_in_group("sub_child_user", child) == True
assert is_user_in_group("sub_child_user", parent) == True

 

## Test Case 2 - user exist in only parent group
second_child = Group('secondchild')
parent.add_group(second_child)
assert is_user_in_group("sub_child_user", second_child) == False
assert is_user_in_group("sub_child_user", parent) == True

 

## Test Case 3 - - user not exist in both parent group or child group
assert is_user_in_group("sub_child_user", None) == False
assert is_user_in_group("", parent) == False