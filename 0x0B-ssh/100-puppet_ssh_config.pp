# Puppet is an open source configuration management tool. Adv task - using puppet to alter config file

file { '/etc/ssh/ssh_config':
     content => 'PasswordAuthentication No
     IdentityFile ~/.ssh.holberton',
}
