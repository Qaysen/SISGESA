def user_in_group(user,group):
	return 1 if user.groups.filter(name=group).exists() else 0