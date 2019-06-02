
| Kernel API | Kernel API call | Get the call| 
|---|---|---|
| Linked List API  | list_add, list_add_tail  | grep -R -n  'list_add*' kernel/*  --include '*.c'  |
| |__list_del_entry | grep -R -n  '__list_del_entry*' kernel/*    --include '*.c'|
| |list_replace |grep -R -n  'list_replace*' kernel/*    --include '*.c'|
| |list_prepare_entry |grep -R -n  'list_prepare_entry*' kernel/*    --include '*.c'| 
| | list_for_each<br> list_for_each_prev<br>  list_for_each_safe<br>   list_for_each_prev_safe<br> list_for_each_entry<br> list_for_each_entry_reverse<br>  list_prepare_entry <br> list_for_each_entry_continue<br> list_for_each_entry_continue_reverse<br> list_for_each_entry_from<br> list_for_each_entry_from_reverse<br> list_for_each_entry_safe<br> list_for_each_entry_safe_continue<br>  list_for_each_entry_safe_from<br> list_for_each_entry_safe_reverse  | grep -R -n  'list_for_each_' kernel/*   --include '*.c' |
| | list_prev_entry |grep -R -n  'list_prev_entry*' kernel/*  --include '*.c'|
| | list_nrext_entry|grep -R -n  'list_next_entry*'  kernel/*  --include '*.c'|
| | list_first_entry<br> list_first_entry_or_null|grep -R -n  'list_first_entry_' kernel/*    --include '*.c'|
| |list_entry |grep -R -n  'list_entry_'  kernel/*   --include '*.c'|
| | list_splice<br> list_splice_tail<br> list_splice_init<br> list_splice_tail_init |grep -R -n  'list_splice_'  kernel/*   --include '*.c'|
| | list_cut_position|grep -R -n  'list_cut_position*' kernel/*    --include '*.c'|
| | list_is_singular|grep -R -n  'list_is_singular*' kernel/*    --include '*.c'|
| | list_rotate_left|grep -R -n  'list_rotate_left*' kernel/*    --include '*.c'|
| | list_empty<br> list_empty_careful|grep -R -n  'list_empty*' kernel/*    --include '*.c'|
| | list_is_last |grep -R -n  'list_is_last*' kernel/*    --include '*.c'|
| | list_move|grep -R -n  'list_move*' kernel/*    --include '*.c'|
| | list_del)init |grep -R -n  'list_del_init*' kernel/*    --include '*.c'|
| Clock Framework|clk_get_sys |grep -R -n  'clk_get_sys*' kernel/*    --include '*.c'|
|| clk_get_parent|grep -R -n  'clk_get_parent*' kernel/*    --include '*.c'|
||clk_set_max_rate|grep -R -n  'clk_set_max_rate*' kernel/*    --include '*.c'|
||clk_set_min_rate|grep -R -n  'clk_set_min_rate*' kernel/*    --include '*.c' |
||clk_set_range|grep -R -n  'clk_set_rate_range*' kernel/*    --include '*.c'|
||clk_has_parent|grep -R -n  'clk_has_parent*' kernel/*    --include '*.c'|
||clk_set_rate|grep -R -n  'clk_set_rate' kernel/*    --include '*.c'|
||clk_round_rate|grep -R -n  'clk_round_rate*' kernel/*    --include '*.c'|
||devm_clk_put|grep -R -n  'devm_clk_put*' kernel/*    --include '*.c'|
||clk_put|grep -R -n  'clk_put*' kernel/*    --include '*.c'|
||clk_get_rate|grep -R -n  'clk_get_rate*' kernel/*    --include '*.c'|
||clk_disable|grep -R -n  'clk_disable*' kernel/*    --include '*.c' |
||clk_enable|grep -R -n  'clk_enable*' kernel/*    --include '*.c'|
||devm_get_clk_from_child|grep -R -n  'devm_get_clk_from_child*' kernel/*    --include '*.c'|
||devm_clk_get|grep -R -n  'devm_clk_get*' kernel/*    --include '*.c'|
||clk_get|grep -R -n  'clk_get*' kernel/*    --include '*.c'|
||clk_unprepare|grep -R -n  'clk_unprepare*' kernel/*    --include '*.c'|
||clk_prepare|grep -R -n  'clk_prepare*' kernel/*    --include '*.c'|
||clk_is_match|grep -R -n  'clk_is_match*' kernel/*    --include '*.c'|
||clk_get_phase|grep -R -n  'clk_get_phase*' kernel/*    --include '*.c' |
||clk_set_phase|grep -R -n  'clk_set_phase*' kernel/*    --include '*.c' |
||clk_get_accuracy|grep -R -n  'clk_get_accuracy*' kernel/*    --include '*.c'|
||clk_notifier_unregister|grep -R -n  'clk_notifier_unregister*' kernel/*    --include '*.c'|
||clk_notifier_register |grep -R -n  'clk_notifier_register*' kernel/*    --include '*.c'|
|FIFO API| kfifo_out_peek|grep -R -n  'kfifo_out_peek*' kernel/*    --include '*.c' |
||kfifo_dma_out_finish|grep -R -n  'kfifo_dma_out_finish*' kernel/*    --include '*.c' |
||kfifo_dma_out_prepare|grep -R -n  'kfifo_dma_out_prepare*' kernel/*    --include '*.c' |
||kfifo_dma_in_finish|grep -R -n  'kfifo_dma_in_finish*' kernel/*    --include '*.c' |
||kfifo_dma-in_prepare|grep -R -n  'kfifo_dma_in_prepare*' kernel/*    --include '*.c' |
||kfifo_to_user|grep -R -n  'kfifo_to_user*' kernel/*    --include '*.c' |
||kfifo_from_user|grep -R -n  'kfifo_from_user*' kernel/*    --include '*.c'| 
||kfifo_out_spinlocked|grep -R -n  'kfifo_out_spinlocked*' kernel/*    --include '*.c'| 
||kfifo_out|grep -R -n  'kfifo_out*' kernel/*    --include '*.c' |
||kfifo_in_spinlocked|grep -R -n  'kfifo_in_spinlocked*' kernel/*    --include '*.c'| 
||kfifo_in|grep -R -n  'kfifo_in*' kernel/*    --include '*.c' |
||kfifo_peek|grep -R -n  'kfifo_peek*' kernel/*    --include '*.c'| 
||kfifo_get|grep -R -n  'kfifo_get*' kernel/*    --include '*.c' |
||kfifo_put|grep -R -n  'kfifo_put*' kernel/*    --include '*.c' |
||kfifo_init|grep -R -n  'kfifo_init*' kernel/*    --include '*.c' |
||kfifo_free|grep -R -n  'kfifo_free*' kernel/*    --include '*.c'|
||kfifo_alloc|grep -R -n  'kfifo_alloc*' kernel/*    --include '*.c'| 
||kfifo_peek_len|grep -R -n  'kfifo_peek_len*' kernel/*    --include '*.c'| 
||kfifo_skip|grep -R -n  'kfifo_skip*' kernel/*    --include '*.c' |
||kfifo_avail|grep -R -n  'kfifo_avail*' kernel/*    --include '*.c' |
||kfifo_is_full|grep -R -n  'kfifo_is_full*' kernel/*    --include '*.c'| 
||kfifo_is_empty|grep -R -n  'kfifo_is_empty*' kernel/*    --include '*.c'|
||kfifo_len|grep -R -n  'kfifo_len*' kernel/*    --include '*.c' |
||kfifo_reset|grep -R -n  'kfifo_reset_' kernel/*    --include '*.c'| 
||kfifo_size|grep -R -n  'kfifo_size*' kernel/*    --include '*.c' |
||kfifo_recsize|grep -R -n  'kfifo_recsize*' kernel/*    --include '*.c'| 
||kfifo_esize|grep -R -n  'kfifo_esize*' kernel/*    --include '*.c' |
||kfifo_initialized|grep -R -n  'kfifo_initialized*' kernel/*    --include '*.c'| 
|IPC API|ipc_parse_version|grep -R -n  'ipc_parse_version*'  kernel/*    --include '*.c' |
||ipcctl_pre_down_nolock|grep -R -n  'ipcctl_pre_down_nolock*' kernel/*    --include '*.c' |
||ipc_update_perm|grep -R -n  'ipc_update_perm*' kernel/*    --include '*.c' |
||ipcget|grep -R -n  'ipcget*' kernel/*    --include '*.c' |
||ipc_obtain_object_check|grep -R -n  'ipc_obtain_object_check*' kernel/*    --include '*.c' |
||ipc_lock|grep -R -n  'ipc_lock*' kernel/*    --include '*.c |
||ipc_obtain_object_idr|grep -R -n  'ipc_obtain_object_idr*' kernel/*    --include '*.c' | 
||ipc64_perm_to_ipc_perm|grep -R -n  'ipc64_perm_to_ipc_perm*' kernel/*    --include '*.c' |
||kernel_to_ipc64_perm|grep -R -n  'kernel_to_ipc64_perm*' kernel/*    --include '*.c' |
||ipcperms|grep -R -n  'ipcperms*' kernel/*    --include '*.c' |
||ipc_rcu_alloc|grep -R -n  'ipc_rcu_alloc*' kernel/*    --include '*.c' | 
||ipc_free|grep -R -n  'ipc_free*' kernel/*    --include '*.c' |
||ipc_alloc|grep -R -n  'ipc_alloc*' kernel/*    --include '*.c' |
||ipc_rmid|grep -R -n  'ipc_rmid*' kernel/*    --include '*.c' |
||ipcget_public|grep -R -n  'ipcget_public*' kernel/*    --include '*.c' | 
||ipc_check_perms|grep -R -n  'ipc_check_perms*' kernel/*    --include '*.c'| 
||ipcget_new|grep -R -n  'ipcget_new*' kernel/*    --include '*.c' |
||ipc_addid|grep -R -n  'ipc_addid*' kernel/*    --include '*.c' |
||ipc_get_maxid|grep -R -n  'ipc_get_maxid*' kernel/*    --include '*.c'| 
||ipc_findkey|grep -R -n  'ipc_findkey*' kernel/*    --include '*.c' |
||ipc_init_proc_interface|grep -R -n  'ipc_init_proc_interface*' kernel/*    --include '*.c' |
||ipc_init_ids|grep -R -n  'ipc_init_ids*' kernel/*    --include '*.c' |
||ipc_init|grep -R -n  'ipc_init*' kernel/*    --include '*.c |
|Memory management API|kmalloc, kmalloc_array|grep -R -n  'kmalloc*' kernel/*    --include '*.c' |
||kcalloc|grep -R -n  'kcalloc*' kernel/*    --include '*.c'|
||kzalloc<br> kzalloc_node||grep -R -n  -e 'kzalloc*'  -e 'kzalloc_node *' kernel/*    --include '*.c'|
||kmem_cache_alloc<br> kmem_cache_alloc_node<br> kmem_cache_free|grep -R -n  -e 'kmem_cache_alloc*'  -e 'kmem_cache_alloc_node *  -e 'kmem_cache_free' ' kernel/*    --include '*.c' |
||kfree<br> kfree_const|grep -R -n  'kfree*'  kernel/*    --include '*.  |
||kstrdup<br> kstrdup_const|grep -R -n  -e 'kstrdup*' -e 'kstrdup_const'  kernel/*    --include '*.c'|
||kmemdup<br> memdup_user<br> memdup_usr_nul|grep -R -n  -e 'kmemdup*' -e 'memdup_user*' -e 'memdup_usr_nul*'  kernel/*    --include '*.c'|
||kstrndup|grep -R -n  -e 'kstrndup*'  kernel/*    --include '*.c' |
||get_user_pages_fast|grep -R -n  -e 'get_user_pages_fast*'  kernel/*    --include '*.c'|
||__copy_to_user_inatomic|grep -R -n  -e '__copy_to_user_inatomic*'   kernel/*    --include '*.c'|
|String API|simple_strtoull<br> simple_stroul<br> simple_strtol<br> |grep -R -n  -e 'simple_strtoull*' -e 'simple_strtoul*' -e 'simple_strtol*' -e 'simple_stroll'    kernel/*    --include '*.c'|   
||vsnprintf|grep -R -n  -e 'vsnprintf*'   kernel/*    --include '*.c'|   
||vscnprintf|grep -R -n  -e 'vscnprintf*'   kernel/*    --include '*.c'|  
||snprintf|grep -R -n  -e 'snprintf*'   kernel/*    --include '*.c'  |
||vsprintf|grep -R -n  -e 'sprintf*' -e 'vsprintf*'   kernel/*    --include '*.c|
||sscanf<br> vsscanf|grep -R -n  -e 'sscanf*' -e 'vsscanf*'   kernel/*    --include '*.c' |
||vbin_printf<br> bprintf<br> bstr_printf<br>|grep -R -n  -e 'vbin_printf*' -e 'bprintf*' -e 'bstr_printf'   kernel/*    --include '*.c' |
||kstrtol,kstrtoul<br> ktrtoull,kstrtoll<br> kstrtouint,kstrtoint<br> kstrtobool |grep -R -n  -e 'kstrtol' -e 'kstrtoul' -e 'ktrtoull' -e 'kstrtoll' -e 'kstrtouint' -e 'kstrtoint' -e 'kstrtobool'   kernel/*    --include '*.c'|
||strncasecmp ,strcmp ,strncmp|grep -R -n  -e 'strcmp' -e 'strncmp' -e 'strcasecmp' kernel/*    --include '*.c'|
||strcpy,strncpy<br>  strlcpy,strscpy<br>|grep -R -n  -e 'strcpy' -e 'strncpy' -e 'strlcpy' -e 'strscpy' kernel/*    --include '*.c'|
||strcat,strncat, strlcat |grep -R -n  -e 'strcat' -e 'strncat' -e 'strlcat' kernel/*    --include '*.c'|
||strchr ,strchrnul <br> strrchr,strnchr |grep -R -n  -e 'strchr' -e 'strnchrnul' -e 'strrchr' -e 'strnchr' kernel/*    --include '*.c'|
||skip_spaces|grep -R -n  'skip_spaces' kernel/*    --include '*.c'|
||strim|grep -R -n  'strim' kernel/*    --include '*.c'|
||strlen<br> strnlen| grep -R -n  -e 'strlen' -e 'strnlen'  kernel/*    --include '*.c'|
||strspn<br> strcspn |grep -R -n  -e 'strspn' -e 'strcspn'  kernel/*    --include '*.c'|
||strpbrk|grep -R -n  'strpbrk'  kernel/*    --include '*.c'|
||strsep|grep -R -n  'strsep'  kernel/*    --include '*.c'|
||sysyfs_streq |grep -R -n  'sysfs_streq '  kernel/*    --include '*.c'|
||memset|grep -R -n  'memset'  kernel/*    --include '*.c'|
||memcpy|grep -R -n  'memcpy'  kernel/*    --include '*.c'|
||memmove|grep -R -n  'memmove'  kernel/*    --include '*.c'|
||memcmp|grep -R -n  'memcmp'  kernel/*    --include '*.c'|
||memscan|grep -R -n  'memscan'  kernel/*    --include '*.c'|
||strsts|grep -R -n  'strstr'  kernel/*    --include '*.c'|
||strnstr|grep -R -n  'mstrnstr  kernel/*    --include '*.c'|
||memchr,memchr_inv|grep -R -n  -e 'memchr' -e 'memchr_inv'  kernel/*    --include '*.c'|
||strreplace|grep -R -n  'strreplace'  kernel/*    --include '*.c'|
|Relay API|relay_buf_full|grep -R -n  'relay_buf_full'  kernel/*    --include '*.c'|
||relay_reset|grep -R -n  'relay_reset'  kernel/*    --include '*.c' |
||relay_open|grep -R -n  'relay_open'  kernel/*    --include '*.c'|
||relay_late_setup_files|grep -R -n  'relay_late_setup_files'  kernel/*    --include '*.c'|
||relay_switch_subbuf |grep -R -n  'relay_switch_subbuf'  kernel/*    --include '*.c'|
|| relay_subbufs_consumed  |grep -R -n  'relay_subbufs_consumed '  kernel/*    --include '*.c'  |
|| relay_close| grep -R -n  'relay_close'  kernel/*    --include '*.c' |
||relay_flush |grep -R -n  'relay_flush'  kernel/*    --include '*.c'|
||relay_mmap_buf|grep -R -n  'relay_mmap_buf'  kernel/*    --include '*.c|
||relay_alloc_buf |grep -R -n  'relay_alloc_buf '  kernel/*    --include '*.c'|
||relay_create_buf|grep -R -n  'relay_create_buf '  kernel/*    --include '*.c'|
||relay_destroy_channel |grep -R -n  'relay_destroy_channel'  kernel/*    --include '*.c'|
||relay_destroy_buf |grep -R -n  'relay_destroy_buf '  kernel/*    --include '*.c'|
||relay_remove_buf| grep -R -n  'relay_remove_buf '  kernel/*    --include '*.c'|
||relay_buf_empty |grep -R -n  'relay_buf_empty '  kernel/*    --include '*.c'|
||wakeup_readers|grep -R -n  'wakeup_readers '  kernel/*    --include '*.c'|
||__relay_reset |grep -R -n  '__relay_reset '  kernel/*    --include '*.c'|
||relay_close_buf|grep -R -n  'relay_close_buf '  kernel/*    --include '*.c'|
||relay_file_open |grep -R -n  'relay_file_open'  kernel/*    --include '*.c'|
||relay_file_mmap |grep -R -n  'relay_file_mmap '  kernel/*    --include '*.c'|
||relay_file_poll|grep -R -n  'relay_file_poll '  kernel/*    --include '*.c'|
||relay_file_release |grep -R -n  'relay_file_release'  kernel/*    --include '*.c'|
||relay_file_read_subbuf_avail|grep -R -n  'relay_file_read_subbuf_avail '  kernel/*    --include '*.c'|
||relay_file_read_start_pos|grep -R -n  'relay_file_read_start_pos '  kernel/*    --include '*.c'|
||relay_file_read_end_pos|grep -R -n  'relay_file_read_end_pos'  kernel/*    --include '*.c'| 
|Accounting API|sys_acct | grep -R -n  'sys_acct'  kernel/*    --include '*.c'|
||acct_collect| grep -R -n  'acct_collect '  kernel/*    --include '*.c'|
||acct_process |grep -R -n  'acct_process'  kernel/*    --include '*.c'|
|Security API|security_init| grep -R -n  'security_init'  kernel/*    --include '*.c'|
||security_module_enable |grep -R -n  'security_module_enable'  kernel/*    --include '*.c'|
||security_add_hooks|grep -R -n  'security_add_hooks'  kernel/*    --include '*.c'|
||securityfs_create_file|grep -R -n  'securityfs_create_file'  kernel/*    --include '*.c'|
||securityfs_create_dir|grep -R -n  'securityfs_create_dir'  kernel/*    --include '*.c'|
||securityfs_remove |grep -R -n  'securityfs_remove'  kernel/*    --include '*.c'|
|Firmware API| DMA Interface||
||dmi_check_system| grep -R -n  'dmi_check_system'  kernel/*    --include '*.c'|
||dmi_first_match | grep -R -n  'dmi_first_match'  kernel/*    --include '*.c'|
||dmi_get_system_info | grep -R -n  'dmi_get_system_info'  kernel/*    --include '*.c'|
||dmi_name_in_vendors | grep -R -n  'dmi_name_in_vendors'  kernel/*    --include '*.c'|
|dim_find_device | grep -R -n  'dmi_find_device'  kernel/*    --include '*.c'|
||dmi_get_date |grep -R -n  'dmi_get_date'  kernel/*    --include '*.c'|
||dmi_walk|grep -R -n  'dmi_walk'  kernel/*    --include '*.c'|
||dmi_match|grep -R -n  'dmi_match'  kernel/*    --include '*.c'| 
||EDD Interface||
||edd_show_raw_data|grep -R -n  'edd_show_raw_data'  kernel/*    --include '*.c'|
||edd_release |grep -R -n  'edd_release'  kernel/*    --include '*.c'|
||edd_dev_is_type |grep -R -n  'edd_dev_is_type'  kernel/*    --include '*.c'|
||edd_get_pci_dev |grep -R -n  'edd_get_pci_dev'  kernel/*    --include '*.c'|
||edd_init|grep -R -n  'edd_init'  kernel/*    --include '*.c'|







