import sys
import vtk
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from vtkmodules.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor

class VTKWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("VTK with PyQt")
        self.resize(800, 600)

        # 创建中央部件（central widget）
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # 创建垂直布局
        layout = QVBoxLayout()
        self.central_widget.setLayout(layout)

        # 创建 VTK 渲染窗口（作为 Qt 小部件）
        self.vtk_widget = QVTKRenderWindowInteractor(self.central_widget)
        layout.addWidget(self.vtk_widget)

        # 创建渲染器
        self.renderer = vtk.vtkRenderer()

        # 让 QVTKRenderWindowInteractor 作为 VTK 的渲染窗口
        self.render_window = self.vtk_widget.GetRenderWindow()
        self.render_window.AddRenderer(self.renderer)

        # 创建球体并映射
        sphere = vtk.vtkSphereSource()
        sphere.SetPhiResolution(50)
        sphere.SetThetaResolution(50)

        mapper = vtk.vtkPolyDataMapper()
        mapper.SetInputConnection(sphere.GetOutputPort())

        actor = vtk.vtkActor()
        actor.SetMapper(mapper)

        # 添加球体到渲染器
        self.renderer.AddActor(actor)
        self.renderer.SetBackground(0.1, 0.2, 0.4)

        # 初始化 VTK 交互
        self.interactor = self.vtk_widget
        self.interactor.Initialize()
        self.interactor.Start()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = VTKWindow()
    window.show()
    sys.exit(app.exec())
