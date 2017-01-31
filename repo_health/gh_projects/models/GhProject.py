'''
Hold the models for Github projects.
'''


from django.db import models as m

class GhProject(m.Model):
    url = m.CharField(max_length=255, null=True)
    owner = m.ForeignKey('gh_users.GhUser', null=True)
    name = m.CharField(max_length=255)
    description = m.CharField(max_length=255)
    language = m.CharField(max_length=255)
    created_at = m.DateField()


# DDL pulled from MySQl
# CREATE TABLE `projects` (
#   `id` int(11) NOT NULL AUTO_INCREMENT,
#   `url` varchar(255) DEFAULT NULL,
#   `owner_id` int(11) DEFAULT NULL,
#   `name` varchar(255) NOT NULL,
#   `description` varchar(255) DEFAULT NULL,
#   `language` varchar(255) DEFAULT NULL,
#   `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
#   `ext_ref_id` varchar(24) NOT NULL DEFAULT '0',
#   `forked_from` int(11) DEFAULT NULL,
#   `deleted` tinyint(1) NOT NULL DEFAULT '0',
#   PRIMARY KEY (`id`),
#   UNIQUE KEY `name` (`name`,`owner_id`),
#   KEY `owner_id` (`owner_id`),
#   KEY `forked_from` (`forked_from`),
#   CONSTRAINT `projects_ibfk_1` FOREIGN KEY (`owner_id`) REFERENCES `users` (`id`),
#   CONSTRAINT `projects_ibfk_2` FOREIGN KEY (`forked_from`) REFERENCES `projects` (`id`)
# ) ENGINE=InnoDB AUTO_INCREMENT=108741 DEFAULT CHARSET=utf8    