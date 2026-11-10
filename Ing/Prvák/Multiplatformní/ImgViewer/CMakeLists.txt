cmake_minimum_required(VERSION 3.16)

project(ImgViewer VERSION 0.1 LANGUAGES CXX)

set(CMAKE_AUTOMOC ON)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(Qt6 6.2 COMPONENTS Quick QuickControls2 REQUIRED)

qt_add_executable(appImgViewer
    main.cpp
)

qt_add_qml_module(appImgViewer
    URI ImgViewer
    VERSION 1.0
    QML_FILES main.qml 
)

qt_add_resources(appImgViewer Images FILES
        img/settings.png
        img/menu.png
        img/image1.jpg
        img/image2.jpg
        img/image3.jpg
    )

# Qt for iOS sets MACOSX_BUNDLE_GUI_IDENTIFIER automatically since Qt 6.1.
# If you are developing for iOS or macOS you should consider setting an
# explicit, fixed bundle identifier manually though.
set_target_properties(appImgViewer PROPERTIES
#    MACOSX_BUNDLE_GUI_IDENTIFIER com.example.appImgViewer
    MACOSX_BUNDLE_BUNDLE_VERSION ${PROJECT_VERSION}
    MACOSX_BUNDLE_SHORT_VERSION_STRING ${PROJECT_VERSION_MAJOR}.${PROJECT_VERSION_MINOR}
    MACOSX_BUNDLE TRUE
    WIN32_EXECUTABLE TRUE
)

target_link_libraries(appImgViewer
    PRIVATE Qt6::Quick)

include(GNUInstallDirs)
install(TARGETS appImgViewer
    BUNDLE DESTINATION .
    LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR})
