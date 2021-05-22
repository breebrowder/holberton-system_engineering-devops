# Puppet is an open source config management tool, use to alter config file

file { '/etc/ssh/ssh_config':
     content => 'PasswordAuthentication No
     IdentityFile ~/.ssh.holberton',
}
