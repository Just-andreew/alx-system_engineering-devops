# Execute pkill command
exec {'pkill killmenow':
    path   => '/usr/bin',
    onlyif => 'pgrep -x killmenow',
}
