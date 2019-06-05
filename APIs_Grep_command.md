
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
||dim_find_device | grep -R -n  'dmi_find_device'  kernel/*    --include '*.c'|
||dmi_get_date |grep -R -n  'dmi_get_date'  kernel/*    --include '*.c'|
||dmi_walk|grep -R -n  'dmi_walk'  kernel/*    --include '*.c'|
||dmi_match|grep -R -n  'dmi_match'  kernel/*    --include '*.c'| 
||EDD Interface||
||edd_show_raw_data|grep -R -n  'edd_show_raw_data'  kernel/*    --include '*.c'|
||edd_release |grep -R -n  'edd_release'  kernel/*    --include '*.c'|
||edd_dev_is_type |grep -R -n  'edd_dev_is_type'  kernel/*    --include '*.c'|
||edd_get_pci_dev |grep -R -n  'edd_get_pci_dev'  kernel/*    --include '*.c'|
||edd_init|grep -R -n  'edd_init'  kernel/*    --include '*.c'|
|Block API|blk_delay_queue|grep -R -n  'blk_delay_queue'  kernel/*    --include '*.c'|
||blk_start_queue_async |grep -R -n  'blk_start_queue_async'  kernel/*    --include '*.c'|
||blk_start_queue |grep -R -n  'blk_start_queue'  kernel/*    --include '*.c'|
||blk_stop_queue |grep -R -n  'blk_stop_queue'  kernel/*    --include '*.c'|
||blk_sync_queue |grep -R -n  'blk_sync_queue'  kernel/*    --include '*.c'|
||__blk_run_queue_uncond|grep -R -n  '__blk_run_queue_uncond'  kernel/*    --include '*.c'|
||__blk_run_queue |grep -R -n  '__blk_run_queue'  kernel/*    --include '*.c'|
||blk_run_queue_async |grep -R -n  'blk_run_queue_async'  kernel/*    --include '*.c'|
||blk_run_queue |grep -R -n  'blk_run_queue'  kernel/*    --include '*.c'|
||blk_queue_bypass_start |grep -R -n  'blk_queue_bypass_start'  kernel/*    --include '*.c'|
||blk_queue_bypass_end|grep -R -n  'blk_queue_bypass_end'  kernel/*    --include '*.c'|
||blk_cleanup_queue |grep -R -n  'blk_cleanup_queue'  kernel/*    --include '*.c'|
||blk_init_queue|grep -R -n  'blk_init_queue'  kernel/*    --include '*.c'|
||blk_requeue_request|grep -R -n  'blk_requeue_request'  kernel/*    --include '*.c'|
||part_round_stats |grep -R -n  'part_round_stats'  kernel/*    --include '*.c'|
||generic_make_request |grep -R -n  'generic_make_request'  kernel/*    --include '*.c'|
||submit_bio |grep -R -n  'submit_bio'  kernel/*    --include '*.c'|
||blk_insert_cloned_request |grep -R -n  'blk_insert_cloned_request'  kernel/*    --include '*.c'|
||blk_rq_err_bytes |grep -R -n  'blk_rq_err_bytes'  kernel/*    --include '*.c'|
||blk_peek_request|grep -R -n  'blk_peek_request'  kernel/*    --include '*.c'|
||blk_start_request |grep -R -n  'blk_start_request'  kernel/*    --include '*.c'|
||blk_fetch_request |grep -R -n  'blk_fetch_request'  kernel/*    --include '*.c'|
||blk_update_request |grep -R -n  'blk_update_request'  kernel/*    --include '*.c'|
||blk_unprep_request |grep -R -n  'blk_unprep_request'  kernel/*    --include '*.c'|
||blk_end_request |grep -R -n  'blk_end_request'  kernel/*    --include '*.c'|
||blk_end_request_all |grep -R -n  'blk_end_request_all'  kernel/*    --include '*.c'|
||blk_end_request_cur |grep -R -n  'blk_end_request_cur'  kernel/*    --include '*.c'|
||blk_end_request_err|grep -R -n  'blk_end_request_err'  kernel/*    --include '*.c'|
||__blk_end_request |grep -R -n  '__blk_end_request'  kernel/*    --include '*.c'|
||__blk_end_request_all |grep -R -n  '__blk_end_request_all'  kernel/*    --include '*.c'|
||__blk_end_request_cur |grep -R -n  'blk_end_request_cur'  kernel/*    --include '*.c'|
||__blk_end_request_err |grep -R -n  'blk_end_request_err'  kernel/*    --include '*.c'|
||rq_flush_dcache_pages |grep -R -n  'rq_flush_dcache_pages'  kernel/*    --include '*.c'|
||blk_lld_busy |grep -R -n  'blk_lld_busy'  kernel/*    --include '*.c'|
||blk_rq_unprep_clone |grep -R -n  'blk_rq_unprep_clone'  kernel/*    --include '*.c'|
||blk_rq_prep_clone|grep -R -n  'blk_rq_prep_clone'  kernel/*    --include '*.c'|
||blk_start_plug |grep -R -n  'blk_start_plug'  kernel/*    --include '*.c'|
||blk_pm_runtime_init |grep -R -n  'blk_pm_runtime_init'  kernel/*    --include '*.c'|
||blk_pre_runtime_suspend |grep -R -n  'blk_pre_runtime_suspend'  kernel/*    --include '*.c'|
||blk_post_runtime_suspend |grep -R -n  'blk_post_runtime_suspend'  kernel/*    --include '*.c'|
||blk_pre_runtime_resume |grep -R -n  'blk_post_runtime_resume'  kernel/*    --include '*.c'|
||blk_post_runtime_resume |grep -R -n  'blk_post_runtime_resume'  kernel/*    --include '*.c'|
||blk_set_runtime_active|grep -R -n  'blk_set_runtime_active'  kernel/*    --include '*.c'|
||__blk_drain_queue |grep -R -n  '__blk_drain_queue'  kernel/*    --include '*.c'|
||__get_request |grep -R -n  '__get_request'  kernel/*    --include '*.c'|
||get_request|grep -R -n  'get_request'  kernel/*    --include '*.c'|
||blk_attempt_plug_merge |grep -R -n  'blk_attempt_plug_merge'  kernel/*    --include '*.c'|
||blk_cloned_rq_check_limits |grep -R -n  'blk_cloned_rq_check_limits'  kernel/*    --include '*.c'|
||blk_end_bidi_request |grep -R -n  'blk_end_bidi_request'  kernel/*    --include '*.c'|
||__blk_end_bidi_request |grep -R -n  '__blk_end_bidi_request'  kernel/*    --include '*.c'|
||blk_rq_map_user_iov |grep -R -n  'blk_rq_map_user_iov'  kernel/*    --include '*.c'|
||blk_rq_unmap_user |grep -R -n  'blk_rq_unmap_user'  kernel/*    --include '*.c'|
||blk_rq_map_kern |grep -R -n  'blk_rq_map_kern'  kernel/*    --include '*.c'|
||blk_release_queue |grep -R -n  'blk_release_queue'  kernel/*    --include '*.c'|
||blk_queue_prep_rq |grep -R -n  'blk_queue_prep_rq'  kernel/*    --include '*.c'|
||blk_queue_unprep_rq |grep -R -n  'blk_queue_unprep_rq'  kernel/*    --include '*.c'|
||blk_set_default_limits |grep -R -n  'blk_set_default_limits'  kernel/*    --include '*.c'|
||blk_set_stacking_limits |grep -R -n  'blk_det_stacking_limits'  kernel/*    --include '*.c'|
||blk_queue_make_request |grep -R -n  'blk_queue_make_request'  kernel/*    --include '*.c'|
||blk_queue_bounce_limit|grep -R -n  'blk_queue_bounce_limit'  kernel/*    --include '*.c'|
||blk_queue_max_hw_sectors|grep -R -n  'blk_queue_max_hw_sectors'  kernel/*    --include '*.c'|
||blk_queue_chunk_sectors|grep -R -n  'blk_queue_chunk_sectors'  kernel/*    --include '*.c'|
||blk_queue_max_discard_sectors |grep -R -n  'blk_queue_max_discard_sectors'  kernel/*    --include '*.c'|
||blk_queue_max_write_same_sectors|grep -R -n  'blk_queue_max_write_same_sectors'  kernel/*    --include '*.c'|
||blk_queue_max_write_zeroes_sectors|grep -R -n  'blk_queue_max_write_zeroes_sectors'  kernel/*    --include '*.c'|
||blk_queue_max_segments |grep -R -n  'blk_queue_max_segments'  kernel/*    --include '*.c'|
||blk_queue_max_discard_segments |grep -R -n  'blk_queue_max_discard_segments '  kernel/*    --include '*.c'|
||blk_queue_max_segment_size|grep -R -n  ' blk_queue_max_segment_size'  kernel/*    --include '*.c'|
||blk_queue_logical_block_size|grep -R -n  ' blk_queue_logical_block_size'  kernel/*    --include '*.c'|
||blk_queue_physical_block_size |grep -R -n  'blk_queue_physical_block_size '  kernel/*    --include '*.c'|
||blk_queue_alignment_offset |grep -R -n  'blk_queue_alignment_offset'  kernel/*    --include '*.c'|
||blk_limits_io_min|grep -R -n  'blk_limits_io_min '  kernel/*    --include '*.c'|
||blk_queue_io_min |grep -R -n  'blk_queue_io_min '  kernel/*    --include '*.c'|
||blk_limits_io_opt|grep -R -n  'blk_limits_io_opt '  kernel/*    --include '*.c'|
||blk_queue_io_opt|grep -R -n  'blk_queue_io_opt '  kernel/*    --include '*.c'|
||blk_queue_stack_limits|grep -R -n  'blk_queue_stack_limits '  kernel/*    --include '*.c'|
||blk_stack_limits|grep -R -n  'blk_stack_limits '  kernel/*    --include '*.c'|
||bdev_stack_limits|grep -R -n  'bdev_stack_limits '  kernel/*    --include '*.c'|
||disk_stack_limits| grep -R -n  'disk_stack_limits '  kernel/*    --include '*.c'|
||blk_queue_dma_pad |grep -R -n  'blk_queue_dma_pad '  kernel/*    --include '*.c'|
||blk_queue_update_dma_pad|grep -R -n  'blk_queue_update_dma_pad '  kernel/*    --include '*.c' |
||blk_queue_dma_drain |grep -R -n  ' blk_queue_dma_drain '  kernel/*    --include '*.c'|
||blk_queue_segment_boundary |grep -R -n  ' blk_queue_segment_boundary'  kernel/*    --include '*.c'|
||blk_queue_virt_boundary |grep -R -n  'blk_queue_virt_boundary  '  kernel/*    --include '*.c'|
||blk_queue_dma_alignment |grep -R -n  ' blk_queue_dma_alignment'  kernel/*    --include '*.c'|
||blk_queue_update_dma_alignment |grep -R -n  'blk_queue_update_dma_alignment '  kernel/*    --include '*.c'|
||blk_set_queue_depth   |grep -R -n  'blk_set_queue_depth '  kernel/*    --include '*.c'|
||blk_queue_write_cache |grep -R -n  'blk_queue_write_cache '  kernel/*    --include '*.c'|
||blk_execute_rq_nowait |grep -R -n  'blk_execute_rq_wait'  kernel/*    --include '*.c'|
||blk_execute_rq|grep -R -n  'blk_execute_rq'  kernel/*    --include '*.c'|
||blkdev_issue_flush |grep -R -n  'blkdev_issue_flush'  kernel/*    --include '*.c'|
||blkdev_issue_discard|grep -R -n  'blkdev_issue_discard'  kernel/*    --include '*.c'|
||blkdev_issue_write_same|grep -R -n  'blkdev_issue_write_same'  kernel/*    --include '*.c'|
||__blkdev_issue_zeroout|grep -R -n  '__blkdev_issue_zeroout'  kernel/*    --include '*.c'|
||blkdev_issue_zeroout|grep -R -n  'blkdev_issue_zeroout'  kernel/*    --include '*.c'|
||blk_queue_find_tag |grep -R -n  'blk_queue_find_tag'  kernel/*    --include '*.c'|
||blk_free_tags |grep -R -n  'blk_free_tags'  kernel/*    --include '*.c'|
||blk_queue_free_tags |grep -R -n  'blk_queue_free_tags'  kernel/*    --include '*.c'|
||blk_init_tags |grep -R -n  'blk_init_tags'  kernel/*    --include '*.c'|
||blk_queue_init_tags |grep -R -n  'blk_queue_init_tags'  kernel/*    --include '*.c'|
||blk_queue_resize_tags |grep -R -n  'blk_queue_resize_tags'  kernel/*    --include '*.c'|
||blk_queue_end_tag |grep -R -n  'blk_queue_end_tag'  kernel/*    --include '*.c'|
||blk_queue_start_tag |grep -R -n  'blk_queue_start_tag'  kernel/*    --include '*.c'|
||blk_queue_invalidate_tags|grep -R -n  'blk_queue_invalidate_tags'  kernel/*    --include '*.c'|
||__blk_queue_free_tags |grep -R -n  '__blk_queue_free_tags'  kernel/*    --include '*.c'|
||blk_rq_count_integrity_sg |grep -R -n  'blk_rq_count_integrity_sg'  kernel/*    --include '*.c'|
||blk_rq_map_integrity_sg |grep -R -n  'blk_rq_map_integrity_sg'  kernel/*    --include '*.c'|
||blk_integrity_compare|grep -R -n  'blk_integrity_compare'  kernel/*    --include '*.c'|
||blk_integrity_register |grep -R -n  'blk_integrity_register'  kernel/*    --include '*.c'|
||blk_integrity_unregister |grep -R -n  'blk_integrity_unregister'  kernel/*    --include '*.c'|
||blk_trace_ioctl |grep -R -n  'blk_trace_ioctl'  kernel/*    --include '*.c'|
||blk_trace_shutdown |grep -R -n  'blk_trace_shutdown'  kernel/*    --include '*.c'|
||blk_add_trace_rq |grep -R -n  'blk_add_trace_rq'  kernel/*    --include '*.c'|
||blk_add_trace_bio |grep -R -n  'blk_add_trace_bio'  kernel/*    --include '*.c'|
||blk_add_trace_bio_remap |grep -R -n  'blk_add_trace_bio_remap'  kernel/*    --include '*.c'|
||blk_add_trace_rq_remap|grep -R -n  'blk_add_trace_rq_remap'  kernel/*    --include '*.c'|
||blk_mangle_minor |grep -R -n  'blk_mangle_minor'  kernel/*    --include '*.c'|
||blk_alloc_devt |grep -R -n  'blk_alloc_devt'  kernel/*    --include '*.c'|
||blk_free_devt|grep -R -n  'blk_free_devt'  kernel/*    --include '*.c'|
||disk_replace_part_tbl |grep -R -n  'disk_replace_part_tbl'  kernel/*    --include '*.c'|
||disk_expand_part_tbl |grep -R -n  'disk_expand_part_tbl'  kernel/*    --include '*.c'|
||disk_block_events |grep -R -n  'disk_block_events'  kernel/*    --include '*.c'|
||disk_unblock_events |grep -R -n  'disk_unblock_events'  kernel/*    --include '*.c'|
||disk_flush_events |grep -R -n  'disk_flush_events'  kernel/*    --include '*.c'|
||disk_clear_events |grep -R -n  'disk_clear_events'  kernel/*    --include '*.c'|
||disk_get_part |grep -R -n  'disk_get_part'  kernel/*    --include '*.c'|
||disk_part_iter_init |grep -R -n  'disk_part_iter_init'  kernel/*    --include '*.c'|
||disk_part_iter_next |grep -R -n  'disk_part_iter_next'  kernel/*    --include '*.c'|
||disk_part_iter_exit|grep -R -n  'disk_part_iter_exit'  kernel/*    --include '*.c'| 
||disk_map_sector_rcu |grep -R -n  'disk_map_sector'  kernel/*    --include '*.c'|
||register_blkdev|grep -R -n  'register_blkdev'  kernel/*    --include '*.c'|
||device_add_disk|grep -R -n  'device_add_disk'  kernel/*    --include '*.c'| 
||get_gendisk|grep -R -n  'get_gendisk'  kernel/*    --include '*.c'|
||bdget_disk|grep -R -n  'bdget_disk'  kernel/*    --include '*.c'|  
|Hardware Interface|Interrupt Handling|||
||synchronize_hardirq |grep -R -n  'synchronize_hardirq'  kernel/*    --include '*.c'|
||synchronize_irq|grep -R -n  'synchronize_irq'  kernel/*    --include '*.c'|
||irq_set_affinity_notifier |grep -R -n  'irq_set_affinity_notifier'  kernel/*    --include '*.c'|
||irq_set_vcpu_affinity |grep -R -n  'irq_set_vcpu_affinity'  kernel/*    --include '*.c'|
||disable_irq_nosync |grep -R -n  'disable_irq_nosync'  kernel/*    --include '*.c'|
||disable_irq|grep -R -n  'disable_irq'  kernel/*    --include '*.c'|
||disable_hardirq |grep -R -n  'disable_hardirq'  kernel/*    --include '*.c'|
||enable_irq|grep -R -n  'enable_irq'  kernel/*    --include '*.c'|
||irq_set_irq_wake |grep -R -n  'irq_set_irq_wake'  kernel/*    --include '*.c'|
||irq_wake_thread |grep -R -n  'irq_wake_thread'  kernel/*    --include '*.c'|
||setup_irq |grep -R -n  'setup_irq '  kernel/*    --include '*.c'|
||remove_irq |grep -R -n  'remove_irq'  kernel/*    --include '*.c'|
||free_irq |grep -R -n  'free_irq'  kernel/*    --include '*.c'|
||request_threaded_irq |grep -R -n  'request_threaded_irq '  kernel/*    --include '*.c'|
||request_any_context_irq|grep -R -n  'request_any_context_irq'  kernel/*    --include '*.c'|
||irq_percpu_is_enabled |grep -R -n  'irq_percpu_is_enabled '  kernel/*    --include '*.c'|
||free_percpu_irq|grep -R -n  'free_percpu_irq'  kernel/*    --include '*.c'|
||request_percpu_irq|grep -R -n  'request_percpu_irq'  kernel/*    --include '*.c'|
||irq_get_irqchip_state |grep -R -n  'irq_get_irqchip_state'  kernel/*    --include '*.c'|
||irq_set_irqchip_state |grep -R -n  'irq_set_irqchip_state '  kernel/*    --include '*.c'|
||DMA Channels||
||request_dma |grep -R -n  'request_dam'  kernel/*    --include '*.c'|
||free_dma|grep -R -n  'free_dma'  kernel/*    --include '*.c'|
||Resource Management||
||request_resource_conflict |grep -R -n  'request_resource_conflict'  kernel/*    --include '*.c'|
||reallocate_resource |grep -R -n  'reallocate_resource'  kernel/*    --include '*.c'|
||lookup_resource |grep -R -n  'lookup_resource'  kernel/*    --include '*.c'|
||insert_resource_conflict|grep -R -n  'insert_resource_conflict'  kernel/*    --include '*.c'|
||insert_resource_expand_to_fit |grep -R -n  'insert_resource_expand_to_fit'  kernel/*    --include '*.c'|
||resource_alignment |grep -R -n  'resource_alignment'  kernel/*    --include '*.c'|
||release_mem_region_adjustable|grep -R -n  'release_mem_region_adjustable'  kernel/*    --include '*.c'|
||request_resource |grep -R -n  'request_resource'  kernel/*    --include '*.c'|
||release_resource|grep -R -n  'release_resource'  kernel/*    --include '*.c'|
||region_intersects |grep -R -n  'region_intersects'  kernel/*    --include '*.c'|
||allocate_resource |grep -R -n  'allocate_resource '  kernel/*    --include '*.c'|
||insert_resource |grep -R -n  'insert_resource'  kernel/*    --include '*.c'|
||remove_resource |grep -R -n  'remove_resource'  kernel/*    --include '*.c'|
||adjust_resource |grep -R -n  'adjust_resource'  kernel/*    --include '*.c'|
||__request_region |grep -R -n  '__request_region'  kernel/*    --include '*.c'|
||__release_region |grep -R -n  '__release_region '  kernel/*    --include '*.c'|
||devm_request_resource|grep -R -n  'devm_request_resource'  kernel/*    --include '*.c'| 
||devm_release_resource |grep -R -n  'devm_release_resource'  kernel/*    --include '*.c'|
||MTRR Handling||
||arch_phys_wc_add |grep -R -n  'arch_phys_wc_add'  kernel/*    --include '*.c'|
||PCI Support Library||
||pci_bus_max_busnr |grep -R -n  'pci_bus_max_busnr'  kernel/*    --include '*.c'|
||pci_find_capability |grep -R -n  'pci_find_capability'  kernel/*    --include '*.c'|
||pci_bus_find_capability |grep -R -n  'pci_bus_find_capability'  kernel/*    --include '*.c'|
||pci_find_next_ext_capability|grep -R -n  'pci_find_next_ext_capability'  kernel/*    --include '*.c'| 
||pci_find_ext_capability|grep -R -n  'pci_find_ext_capability'  kernel/*    --include '*.c'|
||pci_find_next_ht_capability|grep -R -n  'pci_find_next_ht_capability'  kernel/*    --include '*.c'|
||pci_find_ht_capability |grep -R -n  'pci_find_ht_capability '  kernel/*    --include '*.c'|
||pci_find_parent_resource |grep -R -n  'pci_find_parent_resource'  kernel/*    --include '*.c'|
||pci_find_resource |grep -R -n  'pci_find_resource'  kernel/*    --include '*.c'|
||pci_find_pcie_root_port |grep -R -n  'pci_find_pcie_root_port'  kernel/*    --include '*.c'|
||__pci_complete_power_transition |grep -R -n  '__pci_complete_power_transition'  kernel/*    --include '*.c'|
||pci_set_power_state |grep -R -n  'pci_set_power_state'  kernel/*    --include '*.c'|
||pci_choose_state |grep -R -n  'pci_choose_state'  kernel/*    --include '*.c'|
||pci_save_state |grep -R -n  'pci_save_state '  kernel/*    --include '*.c'|
||pci_restore_state |grep -R -n  'pci_restore_state '  kernel/*    --include '*.c'|
||pci_store_saved_state |grep -R -n  'pci_store_saved_state '  kernel/*    --include '*.c'|
||pci_load_saved_state |grep -R -n  'pci_load_saved_state'  kernel/*    --include '*.c'|
||pci_load_and_free_saved_state |grep -R -n  'pci_load_and_free_saved_state'  kernel/*    --include '*.c'|
||pci_reenable_device |grep -R -n  'pci_reenable_device'  kernel/*    --include '*.c'|
||pci_enable_device_io |grep -R -n  'pci_enable_device_io'  kernel/*    --include '*.c'|
||pci_enable_device_mem|grep -R -n  'pci_enable_device_mem'  kernel/*    --include '*.c'|
||pci_enable_device |grep -R -n  ''  kernel/*    --include '*.c'|
||pcim_enable_device |grep -R -n  'pcim_enable_device '  kernel/*    --include '*.c'|
||pcim_pin_device |grep -R -n  'pcim_pin_device '  kernel/*    --include '*.c'|
||pci_disable_device|grep -R -n  'pci_disable_device'  kernel/*    --include '*.c'| 
||pci_set_pcie_reset_state |grep -R -n  'pci_set_pcie_reset_state'  kernel/*    --include '*.c'|
||pci_pme_capable |grep -R -n  'pci_pme_capable'  kernel/*    --include '*.c'|
||pci_pme_active |grep -R -n  'pci_pme_active'  kernel/*    --include '*.c'|
||__pci_enable_wake|grep -R -n  '__pci_enable_wake'  kernel/*    --include '*.c'|
||pci_wake_from_d3|grep -R -n  'pci_wake_from_d3'  kernel/*    --include '*.c'|
||pci_prepare_to_sleep |grep -R -n  'pci_prepare_to_sleep'  kernel/*    --include '*.c'|
||pci_back_from_sleep|grep -R -n  'pci_back_from_sleep'  kernel/*    --include '*.c'|
||pci_dev_run_wake |grep -R -n  'pci_dev_run_wake '  kernel/*    --include '*.c'|
||pci_d3cold_enable|grep -R -n  'pci_d3cold_enable'  kernel/*    --include '*.c'|
||pci_d3cold_disable |grep -R -n  'pci_d3cold_disable '  kernel/*    --include '*.c'|
||pci_common_swizzle |grep -R -n  'pci_common_swizzle '  kernel/*    --include '*.c'|
||pci_release_region|grep -R -n  'pci_release_region'  kernel/*    --include '*.c'|
||pci_request_region |grep -R -n  'pci_request_region '  kernel/*    --include '*.c'|
||pci_request_region_exclusive |grep -R -n  'pci_request_region_exclusive'  kernel/*    --include '*.c'|
||pci_release_selected_regions|grep -R -n  'pci_release_selected_regions'  kernel/*    --include '*.c'|
||pci_request_selected_regions|grep -R -n  ''  kernel/*    --include '*.c'|
||pci_release_regions |grep -R -n  'pci_release_regions'  kernel/*    --include '*.c'|
||pci_request_regions|grep -R -n  'pci_request_regions'  kernel/*    --include '*.c'|
||pci_request_regions_exclusive|grep -R -n  'pci_request_regions_exclusive'  kernel/*    --include '*.c'|
||pci_set_master |grep -R -n  'pci_set_master'  kernel/*    --include '*.c'|
||pci_clear_master|grep -R -n  'pci_clear_master'  kernel/*    --include '*.c'|
||pci_set_cacheline_size|grep -R -n  'pci_set_cacheline_size'  kernel/*    --include '*.c'|
||pci_set_mwi |grep -R -n  'pci_set_mwi'  kernel/*    --include '*.c'|
||pci_try_set_mwi |grep -R -n  'pci_try_set_mwi '  kernel/*    --include '*.c'|
||pci_clear_mwi|grep -R -n  'pci_clear_mwi'  kernel/*    --include '*.c'|
||pci_intx|grep -R -n  'pci_intx'  kernel/*    --include '*.c'|
||pci_intx_mask_supported |grep -R -n  'pci_intx_mask_supported'  kernel/*    --include '*.c'|
||pci_check_and_mask_intx |grep -R -n  'pci_check_and_mask_intx '  kernel/*    --include '*.c'|
||pci_check_and_unmask_intx |grep -R -n  'pci_check_and_unmask_intx'  kernel/*    --include '*.c'|
||pci_wait_for_pending_transaction|grep -R -n  'pci_wait_for_pending_transaction'  kernel/*    --include '*.c'|
||pci_reset_bridge_secondary_bus |grep -R -n  'pci_reset_bridge_secondary_bus'  kernel/*    --include '*.c'|
||__pci_reset_function |grep -R -n  '__pci_reset_function'  kernel/*    --include '*.c'|
||__pci_reset_function_locked |grep -R -n  '__pci_reset_function_locked'  kernel/*    --include '*.c'|
||pci_reset_function |grep -R -n  'pci_reset_function'  kernel/*    --include '*.c'|
||pci_try_reset_function |grep -R -n  'pci_try_reset_function'  kernel/*    --include '*.c'|
||pci_probe_reset_slot |grep -R -n  'pci_probe_reset_slot'  kernel/*    --include '*.c'|
||pci_reset_slot |grep -R -n  'pci_reset_slot'  kernel/*    --include '*.c'|
||pci_try_reset_slot |grep -R -n  'pci_try_reset_slot '  kernel/*    --include '*.c'|
||pci_probe_reset_bus|grep -R -n  'pci_probe_reset_bus'  kernel/*    --include '*.c'| 
||pci_reset_bus |grep -R -n  'pci_reset_bus '  kernel/*    --include '*.c'|
||pci_try_reset_bus |grep -R -n  'pci_try_reset_bus '  kernel/*    --include '*.c'|
||pcix_get_max_mmrbc|grep -R -n  'pcix_get_max_mmrbc'  kernel/*    --include '*.c'|
||pcix_get_mmrbc|grep -R -n  'pcix_get_mmrbc'  kernel/*    --include '*.c'|
||pcix_set_mmrbc |grep -R -n  'pcix_set_mmrbc'  kernel/*    --include '*.c'|
||pcie_get_readrq |grep -R -n  'pcie_get_readrq '  kernel/*    --include '*.c'|
||pcie_set_readrq |grep -R -n  'pcie_set_readrq '  kernel/*    --include '*.c'|
||pcie_get_mps|grep -R -n  'pcie_get_mps'  kernel/*    --include '*.c'|
||pcie_set_mps|grep -R -n  'pcie_set_mps'  kernel/*    --include '*.c'|
||pcie_get_minimum_link |grep -R -n  'pcie_get_minimum_link'  kernel/*    --include '*.c'|
||pci_select_bars |grep -R -n  'pci_select_bars'  kernel/*    --include '*.c'|
||pci_add_dynid|grep -R -n  'pci_add_dynid'  kernel/*    --include '*.c'|
||pci_match_id|grep -R -n  'pci_match_id'  kernel/*    --include '*.c'|
||__pci_register_driver |grep -R -n  '__pci_register_driv'  kernel/*    --include '*.c'|
||pci_unregister_driver |grep -R -n  'pci_unregister_driver'  kernel/*    --include '*.c'|
||pci_dev_driver |grep -R -n  'pci_dev_driver'  kernel/*    --include '*.c'|
||pci_dev_get |grep -R -n  'pci_dev_get '  kernel/*    --include '*.c'|
||pci_dev_put |grep -R -n  'pci_dev_put' kernel/*    --include '*.c'|
||pci_stop_and_remove_bus_device |grep -R -n  'pci_stop_and_remove_bus_device'  kernel/*    --include '*.c'|
||pci_find_bus |grep -R -n  'pci_find_bus'  kernel/*    --include '*.c'|
||pci_find_next_bus|grep -R -n  'pci_find_next_bus'  kernel/*    --include '*.c'| 
||pci_get_slot |grep -R -n  'pci_get_slot '  kernel/*    --include '*.c'|
||pci_get_domain_bus_and_slot |grep -R -n  'pci_get_domain_bus_and_slot'  kernel/*    --include '*.c'| 
||pci_get_subsys|grep -R -n  'pci_get_subsys'  kernel/*    --include '*.c'| 
||pci_get_device |grep -R -n  'pci_get_device'  kernel/*    --include '*.c'|
||pci_get_class |grep -R -n  'pci_get_class '  kernel/*    --include '*.c'|
||pci_dev_present |grep -R -n  'pci_dev_present'  kernel/*    --include '*.c'|
||pci_msi_mask_irq |grep -R -n  'pci_msi_mask_irq '  kernel/*    --include '*.c'|
||pci_msi_unmask_irq |grep -R -n  'pci_msi_unmask_irq '  kernel/*    --include '*.c'|
||pci_msi_vec_count |grep -R -n  'pci_msi_vec_count '  kernel/*    --include '*.c'|
||pci_msix_vec_count |grep -R -n  'pci_msix_vec_count'  kernel/*    --include '*.c'|
||pci_enable_msix|grep -R -n  'pci_enable_msix'  kernel/*    --include '*.c'|
||pci_msi_enabled |grep -R -n  'pci_msi_enabled'  kernel/*    --include '*.c'|
||pci_enable_msix_range |grep -R -n  'pci_enable_msix_range '  kernel/*    --include '*.c'|
||pci_alloc_irq_vectors_affinity|grep -R -n  'pci_alloc_irq_vectors_affinity'  kernel/*    --include '*.c'|
||pci_free_irq_vectors |grep -R -n  'pci_free_irq_vectors'  kernel/*    --include '*.c'|
||pci_irq_vector|grep -R -n  'pci_irq_vector'  kernel/*    --include '*.c'|
||pci_irq_get_affinity|grep -R -n  'pci_irq_get_affinity'  kernel/*    --include '*.c'| 
||pci_irq_get_node |grep -R -n  'pci_irq_get_node '  kernel/*    --include '*.c'|
||pci_msi_create_irq_domain |grep -R -n  'pci_msi_create_irq_domain '  kernel/*    --include '*.c'|
||pci_bus_alloc_resource |grep -R -n  'pci_bus_alloc_resource'  kernel/*    --include '*.c'|
||pci_bus_add_device |grep -R -n  'pci_bus_add_device '  kernel/*    --include '*.c'|
||pci_bus_add_devices |grep -R -n  'pci_bus_add_devices'  kernel/*    --include '*.c'|
||pci_bus_set_ops |grep -R -n  'pci_bus_set_ops'  kernel/*    --include '*.c'|
||pci_read_vpd |grep -R -n  'pci_read_vpd '  kernel/*    --include '*.c'|
||pci_write_vpd|grep -R -n  'pci_write_vpd'  kernel/*    --include '*.c'|
||pci_set_vpd_size |grep -R -n  'pci_set_vpd_size'  kernel/*    --include '*.c'|
||pci_cfg_access_lock|grep -R -n  'pci_cfg_access_lock'  kernel/*    --include '*.c'|
||pci_cfg_access_trylock|grep -R -n  'pci_cfg_access_trylock'  kernel/*    --include '*.c'|
||pci_cfg_access_unlock|grep -R -n  'pci_cfg_access_unlock'  kernel/*    --include '*.c'|
||pci_lost_interrupt |grep -R -n  'pci_lost_interrupt '  kernel/*    --include '*.c'|
||__ht_create_irq |grep -R -n  '__ht_create_irq'  kernel/*    --include '*.c'|
||ht_create_irq |grep -R -n  'ht_create_irq'  kernel/*    --include '*.c'|
||ht_destroy_irq |grep -R -n  'ht_destroy_irq'  kernel/*    --include '*.c'|
||pci_scan_slot |grep -R -n  'pci_scan_slot '  kernel/*    --include '*.c'|
||pci_rescan_bus|grep -R -n  'pci_rescan_bus'  kernel/*    --include '*.c'|
||pci_create_slot |grep -R -n  'pci_create_slot'  kernel/*    --include '*.c'|
||pci_destroy_slot |grep -R -n  'pci_destroy_slot '  kernel/*    --include '*.c'|
||pci_hp_create_module_link |grep -R -n  'pci_hp_create_module_link '  kernel/*    --include '*.c'|
||pci_hp_remove_module_link|grep -R -n  ''  kernel/*    --include '*.c'|
||pci_enable_rom |grep -R -n  'pci_enable_rom '  kernel/*    --include '*.c'|
||pci_disable_rom|grep -R -n  'pci_disable_rom'  kernel/*    --include '*.c'| 
||pci_map_rom |grep -R -n  'pci_map_rom'  kernel/*    --include '*.c'|
||pci_unmap_rom |grep -R -n  'pci_unmap_rom'  kernel/*    --include '*.c'|
||pci_platform_rom |grep -R -n  'pci_platform_rom '  kernel/*    --include '*.c'|
||pci_enable_sriov |grep -R -n  'pci_enable_sriov'  kernel/*    --include '*.c'|
||pci_disable_sriov |grep -R -n  'pci_disable_sriov'  kernel/*    --include '*.c'|
||pci_num_vf |grep -R -n  'pci_num_vf'  kernel/*    --include '*.c'|
||pci_vfs_assigned |grep -R -n  'pci_vfs_assigned'  kernel/*    --include '*.c'|
||pci_sriov_set_totalvfs|grep -R -n  'pci_sriov_set_totalvfs'  kernel/*    --include '*.c'| 
||pci_sriov_get_totalvfs |grep -R -n  'pci_sriov_get_totalvfs'  kernel/*    --include '*.c'|
||pci_read_legacy_io |grep -R -n  'pci_read_legacy_io '  kernel/*    --include '*.c'|
||pci_write_legacy_io |grep -R -n  'pci_write_legacy_io'  kernel/*    --include '*.c'|
||pci_mmap_legacy_mem |grep -R -n  'pci_mmap_legacy_mem'  kernel/*    --include '*.c'|
||pci_mmap_legacy_io |grep -R -n  'pci_mmap_legacy_io'  kernel/*    --include '*.c'|
||pci_adjust_legacy_attr|grep -R -n  'pci_adjust_legacy_attr'  kernel/*    --include '*.c'|
||pci_create_legacy_files |grep -R -n  'pci_create_legacy_files'  kernel/*    --include '*.c'|
||pci_mmap_resource |grep -R -n  'pci_mmap_resource'  kernel/*    --include '*.c'|
||pci_remove_resource_files |grep -R -n  'pci_remove_resource_files'  kernel/*    --include '*.c'|
||pci_create_resource_files |grep -R -n  'pci_create_resource_files'  kernel/*    --include '*.c'|
||pci_write_rom|grep -R -n  'pci_write_rom'  kernel/*    --include '*.c'|
||pci_read_rom|grep -R -n  'pci_read_rom'  kernel/*    --include '*.c'|
||pci_remove_sysfs_dev_files |grep -R -n  'pci_remove_sysfs_dev_files '  kernel/*    --include '*.c'|
||PCI Hotplug Support Library||
||__pci_hp_register|grep -R -n  '__pci_hp_register'  kernel/*    --include '*.c'| 
||pci_hp_deregister|grep -R -n  'pci_hp_deregister'  kernel/*    --include '*.c'|
||pci_hp_change_slot_info|grep -R -n  'pci_hp_change_slot_info'  kernel/*    --include '*.c'| 
|Audit Interfaces|audit_log_start|grep -R -n  'audit_log_start'  kernel/*    --include '*.c'|
||audit_log_format |grep -R -n  'audit_log_format'  kernel/*    --include '*.c'|
||audit_log_end|grep -R -n  'audit_log_end'  kernel/*    --include '*.c'|
||audit_log |grep -R -n  'audit_log '  kernel/*    --include '*.c'|
||audit_log_secctx |grep -R -n  'audit_log_secctx'  kernel/*    --include '*.c'|
||audit_alloc |grep -R -n  'audit_alloc'  kernel/*    --include '*.c'|
|| __audit_free |grep -R -n  '__audit_free'  kernel/*    --include '*.c'|
|| __audit_syscall_entry|grep -R -n  '__audit_syscall_entry'  kernel/*    --include '*.c'| 
|| __audit_syscall_exit |grep -R -n  '__audit_syscall_exit'  kernel/*    --include '*.c'|
|| __audit_reusename |grep -R -n  '__audit_reusename '  kernel/*    --include '*.c'|
||__audit_getname|grep -R -n  '__audit_getname'  kernel/*    --include '*.c'|
||__audit_inode |grep -R -n  '__audit_inode '  kernel/*    --include '*.c'|
||auditsc_get_stamp|grep -R -n  'auditsc_get_stamp'  kernel/*    --include '*.c'| 
||audit_set_loginuid |grep -R -n  'audit_set_loginuid '  kernel/*    --include '*.c'|
|| __audit_mq_open|grep -R -n  '__audit_mq_open'  kernel/*    --include '*.c'|
|| __audit_mq_sendrecv|grep -R -n  '__audit_mq_sendrecv'  kernel/*    --include '*.c'| 
|| __audit_mq_notify |grep -R -n  '__audit_mq_notify'  kernel/*    --include '*.c'|
|| __audit_mq_getsetattr|grep -R -n  '__audit_mq_getsetattr'  kernel/*    --include '*.c'|
|| __audit_ipc_obj |grep -R -n  '__audit_ipc_obj'  kernel/*    --include '*.c'|
|| __audit_ipc_set_perm|grep -R -n  '__audit_ipc_set_perm'  kernel/*    --include '*.c'|
|| __audit_socketcall |grep -R -n  '__audit_socketcall '  kernel/*    --include '*.c'|
|| __audit_fd_pair|grep -R -n  '__audit_fd_pair'  kernel/*    --include '*.c'|
|| __audit_sockaddr |grep -R -n  '__audit_sockaddr '  kernel/*    --include '*.c'|
|| audit_signal_info|grep -R -n  'audit_signal_info'  kernel/*    --include '*.c'|
|| __audit_log_bprm_fcaps |grep -R -n  '__audit_log_bprm_fcaps '  kernel/*    --include '*.c'|
|| __audit_log_capset |grep -R -n  '__audit_log_capset'  kernel/*    --include '*.c'|
|| audit_core_dumps |grep -R -n  'audit_core_dumps '  kernel/*    --include '*.c'|
|| audit_rule_change|grep -R -n  'audit_rule_change'  kernel/*    --include '*.c'|
|| audit_list_rules_send |grep -R -n  'audit_list_rules_send'  kernel/*    --include '*.c'|
|| parent_len |grep -R -n  'parent_len '  kernel/*    --include '*.c'|
|| audit_compare_dname_path |grep -R -n  'audit_compare_dname_path'  kernel/*    --include '*.c'|



