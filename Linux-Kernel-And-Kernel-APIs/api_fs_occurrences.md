
| Kernel Directory| Kernel API | Kernel API call |  Kernel API Occurrences |    Get the call    |
|---|---|---|---|---|
| fs | [Linux Filesystems API](https://www.kernel.org/doc/html/latest/filesystems/api-summary.html#linux-filesystems-api-summary) |  The Linux VFS<br>      - File System Types<br><br>   - The Directory Cache   | grep -c 'sb_end*' fs/* <br>   grep  -c 'sb_start*' fs/* <br><br>  | grep  -n 'sb_end*' fs/* <br>  grep  -n 'sb_start*' fs/* <br><br> |
|    |   | The proc system<br>  -sysctl interface<br>  - proc filesystem interface<br> | grep -c 'proc_doinvtec*' fs/* <br>  grep  -c 'proc_flush_task*' fs/proc/*   | grep -n 'proc_doinvtec*' fs/* <br> grep  -n 'proc_flush_task*' fs/proc/*| 
|    |   | Events based on file descriptors |  grep  -c 'eventfd_* 'fs/* <br>  |  grep  -n 'eventfd_* 'fs/* <br>   |0
|    |   | The Filesystem for Exporting Kernel Objects |   grep  -c 'sysfs_* 'fs/*  <br>  grep  -c 'kernfs_* 'fs/*  <br>   grep  -c 'kernfs_* 'fs/kernfs/* <br> grep  -n 'sysfs_* ' fs/sysfs/*| grep  -n 'sysfs_* ' fs/*  <br> grep  -n 'kernfs_* ' fs/*   <br>  grep  -n 'kernfs_* ' fs/kernfs/* <br>  grep  -n 'sysfs_* ' fs/sysfs/*|
|    |   | The debugfs filesystem  |  grep  -c 'debugfs_* 'fs/orangefs/*  |  grep  -n 'debugfs_* ' fs/orangefs/*  |
|    |   |  splice API  |    grep  -c 'splice_* 'fs/*   |    grep  -n 'splice_* 'fs/*   |
|    |   |  pipe API  |   grep  -c 'pipe_* 'fs/*   |  grep  -n 'pipe_* 'fs/*    |
|    |   |  The Linux Journalling API |  grep  -c 'jbd2_journal_* 'fs/ext4/*  <br>  grep  -c'jbd2_journal_*  'fs/jbd2/* <br>  grep  -c 'jbd2_journal_* 'fs/ocfs2/*   |  grep  -n 'jbd2_journal_* ' fs/ext4/* <br>  grep  -n 'jbd2_journal_* 'fs/jbd2/*  <br>   grep  -n 'jbd2_journal_* 'fs/ocfs2/*   | 
