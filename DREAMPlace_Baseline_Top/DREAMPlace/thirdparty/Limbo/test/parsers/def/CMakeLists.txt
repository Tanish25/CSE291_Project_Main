if(Boost_INCLUDE_DIRS)
    set(INCLUDES ${Boost_INCLUDE_DIRS})
    set(LIBS ${Boost_LIBRARIES})
else(Boost_INCLUDE_DIRS)
    set(LIBS Boost::boost)
endif(Boost_INCLUDE_DIRS)
include_directories(
    ${PROJECT_SOURCE_DIR}
    ${INCLUDES}
    )
if(CMAKE_BUILD_TYPE STREQUAL "Debug")
    set(COMPILE_DEFINITIONS DEBUG_DEFPARSER)
else()
    set(COMPILE_DEFINITIONS "")
endif()

if(PARSER_DEF_BISON)
add_executable(test_def_bison test_bison.cpp)
set_target_properties(test_def_bison PROPERTIES OUTPUT_NAME "test_bison")
target_link_libraries(test_def_bison PRIVATE defparser ${LIBS})
if(COMPILE_DEFINITIONS)
    target_compile_definitions(test_def_bison PRIVATE ${COMPILE_DEFINITIONS})
endif(COMPILE_DEFINITIONS)
if(INSTALL_LIMBO)
    install(TARGETS test_def_bison DESTINATION test/parsers/def)
endif(INSTALL_LIMBO)
endif(PARSER_DEF_BISON)

if(PARSER_DEF_ADAPT)
add_executable(test_def_adapt test_adapt.cpp)
set_target_properties(test_def_adapt PROPERTIES OUTPUT_NAME "test_adapt")
target_link_libraries(test_def_adapt PRIVATE ${PROJECT_BINARY_DIR}/limbo/parsers/def/adapt/libdefparseradapt.a ${LIBS})
add_dependencies(test_def_adapt defparseradapt)
if(COMPILE_DEFINITIONS)
    target_compile_definitions(test_def_adapt PRIVATE ${COMPILE_DEFINITIONS})
endif(COMPILE_DEFINITIONS)
if(INSTALL_LIMBO)
    install(TARGETS test_def_adapt DESTINATION test/parsers/def)
endif(INSTALL_LIMBO)
endif(PARSER_DEF_ADAPT)

if(PARSER_DEF_SPIRIT)
#add_executable(test_def_spirit test_spirit.cpp)
#set_target_properties(test_def_spirit PROPERTIES OUTPUT_NAME "test_spirit")
#if(COMPILE_DEFINITIONS)
#    target_compile_definitions(test_def_spirit PRIVATE ${COMPILE_DEFINITIONS})
#endif(COMPILE_DEFINITIONS)
if(INSTALL_LIMBO)
	#install(TARGETS test_def_spirit DESTINATION test/parsers/def)
    install(DIRECTORY benchmarks DESTINATION test/parsers/def)
endif(INSTALL_LIMBO)
endif(PARSER_DEF_SPIRIT)
