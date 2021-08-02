from Pr_Ad import Admin,Privileges
from User import User
admin=Admin('Peter','Jiang')
admin.privilege.privileges=['can add post','can delete post','can ban user']
admin.privilege.show_privileges()
