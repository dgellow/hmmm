import os
import grp
import signal
import daemon
import lockfile

from main import (
    setup,
    main,
    cleanup,
    reload_config,
)

context = daemon.DaemonContext(
    working_directory = '/var/lib/hmmm',
    umask = 0o002,
    pidfile = lockfile.FileLock('/var/run/hmmm.pid'),
)

context.signal_map = {
    signal.SIGTERM: cleanup,
    signal.SIGHUP: 'terminate',
    signal.SIGUSR1: reload_config
}

initial_program_setup()

with context:
    main()
