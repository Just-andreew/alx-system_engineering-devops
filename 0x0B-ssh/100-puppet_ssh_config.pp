# Ensure SSH client configuration uses the private key ~/.ssh/school
file_line { 'Declare identity file':
  path   => '/user/abbot/.ssh/config',
  line   => 'IdentityFile school',
  ensure => present,
}

# Ensure SSH client configuration refuses to authenticate using a password
file_line { 'Turn off passwd auth':
  path   => '/user/abbot/.ssh/config',
  line   => 'PasswordAuthentication no',
  ensure => present,
}
