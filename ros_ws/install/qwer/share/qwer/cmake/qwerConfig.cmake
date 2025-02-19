# generated from ament/cmake/core/templates/nameConfig.cmake.in

# prevent multiple inclusion
if(_qwer_CONFIG_INCLUDED)
  # ensure to keep the found flag the same
  if(NOT DEFINED qwer_FOUND)
    # explicitly set it to FALSE, otherwise CMake will set it to TRUE
    set(qwer_FOUND FALSE)
  elseif(NOT qwer_FOUND)
    # use separate condition to avoid uninitialized variable warning
    set(qwer_FOUND FALSE)
  endif()
  return()
endif()
set(_qwer_CONFIG_INCLUDED TRUE)

# output package information
if(NOT qwer_FIND_QUIETLY)
  message(STATUS "Found qwer: 0.3.0 (${qwer_DIR})")
endif()

# warn when using a deprecated package
if(NOT "" STREQUAL "")
  set(_msg "Package 'qwer' is deprecated")
  # append custom deprecation text if available
  if(NOT "" STREQUAL "TRUE")
    set(_msg "${_msg} ()")
  endif()
  # optionally quiet the deprecation message
  if(NOT ${qwer_DEPRECATED_QUIET})
    message(DEPRECATION "${_msg}")
  endif()
endif()

# flag package as ament-based to distinguish it after being find_package()-ed
set(qwer_FOUND_AMENT_PACKAGE TRUE)

# include all config extra files
set(_extras "")
foreach(_extra ${_extras})
  include("${qwer_DIR}/${_extra}")
endforeach()
