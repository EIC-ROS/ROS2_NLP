cmake_minimum_required(VERSION 3.8)
project(nlp_connector_dependencies)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(rosidl_default_generators REQUIRED)

set(msg_files
  "msg/NLPType.msg"
)

rosidl_generate_interfaces(${PROJECT_NAME}
  "msg/NLPType.msg"
  "srv/NLPSrv.srv"
  DEPENDENCIES geometry_msgs # Add packages that above messages depend on, in this case geometry_msgs for Sphere.msg
)

ament_export_dependencies(rosidl_default_runtime) 

ament_package()
