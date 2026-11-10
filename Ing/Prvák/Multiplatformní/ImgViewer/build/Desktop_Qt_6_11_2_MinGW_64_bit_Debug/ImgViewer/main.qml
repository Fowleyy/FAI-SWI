import QtQuick
import QtQuick.Controls
import QtQuick.Controls.Material
import QtQuick.Layouts

ApplicationWindow {
    width: 600
    height: 800
    visible: true
    title: qsTr("Image Viewer")

    Material.primary: "stellblue"
    Material.background: "lightgray"

    header: ToolBar {
        id: topToolBar
        Material.foreground: "white"
        RowLayout {
            anchors.fill: parent
            ToolButton{
                icon.source: "qrc:/img/menu.png"
                onClicked: mainDrawer.open()
            }

            Label{
                text: qsTr("ImgViewer")
                horizontalAlignment: Qt.AlignHCenter
                font.pointSize: 14
                font.bold: true
                Layout.fillWidth: true

            }
            ToolButton{
                icon.source: "qrc:/img/settings.png"
                onClicked: mainMenu.open()


                Menu{
                    id: mainMenu
                    y: topToolBar.height
                    MenuItem{
                        text: qsTr("Quit")
                        onTriggered: Qt.quit()
                    }
                }
            }
        }
    }


    Drawer{
        id: mainDrawer
        width: parent.width * 0.6
        height: parent.height

        ListView{
            id: imgSelector
            anchors.fill: parent
            anchors.margins: 20
            model: dataModel
            spacing: 20

            delegate:Column{
                width: imgSelector.width
                spacing: 5
                Image{
                    width: parent.width
                    source: model.url
                    fillMode: Image.PreserveAspectFit

                    MouseArea{
                        anchors.fill: parent
                        onClicked: imgSelector.currentIndex = index
                    }
                }
                Label{
                    text: model.name
                    anchors.horizontalCenter: parent.horizontalCenter
                }
            }
        }
    }

    Image{
        anchors.fill: parent
        anchors.margins: 20
        fillMode: Image.PreserveAspectFit
        source: dataModel.get(imgSelector.currentIndex).url
    }

    ListModel{
        id: dataModel
        ListElement{ url: "qrc:/img/image1.jpg";  name: "Kočka 1"  }
        ListElement{ url: "qrc:/img/image2.jpg";  name: "Kočka 2"  }
        ListElement{ url: "qrc:/img/image3.jpg";  name: "Kočka 3"  }
    }
}


