# Use puppet tool to alter config file, no password auth

file { '/etc/ssh/ssh_config':
  content => 'PasswordAuthentication no
  IdentityFile ~/.ssh/holberton',
}