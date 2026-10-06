#include "mainwindow.h"
#include "./ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    connect(ui->lineEdit, &QLineEdit::textChanged, this, &MainWindow::recalculate);
    connect(ui->rb15, &QRadioButton::clicked, this, &MainWindow::recalculate);
    connect(ui->rb21, &QRadioButton::clicked, this, &MainWindow::recalculate);

}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::on_pushButton_clicked()
{
    ui->lineEdit->clear();
    ui->lineEdit_2->clear();
}

void MainWindow::recalculate()
{
    double value = 0;
    bool isCorrect = false;
    value = ui->lineEdit->text().toDouble(&isCorrect);
    if (isCorrect) {
        if (ui->rb15->isChecked()){
            value *= 1.15;
        } else if (ui->rb21->isChecked()){
            value *= 1.21;
        }
        ui->lineEdit_2->setText(QString("%1").arg(value));
    } else {
        ui->lineEdit_2->setText("N/A");
    }

}

