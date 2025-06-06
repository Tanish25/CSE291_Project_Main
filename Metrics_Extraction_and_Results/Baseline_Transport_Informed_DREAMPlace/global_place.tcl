utl::set_metrics_stage "globalplace__{}"
source $::env(SCRIPTS_DIR)/load.tcl
if {[env_var_exists_and_non_empty PLATFORM_TCL]} {
    log_cmd source $::env(PLATFORM_TCL)
}
source $::env(SCRIPTS_DIR)/read_liberty.tcl
read_lef $::env(TECH_LEF)
read_lef $::env(SC_LEF)
if {[env_var_exists_and_non_empty ADDITIONAL_LEFS]} {
      foreach lef $::env(ADDITIONAL_LEFS) {
        read_lef $lef
      }
}
read_def $::env(RESULTS_DIR)/pre_gp_asap7_ibex_custom.def
write_db $::env(RESULTS_DIR)/pre_gp_asap7_ibex_custom.odb
erase_non_stage_variables place
#load_design pre_gp_asap7_gcd.odb 2_floorplan.sdc
read_sdc $::env(RESULTS_DIR)/2_floorplan.sdc
if [file exists $::env(PLATFORM_DIR)/derate.tcl] {
    log_cmd source $::env(PLATFORM_DIR)/derate.tcl
}
source $::env(PLATFORM_DIR)/setRC.tcl
if { [env_var_equals LIB_MODEL CCS] } {
    puts "Using CCS delay calculation"
    set_delay_calculator prima
}


set_dont_use $::env(DONT_USE_CELLS)

fast_route

set global_placement_args {}

# Parameters for routability mode in global placement
append_env_var global_placement_args GPL_ROUTABILITY_DRIVEN -routability_driven 0

# Parameters for timing driven mode in global placement
if {$::env(GPL_TIMING_DRIVEN)} {
  lappend global_placement_args {-timing_driven}
  if {[info exists ::env(GPL_KEEP_OVERFLOW)]} {
    lappend global_placement_args -keep_resize_below_overflow $::env(GPL_KEEP_OVERFLOW)
  }
}

proc do_placement {global_placement_args} {
  set all_args [concat [list -density [place_density_with_lb_addon] \
    -pad_left $::env(CELL_PAD_IN_SITES_GLOBAL_PLACEMENT) \
    -pad_right $::env(CELL_PAD_IN_SITES_GLOBAL_PLACEMENT)] \
    $global_placement_args]

  lappend all_args {*}$::env(GLOBAL_PLACEMENT_ARGS)

  log_cmd global_placement {*}$all_args
}

set result [catch {do_placement $global_placement_args} errMsg]
if {$result != 0} {
  write_db $::env(RESULTS_DIR)/3_3_place_gp-failed.odb
  error $errMsg
}

estimate_parasitics -placement

if {[env_var_equals CLUSTER_FLOPS 1]} {
  cluster_flops
  estimate_parasitics -placement
}

report_metrics 3 "global place" false false

write_db $::env(RESULTS_DIR)/3_3_place_gp.odb
