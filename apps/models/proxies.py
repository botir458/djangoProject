from apps.models.user import User


class ModeratorUser(User):
    class Meta:
        proxy =True
        verbose_name = 'Moderator'
        verbose_name_plural = 'Moderators'



class StudentUser(User):
    class Meta:
        proxy =True
        verbose_name = 'Jobs'
        verbose_name_plural = 'Jobs'

class TeacherUser(User):
    class Meta:
        proxy =True
        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers'

class AdminUser(User):
    class Meta:
        proxy =True
        verbose_name = 'Admin'
        verbose_name_plural = 'Admins'

