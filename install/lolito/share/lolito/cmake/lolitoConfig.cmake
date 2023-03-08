# generated from ament/cmake/core/templates/nameConfig.cmake.in

# prevent multiple inclusion
if(_lolito_CONFIG_INCLUDED)
  # ensure to keep the found flag the same
  if(NOT DEFINED lolito_FOUND)
    # explicitly set it to FALSE, otherwise CMake will set it to TRUE
    set(lolito_FOUND FALSE)
  elseif(NOT lolito_FOUND)
    # use separate condition to avoid uninitialized variable warning
    set(lolito_FOUND FALSE)
  endif()
  return()
endif()
set(_lolito_CONFIG_INCLUDED TRUE)

# output package information
if(NOT lolito_FIND_QUIETLY)
  message(STATUS "Found lolito: 0.0.0 (${lolito_DIR})")
endif()

# warn when using a deprecated package
if(NOT "" STREQUAL "")
  set(_msg "Package 'lolito' is deprecated")
  # append custom deprecation text if available
  if(NOT "" STREQUAL "TRUE")
    set(_msg "${_msg} ()")
  endif()
  # optionally quiet the deprecation message
  if(NOT ${lolito_DEPRECATED_QUIET})
    message(DEPRECATION "${_msg}")
  endif()
endif()

# flag package as ament-based to distinguish it after being find_package()-ed
set(lolito_FOUND_AMENT_PACKAGE TRUE)

# include all config extra files
set(_extras "")
foreach(_extra ${_extras})
  include("${lolito_DIR}/${_extra}")
endforeach()
