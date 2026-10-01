#include "mainwindow.h"
#include <QMenuBar>
#include <QMenu>
#include <QAction>
#include <QFile>
#include <QFileDialog>
#include <QMessageBox>
#include <QTextStream>

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
{

    setGeometry(100,100,600,400);

    QMenu *menuFile = new QMenu("File");

    QAction *actQuit = new QAction("Quit");
    actQuit->setShortcut(QKeySequence::Close);
    QAction *actOpen = new QAction("Open File");
    actOpen->setShortcut(QKeySequence::Open);
    QAction *actSaveAs = new QAction("Save file");
    actSaveAs->setShortcut(QKeySequence::Save);

    menuFile->addAction(actOpen);
    menuFile->addAction(actSaveAs);
    menuFile->addSeparator();
    menuFile->addAction(actQuit);
    connect(actQuit, &QAction::triggered, this, &MainWindow::close);
    connect(actSaveAs, &QAction::triggered, this, &MainWindow::onSaveClick);
    connect(actOpen, &QAction::triggered, this, &MainWindow::onOpenClick);

    menuBar()->addMenu(menuFile);

    m_edit = new QTextEdit;
    setCentralWidget(m_edit);

}

MainWindow::~MainWindow() = default;

void MainWindow::onSaveClick()
{
    QString fileName = QFileDialog::getSaveFileName(this, "Simple notepad", "", "Text file (*.txt)");
    if (!fileName.isEmpty()){
        QFile file(fileName);
        if (file.open(QIODevice::WriteOnly | QIODevice::Text)){
            QTextStream out(&file);
            out << m_edit->toPlainText();
            file.close();
        }else{
            QMessageBox::critical(this, "Simple notepad", "Cannot write file!");
        };
    }
}

void MainWindow::onOpenClick()
{
    QString fileName = QFileDialog::getOpenFileName(this, "Simple notepad", "", "Text file (*.txt)");
    if (!fileName.isEmpty()){
        QFile file(fileName);
        if (file.open(QIODevice::ReadOnly | QIODevice::Text)){
            QTextStream in(&file);
            m_edit->setText(in.readAll());
            file.close();
        }else{
            QMessageBox::critical(this, "Simple notepad", "Cannot write file!");
        };
    }
}
