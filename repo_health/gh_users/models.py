from django.db import models as m


class GhUser(m.Model):
    login = m.CharField(max_length=255, unique=True)
    name = m.CharField(max_length=255)
    company = m.CharField(max_length=255, null=True)
    email = m.CharField(max_length=255, null=True)
    created_at = m.DateTimeField()
    ext_ref_id = m.CharField(max_length=24, default='0')
    type = m.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name="GitHub User"
        db_table = 'users'
    
# DDL output from MySQL database
# CREATE TABLE `users` (
#   `id` int(11) NOT NULL AUTO_INCREMENT,
#   `login` varchar(255) NOT NULL,
#   `name` varchar(255) DEFAULT NULL,
#   `company` varchar(255) DEFAULT NULL,
#   `location` varchar(255) DEFAULT NULL,
#   `email` varchar(255) DEFAULT NULL,
#   `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
#   `ext_ref_id` varchar(24) NOT NULL DEFAULT '0',
#   `type` varchar(255) NOT NULL DEFAULT 'USR',
#   PRIMARY KEY (`id`),
#   UNIQUE KEY `login` (`login`)
# ) ENGINE=InnoDB AUTO_INCREMENT=507757 DEFAULT CHARSET=utf8