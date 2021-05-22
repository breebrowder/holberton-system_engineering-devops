# ADVANCED TASK IN 0x0B- SSH
# CLIENT CONFIGURATION WITH PUPPET
# Puppet is an open source configuration management tool. The Puppet software pulls its configuration from code written in a Ruby DSL

file { '/etc/ssh/ssh_config':
     content => 'PasswordAuthentication no
     IdentifyFile ~/.ssh.holberton',
}
